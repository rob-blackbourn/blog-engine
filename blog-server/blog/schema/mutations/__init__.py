from graphql import (
    GraphQLObjectType,
)

RootMutationType = GraphQLObjectType(
    name='Mutations',
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
