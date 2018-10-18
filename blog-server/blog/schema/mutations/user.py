from graphql import (
    GraphQLField,
    GraphQLNonNull,
    GraphQLString,
    GraphQLArgument,
    GraphQLList
)

from ..types import (
    UserType
)

from ...resolvers.user import (
    update_profile
)

UpdateProfileMutation = GraphQLField(
    UserType,
    args={
        'originalPrimaryEmail': GraphQLArgument(GraphQLNonNull(GraphQLString)),
        'primaryEmail': GraphQLArgument(GraphQLNonNull(GraphQLString)),
        'secondaryEmails': GraphQLArgument(GraphQLList(GraphQLString)),
        'givenNames': GraphQLArgument(GraphQLList(GraphQLString)),
        'familyName': GraphQLArgument(GraphQLString),
        'nickname': GraphQLArgument(GraphQLString)
    },
    resolve=update_profile
)
