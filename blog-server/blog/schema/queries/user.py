from easydict import EasyDict as edict
from graphql import (
    GraphQLArgument,
    GraphQLList,
    GraphQLString,
    GraphQLField,
    GraphQLNonNull,
)

from ..types.user import UserType
from ...resolvers.user import (
    get_user_by_id,
    get_user_by_primary_email,
    get_all_users,
    get_current_user
)

UserByIdQuery = GraphQLField(
    UserType,
    args={
        'id': GraphQLArgument(GraphQLNonNull(GraphQLString))
    },
    description="The user identified by their id",
    resolve=get_user_by_id
)

UserByPrimaryEmailQuery = GraphQLField(
    UserType,
    args={
        'email': GraphQLArgument(GraphQLNonNull(GraphQLString))
    },
    description="The user identified by their primary email address",
    resolve=get_user_by_primary_email
)

UsersQuery = GraphQLField(
    GraphQLList(UserType),
    description='All of the the users',
    resolve=get_all_users
)

CurrentUserQuery = GraphQLField(
    UserType,
    description='The current user',
    resolve=get_current_user
)
