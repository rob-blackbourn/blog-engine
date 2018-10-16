from graphql import (
    GraphQLSchema,
)

from .queries import RootQueryType
from .mutations import RootMutationType

schema = GraphQLSchema(
    query=RootQueryType,
    mutation=RootMutationType
)
