from aiohttp import web
import asyncio
from easydict import EasyDict as edict
from graphql import graphql
import graphql_ws
from graphql_ws.aiohttp import AiohttpConnectionContext
import json

from .graphiql_template import make_template


class GraphQLController:

    def __init__(self, schema, context_builder, middleware):
        self.schema = schema
        self.context_builder = context_builder
        self.middleware = middleware

        self.subscription_server = graphql_ws.SubscriptionServer(
            schema, AiohttpConnectionContext
        )
        self.websockets = set()


    def add_routes(self, app):
        routes = [
            app.router.add_get("/graphiql", self.handle_root),
            app.router.add_get("/graphql", self.handle_graphql),
            app.router.add_post("/graphql", self.handle_graphql),
            app.router.add_get("/subscriptions", self.handle_subscriptions)
        ]

        return routes


    async def shutdown(self):
        if len(self.websockets) > 0:
            await asyncio.wait([wsr.close() for wsr in self.websockets])


    async def handle_root(self, request):
        template = make_template(request.host)
        return web.Response(text=template, content_type="text/html")


    async def handle_subscriptions(self, request):
        response = web.WebSocketResponse(protocols=(graphql_ws.WS_PROTOCOL,))
        self.websockets.add(response)
        await response.prepare(request)
        await self.subscription_server.handle(response, self.context_builder(request))
        self.websockets.remove(response)
        return response


    async def get_query_document(self, request, content_type):
        if content_type in ("application/graphql"):
            return {'query': await request.text()}
        elif content_type in ("application/json", "text/plain"):
            return await request.json()
        elif request.content_type in (
                "application/x-www-form-urlencoded",
                "multipart/form-data",
        ):
            return await dict(request.post())

        raise Exception(f"Unhandled content type '{content_type}'")


    async def handle_graphql(self, request):

        query_document = await self.get_query_document(request, request.content_type)

        print(query_document['query'])

        result = await graphql(
            self.schema,
            source=query_document['query'],
            variable_values=query_document.get('variables', None),
            operation_name=query_document.get('operationName', None),
            context_value=self.context_builder(request),
            middleware=self.middleware
        )

        response = {'data': result.data}
        if result.errors:
            response["errors"] = [error.formatted for error in result.errors]

        return web.json_response(response)
