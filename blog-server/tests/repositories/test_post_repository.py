import asyncio
import pytest

from motor.motor_asyncio import AsyncIOMotorClient

from blog.repositories import PostRepository


@pytest.mark.asyncio
async def test_create_blog(db):
    post_repository = PostRepository()

    collection = db['posts']
    result = await collection.insert_one({'name': 'Rob'})
    assert result.inserted_id is not None
