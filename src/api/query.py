import strawberry

from src.api.resolvers import (
    get_cities,
    get_countries,
    get_country_with_cities,
)
from src.api.types import City, Country, CountryWithCities


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    countries: list[Country] = strawberry.field(resolver=get_countries)
    cities: list[City] = strawberry.field(resolver=get_cities)
    country_with_cities: list[CountryWithCities] = strawberry.field(
        resolver=get_country_with_cities
    )
