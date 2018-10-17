import aiohttp_cors
from easydict import EasyDict as edict
from graphql.pyutils import EventEmitter

from ..schema import schema
from ..middlewares import AuthenticationMiddleware
from ..repositories import (
    AdminRepository,
    UserRepository,
    BlogRepository,
    PostRepository,
    CommentRepository
)
from ..resolvers.dataloader import DbDataLoaderRegistry

from ..controllers import GraphQLController


async def startup(app):
    authentication = AuthenticationMiddleware(whitelist=[
        '__schema',
        'registerUser',
        'authenticate'
    ])

    db = app['mongo']
    config = app['config']
    event_emitter = EventEmitter()

    repositories = edict(
        admin=AdminRepository(),
        user=UserRepository(),
        blog=BlogRepository(),
        post=PostRepository(),
        comment=CommentRepository()
    )

    data_loader_registry = DbDataLoaderRegistry()
    for repository in repositories.values():
        repository.register_data_loaders(data_loader_registry)

    context_builder = lambda request: edict(
        config=config,
        db=db,
        event_emitter=event_emitter,
        repositories=repositories,
        data_loaders=data_loader_registry.create_loders(db),
        request=request
    )

    middleware = [
        authentication
    ]

    controller = GraphQLController(schema, context_builder, middleware)
    routes = controller.add_routes(app)

    app['graphql'] = controller

    # Configure default CORS settings.
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    for route in routes:
        cors.add(route)


async def shutdown(app):
    await app['graphql'].shutdown()
