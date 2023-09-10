import strawberry
from strawberry.fastapi import GraphQLRouter

from src.api.mutation import Mutation
from src.api.query import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter[object, object](schema=schema)
