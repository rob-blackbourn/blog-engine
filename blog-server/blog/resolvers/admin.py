from ..utils.casing import dict_to_snakecase_dict


async def register_user(root, info, *args, **kwargs):
    return await info.context.repositories.admin.register_user(
        info.context,
        **dict_to_snakecase_dict(kwargs))


async def authenticate_user(root, info, *args, **kwargs):
    return await info.context.repositories.admin.authenticate_user(
        info.context,
        **dict_to_snakecase_dict(kwargs))


async def update_roles(root, info, *args, **kwargs):
    return await info.context.repositories.admin.update_roles(
        info.context,
        **dict_to_snakecase_dict(kwargs))
