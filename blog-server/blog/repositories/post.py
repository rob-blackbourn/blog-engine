from ..middlewares.authorization import authorize
from ..models import User, Blog, Post
from .base import Repository
from ..utils.organiser import organise


class PostRepository(Repository):
    GET_POSTS_BY_BLOGS = 'get_posts_by_blogs'

    def __init__(self):
        self.can_read = authorize(all_roles=['post:read'])
        self.can_write = authorize(all_roles=['post:write'], is_owner=True)

    def register_data_loaders(self, registry):
        registry.register(self.GET_POSTS_BY_BLOGS, self._read_many_by_blog)

    async def create(self, context, blog, title, status, content_type='text/plain', content=None):
        if not self.can_write(context, blog.owner):
            raise Exception('unauthenticated')

        post = Post.qs(context.db).create(blog=blog, title=title, status=status, content_type=content_type,
                                          content=content)
        return post

    async def read_one(self, context, blog, title):
        if not self.can_read(context):
            raise Exception('unauthenticated')

        post = await Post.qs(context.db).find_one(blog=blog, title=title)

        return post

    @classmethod
    async def _read_many_by_blog(cls, db, blog_ids):
        blogs = [Blog(id=id) for id in blog_ids]
        cursor = Blog.qs(db).find(owner={'$in': blogs})
        posts = await organise(cursor, blog_ids, lambda post: post.blog._identity)
        return posts

    async def read_many(self, context, blog_id):
        if not self.can_read(context):
            raise Exception('unauthorized')

        posts = await context.data_loaders.load(PostRepository.GET_POSTS_BY_BLOGS, blog_id)
        return posts

    async def update(self, context, post, title, status, content_type='text/plain', content=None):
        if not self.can_post(context, post.blog.owner):
            raise Exception('unauthenticated')

        post.qs(context.db).update(title=title, status=status, content_type=content_type, content=content)

        return post
