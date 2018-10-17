from inspect import isawaitable
import pytest
import graphql
from graphql.utilities.introspection_query import get_introspection_query

from blog.schema import schema


class MyMiddleware:

    async def resolve(self, next, root, info, *args, **kwargs):
        if isawaitable(next):
            response = await next(root, info, *args, **kwargs)
        else:
            response = next(root, info, *args, **kwargs)
        return response


def test_introspection():
    query = get_introspection_query()
    results = graphql.graphql_sync(schema, query, middleware=[MyMiddleware()])
    assert results.errors is None


@pytest.mark.asyncio
async def test_introspection_async():
    query = get_introspection_query()
    results = await graphql.graphql(schema, query, middleware=[MyMiddleware()])
    assert results.errors is None
