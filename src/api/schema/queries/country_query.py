import strawberry

from src.api.resolvers.queries import get_countries, get_country_by_name
from src.api.schema.types import GetCountriesPayload, GetCountryPayload


@strawberry.type
class CountryQuery:
    countries: GetCountriesPayload = strawberry.field(resolver=get_countries)
    country_by_name: GetCountryPayload = strawberry.field(
        resolver=get_country_by_name
    )
