from typing import Optional

import strawberry
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

from src.database import models

strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()  # type: ignore


@strawberry_sqlalchemy_mapper.type(models.Country)
class Country:
    pass


@strawberry_sqlalchemy_mapper.type(models.City)
class City:
    pass


@strawberry.type
class ServerError:
    msg: str


@strawberry.type
class GetCountriesPayload:
    countries: Optional[list[Country]]
    severErrors: list[ServerError]


@strawberry.type
class GetCitiesPayload:
    cities: Optional[list[City]]
    severErrors: list[ServerError]


@strawberry.type
class GetCountryPayload:
    country: Optional[Country]
    severErrors: list[ServerError]


@strawberry.type
class AddCountryPayload:
    country: Optional[Country]
    severErrors: list[ServerError]


@strawberry.type
class UpdateCountryPayload:
    country: Optional[Country]
    severErrors: list[ServerError]


@strawberry.type
class DeleteCountryPayload:
    country: Optional[Country]
    severErrors: list[ServerError]
