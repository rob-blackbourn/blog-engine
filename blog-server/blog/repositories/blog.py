from ..middlewares.authorization import authorize
from ..models import User, Blog
from .base import Repository
from ..utils.organiser import organise


class BlogRepository(Repository):
    GET_BLOGS_BY_USER_ID = 'get_blogs_by_user_id'

    def __init__(self):
        self.can_create_blog = authorize(all_roles=['blog:write'])
        self.can_read_blog = authorize(all_roles=['blog:read'])
        self.can_change_blog = authorize(all_roles=['blog:write'], is_owner=True)

    def register_data_loaders(self, registry):
        registry.register(self.GET_BLOGS_BY_USER_ID, self._get_blogs_by_owners)

    async def create(self, context, owner, title, content_type='text/plain', content=None):
        if not self.can_create_blog(context):
            raise Exception('unauthorised')

        blog = await Blog.qs(context.db).create(
            owner=owner,
            title=title,
            content_type=content_type,
            content=content)

        return blog

    async def read_one(self, context, owner, title):
        if not self.can_read_blog(context):
            raise Exception('unauthorised')

        blog = Blog.qs(context.db).find_one(owner=owner, title=title)

        return blog

    @classmethod
    async def _get_blogs_by_owners(cls, db, owner_ids):
        users = [User(id=id) for id in owner_ids]
        cursor = Blog.qs(db).find(owner={'$in': users})
        blogs = await organise(cursor, owner_ids, lambda blog: blog.owner._identity)
        return blogs

    async def read_many_by_owner(self, context, owner_id):
        if not self.can_read_blog(context):
            raise Exception('unauthorized')

        blogs = await context.data_loaders.load(BlogRepository.GET_BLOGS_BY_ID, owner_id)
        return blogs

    async def update(self, context, blog, title, content_type='text/plain', content=None):
        if not self.can_change_blog(context, blog.owner):
            raise Exception('unauthorised')

        await blog.qs(context.db).update(title=title, content_type=content_type, content=content)

        return blog

    async def delete(self, context, blog):
        if not self.can_change_blog(context, blog.owner):
            raise Exception('unauthorised')

        await blog.qs(context.db).delete()
