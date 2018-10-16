import logging

logger = logging.getLogger(__name__)


def has_any_role(required_roles, user_roles):
    if not required_roles or len(required_roles) == 0:
        return True

    for required_role in required_roles:
        if required_role in user_roles:
            return True

    return False


def has_all_roles(required_roles, user_roles):
    if not required_roles or len(required_roles) == 0:
        return True

    for required_role in required_roles:
        if required_role not in user_roles:
            return False

    return True


def authorize(*, any_role=[], all_roles=[], is_owner=False, owner_roles=None):
    def authorize_roles(context, owner=None):
        logger.debug('Authorizing user roles')

        if not ('user' in context and 'permission' in context):
            logger.debug('User not authenticated')
            return False

        user, permission = context.user, context.permission
        if not has_any_role(any_role, permission.roles):
            logger.debug(f"User '{user.primary_email}' did not have any required role {any_role}")
            return False

        if not has_all_roles(all_roles, permission.roles):
            logger.debug(f"User '{user.primary_email}' did not have all required roles {all_roles}")

        if is_owner and not (
                user == owner or has_any_role(owner_roles, permission.roles)):
            logger.debug(f"User {user.primary_email} is not the owner '{owner.primary_email}' or an owner role")

        logger.debug(f"User '{user.primary_email}' is authorized.")
        return True

    return authorize_roles
