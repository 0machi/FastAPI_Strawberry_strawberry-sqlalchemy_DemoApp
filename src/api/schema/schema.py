import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.tools import merge_types

from src.api.resolvers.context import get_context
from src.api.schema.mutations.country_mutation import CountryMutation
from src.api.schema.mutations.user_mutation import UserMutation
from src.api.schema.queries.city_query import CityQuery
from src.api.schema.queries.country_query import CountryQuery
from src.api.schema.types import strawberry_sqlalchemy_mapper
from src.api.settings import settings

strawberry_sqlalchemy_mapper.finalize()
additional_types = list(strawberry_sqlalchemy_mapper.mapped_types.values())
all_queries = merge_types("AllQueries", (CityQuery, CountryQuery))
all_mutations = merge_types("AllMutations", (CountryMutation, UserMutation))
schema = strawberry.Schema(
    query=all_queries, mutation=all_mutations, types=additional_types
)
graphql_app = GraphQLRouter[object, object](
    schema=schema, context_getter=get_context, graphiql=settings.env == "dev"
)
