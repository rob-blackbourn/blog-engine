from easydict import EasyDict as edict
from graphql import (
    GraphQLObjectType,
    GraphQLString,
    GraphQLField,
    GraphQLNonNull,
    GraphQLID,
    GraphQLList
)

from ...resolvers.user import get_role_by_user_id

UserType = GraphQLObjectType(
    name='UserType',
    fields=lambda: {
        'id': GraphQLField(GraphQLID),
        'primaryEmail': GraphQLField(GraphQLNonNull(GraphQLString)),
        'password': GraphQLField(GraphQLNonNull(GraphQLString)),
        'secondaryEmails': GraphQLField(GraphQLList(GraphQLString)),
        'givenNames': GraphQLField(GraphQLList(GraphQLString)),
        'familyName': GraphQLField(GraphQLString),
        'nickname': GraphQLField(GraphQLString),
        'created': GraphQLField(GraphQLNonNull(GraphQLString)),
        'updated': GraphQLField(GraphQLNonNull(GraphQLString)),
        'roles': GraphQLField(
            GraphQLList(GraphQLString),
            resolve=get_role_by_user_id
        )
    }
)
