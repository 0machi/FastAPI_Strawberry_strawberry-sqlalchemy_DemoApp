import strawberry

from src.api.resolvers.queries.city_resolver import get_cities
from src.api.schema.types import GetCitiesPayload


@strawberry.type
class CityQuery:
    cities: GetCitiesPayload = strawberry.field(resolver=get_cities)
