import os
from motor.motor_asyncio import AsyncIOMotorClient
import pytest
from easydict import EasyDict as edict
from blog.models import (User, Permission, Blog, Post, Comment)

from blog.server import load_config


@pytest.fixture
def config():
    filename = os.path.join(os.path.dirname(__file__), 'blog-server-test.yml')
    return load_config(filename)


@pytest.fixture
async def db(config):
    print('Connecting')
    client = AsyncIOMotorClient(
        host=config.mongo.host,
        port=config.mongo.port,
        username=config.mongo.username,
        password=config.mongo.password,
        authSource=config.mongo.auth_source
    )

    db = client[config.mongo.database]

    for model in (User, Permission, Blog, Post, Comment):
        await model.qs(db).ensure_indices()

    yield db
    print('Deleting database')
    await client.drop_database(db.name)
    print('Done')


@pytest.fixture
def unauthenticated_context(config, db):
    return edict(config=config, db=db)
