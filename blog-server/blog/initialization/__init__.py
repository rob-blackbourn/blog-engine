from .mongo import (
    startup as startup_mongo,
    shutdown as shutdown_mongo
)
from .graphql import (
    startup as startup_graphql,
    shutdown as shutdown_graphql
)


def initialize(app):
    # Mongo
    app.on_startup.append(startup_mongo)
    app.on_shutdown.append(shutdown_mongo)

    # GraphQL
    app.on_startup.append(startup_graphql)
    app.on_shutdown.append(shutdown_graphql)
