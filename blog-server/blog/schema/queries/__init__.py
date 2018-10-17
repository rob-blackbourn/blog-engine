from graphql import (
    GraphQLObjectType,
)

RootQueryType = GraphQLObjectType(
    name='Queries',
    fields=lambda: {
        'userById': UserByIdQuery,
        'userByPrimaryEmail': UserByPrimaryEmailQuery,
        'users': UsersQuery,
        'currentUser': CurrentUserQuery
    }
)

from .user import (
    UserByIdQuery,
    UserByPrimaryEmailQuery,
    UsersQuery,
    CurrentUserQuery
)
