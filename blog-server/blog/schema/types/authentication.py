from graphql import (
    GraphQLObjectType,
    GraphQLString,
    GraphQLField,
    GraphQLNonNull
)

AuthenticationType = GraphQLObjectType(
    name='Authentication',
    fields=lambda: {
        'token': GraphQLField(
            GraphQLNonNull(GraphQLString),
            description="Set the Authorization header to 'Bearer <token>'"),
        'message': GraphQLField(GraphQLString)
    }
)
