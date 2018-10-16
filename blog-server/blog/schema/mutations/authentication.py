from graphql import (
    GraphQLField,
    GraphQLNonNull,
    GraphQLString,
    GraphQLArgument,
    GraphQLList
)

from ..types import (
    AuthenticationType,
    UserType
)

from ...resolvers.admin import (
    register_user,
    authenticate_user,
    update_roles
)

RegisterUserMutation = GraphQLField(
    AuthenticationType,
    args={
        'primaryEmail': GraphQLArgument(GraphQLNonNull(GraphQLString)),
        'password': GraphQLArgument(GraphQLNonNull(GraphQLString)),
        'secondaryEmails': GraphQLArgument(GraphQLList(GraphQLString)),
        'givenNames': GraphQLArgument(GraphQLList(GraphQLString)),
        'familyName': GraphQLArgument(GraphQLString),
        'nickname': GraphQLArgument(GraphQLString)
    },
    resolve=register_user
)

AuthenticateMutation = GraphQLField(
    AuthenticationType,
    args={
        'primaryEmail': GraphQLArgument(GraphQLNonNull(GraphQLString)),
        'password': GraphQLArgument(GraphQLNonNull(GraphQLString))
    },
    resolve=authenticate_user
)

UpdateRolesMutation = GraphQLField(
    UserType,
    args={
        'primaryEmail': GraphQLArgument(GraphQLNonNull(GraphQLString)),
        'roles': GraphQLArgument(GraphQLList(GraphQLString))
    },
    resolve=update_roles
)
