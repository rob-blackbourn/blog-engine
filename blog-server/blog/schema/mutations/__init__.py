from graphql import (
    GraphQLObjectType,
)

RootMutationType = GraphQLObjectType(
    name='Mutations',
    fields=lambda: {
        'registerUser': RegisterUserMutation,
        'authenticate': AuthenticateMutation,
        'updateRoles': UpdateRolesMutation,
        'updateProfile': UpdateProfileMutation
    }
)

from .authentication import (
    RegisterUserMutation,
    AuthenticateMutation,
    UpdateRolesMutation,
)

from .user import (
    UpdateProfileMutation
)
