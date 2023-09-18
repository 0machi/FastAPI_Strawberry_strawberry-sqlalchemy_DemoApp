import strawberry

from src.api.resolvers.queries import (
    get_cities,
    get_countries,
    get_country_by_name,
)
from src.api.types import (
    GetCitiesPayload,
    GetCountriesPayload,
    GetCountryPayload,
)


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    countries: GetCountriesPayload = strawberry.field(resolver=get_countries)
    cities: GetCitiesPayload = strawberry.field(resolver=get_cities)
    country_by_name: GetCountryPayload = strawberry.field(
        resolver=get_country_by_name
    )
