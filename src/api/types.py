import strawberry
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

from src.database import models

strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()  # type: ignore


@strawberry.type
class Country:
    country_id: int
    country_name: str


@strawberry.type
class City:
    city_id: int
    country_id: int
    city_name: str
    population: int


@strawberry.type
class CountryWithCities:
    country: Country
    cities: list[City]


@strawberry.type
class NotFoundError:
    msg: str


@strawberry.type
class InternalServerError:
    msg: str


@strawberry.type
class Ok:
    msg: str


@strawberry_sqlalchemy_mapper.type(models.Country)
class Hoge:
    pass
