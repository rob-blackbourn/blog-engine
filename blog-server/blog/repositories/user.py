from easydict import EasyDict as edict
from ..models import User, Permission
from ..utils.organiser import organise
from ..utils.casing import dict_to_camelcase_dict
from ..middlewares.authorization import authorize
from .base import Repository


class UserRepository(Repository):
    GET_ROLES_BY_USER_ID = 'user:get_roles_id'
    GET_USER_BY_ID = 'user:get_by_id'
    GET_USER_BY_PRIMARY_EMAIL = 'user:get_by_primary_email'

    def __init__(self):
        self.can_read_other_users = authorize(any_role=['admin'])

    def register_data_loaders(self, registry):
        registry.register(self.GET_ROLES_BY_USER_ID, self._get_roles_by_user_ids)
        registry.register(self.GET_USER_BY_ID, self._get_users_by_ids)
        registry.register(self.GET_USER_BY_PRIMARY_EMAIL, self._get_users_by_primary_emails)

    @classmethod
    async def _get_roles_by_user_ids(cls, db, user_ids):
        users = [User(id=id) for id in user_ids]
        cursor = Permission.qs(db).find(user={'$in': users})
        permissions = await organise(
            cursor,
            user_ids,
            lambda permission: permission.user._identity,
            lambda permission: permission.roles,
            True)
        return permissions

    @classmethod
    async def _get_users_by_ids(cls, db, ids):
        cursor = User.qs(db).find(id={'$in': ids})
        users = await organise(cursor, ids, lambda user: user.id)
        return users

    @classmethod
    async def _get_users_by_primary_emails(cls, db, primary_emails):
        cursor = User.qs(db).find(primary_email={'$in': primary_emails})
        users = await organise(cursor, primary_emails, lambda user: user.primary_email)
        return users

    async def get_all_users(self, context):
        if not self.can_read_other_users(context):
            raise Exception('unauthorized')

        users = [user async for user in User.qs(context.db).find()]
        return [dict_to_camelcase_dict(user.to_dict(), edict) for user in users]

    async def get_current_user(self, context):
        user = dict_to_camelcase_dict(context.user.to_dict(), edict)
        return user

    async def get_role_by_user_id(self, context, id):
        if not self.can_read_other_users(context):
            raise Exception('unauthorized')

        roles = await context.data_loaders.load(UserRepository.GET_ROLES_BY_USER_ID, id)
        return roles

    async def get_user_by_id(self, context, id):
        if not self.can_read_other_users(context):
            raise Exception('unauthorized')

        user = await context.data_loaders.load(UserRepository.GET_USER_BY_ID, id)
        return user

    async def get_user_by_primary_email(self, context, primary_email):
        if not self.can_read_other_users(context):
            raise Exception('unauthorized')

        user = await context.data_loaders.load(UserRepository.GET_USER_BY_PRIMARY_EMAIL, primary_email)
        return user
