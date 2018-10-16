from easydict import EasyDict as edict
from ..models import User, Blog
from ..utils.organiser import organise
from ..utils.casing import dict_to_snakecase_dict, dict_to_camelcase_dict
from ..middlewares.authorization import authorize
from graphql import (
    GraphQLError
)


async def create_blog(root, info, *args, **kwargs):
    if not authorize(all_roles=['post:write'])(info.context):
        raise GraphQLError('unauthorized')

    params = dict_to_snakecase_dict(kwargs, edict)
    blog = await Blog.qs(info.context.db).create(**params)

    return edict(dict_to_camelcase_dict(blog.to_dict()))


async def update_blog_by_id_and_title(root, info, *args, **kwargs):
    id = kwargs.pop('id')
    title = kwargs.pos('title')
    blog = await Blog.qs(info.context.db).find_one(id=id, title=title)

    if not authorize(all_roles=['post:write'], is_owner=True)(info.context, blog.owner):
        raise GraphQLError('unauthorized')

    blog.qs(info.context.db).update(**kwargs)
    return edict(dict_to_camelcase_dict(blog.to_dict()))


def _get_blogs_by_user_ids(db, user_ids):
    users = [User(id=id) for id in user_ids]
    cursor = Blog.qs(db).find(owner={'$in': users})
    blogs = await organise(
        cursor,
        user_ids,
        lambda blog: blog.owner._identity,
        lambda blog: blog,
        True)
    return blogs


async def get_blogs_by_user_id(root, info, *args, **kwargs):
    if not authorize(any_role=['admin'])(info.context):
        raise GraphQLError('unauthorized')

    roles = await info.context.data_loaders.load('blogs_by_user_id', root.id)
    return roles
