from motor.motor_asyncio import AsyncIOMotorClient

from ..models import (
    User,
    Permission,
    Blog,
    Post,
    Comment
)


async def startup(app):
    config = app['config'].mongo

    client = AsyncIOMotorClient(
        host=config.host,
        port=config.port,
        username=config.username,
        password=config.password,
        authSource=config.auth_source
    )

    db = client[config.database]

    for model in (User, Permission, Blog, Post, Comment):
        await model.qs(db).ensure_indices()

    app['mongo'] = db


async def shutdown(app):
    mongo_db = app['mongo']
    mongo_db.client.close()
