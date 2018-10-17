from inspect import isawaitable
import jwt
import logging
from cachetools import TTLCache

logger = logging.getLogger(__name__)

from ..models import (
    User,
    Permission
)


class AuthenticationMiddleware(object):

    def __init__(self, whitelist=[], maxsize=1000, ttl=60 * 60):
        self.whitelist = whitelist
        self._cache = TTLCache(maxsize=maxsize, ttl=ttl)


    def is_whitelisted(self, responsePath):
        for name in self.whitelist:
            if responsePath.key == name:
                logger.debug(f"Path is whitelisted: {responsePath}")
                return True
        return False


    async def _get_user_and_permission(self, db, user_id):
        user, permission = self._cache.get(user_id, (None, None))
        if user and permission:
            logger.debug('Using cached credentials')
        else:
            logger.debug(f"Getting credentials for '{user_id}'")
            user = await User.qs(db).get(user_id)
            permission = await Permission.qs(db).find_one(user={'$eq': user}) if user else None
            self._cache[user_id] = (user, permission)
        return user, permission


    async def _authenticate(self, context):

        scheme, token = context.request.headers['authorization'].split(' ')
        if scheme.lower() != 'bearer':
            raise Exception('invalid token')
        payload = jwt.decode(token, key=context.config.authentication.secret)

        if not payload['sub']:
            raise Exception('token contains no "sub"')

        user_id = payload['sub']

        return await self._get_user_and_permission(context.db, user_id)


    async def resolve(self, next, root, info, *args, **kwargs):
        logger.debug(f"Authenticating {info.path}")
        try:
            if self.is_whitelisted(info.path):
                logger.debug(f"Path is whitelisted: {info.path}")
            elif 'user' in info.context:
                logger.debug(f"Path is already authenticated: {info.path}")
            else:
                logger.debug(f"Path requires authentication {info.path}")
                user, permission = await self._authenticate(info.context)
                info.context.user = user
                info.context.permission = permission
        except:
            logger.debug(f'Failed to authenticate {info.path}')
        finally:
            response = next(root, info, *args, **kwargs)
            return await response if isawaitable(response) else response
