async def get_all_users(root, info, *args, **kwargs):
    return await info.context.repositoreis.user.get_all_users(
        info.context
    )


async def get_current_user(root, info, *args, **kwargs):
    return await info.context.repositories.user.get_current_user(
        info.context
    )


async def get_role_by_user_id(root, info, *args, **kwargs):
    return await info.context.repositories.user.get_role_by_user_id(
        info.context,
        root.id
    )


async def get_user_by_id(root, info, *args, **kwargs):
    return await info.context.repositories.user.get_user_by_id(
        info.context,
        kwargs['id']
    )


async def get_user_by_primary_email(root, info, *args, **kwargs):
    return await info.context.repositories.user.get_user_by_primary_email(
        info.context,
        kwargs['email']
    )
