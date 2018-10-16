from graphql import (
    GraphQLObjectType,
)

RootMutationType = GraphQLObjectType(
    name='RootMutationType',
    fields=lambda: {
        'registerUser': RegisterUserMutation,
        'authenticate': AuthenticateMutation,
        'updateRoles': UpdateRolesMutation
    }
)

from .authentication import (
    RegisterUserMutation,
    AuthenticateMutation,
    UpdateRolesMutation
)
