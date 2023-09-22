from src.database.models import City, Country

los_angeles = City(
    city_id=1, country_id=1, city_name="Los Angeles", population=3849000
)
santa_monica = City(
    city_id=2, country_id=1, city_name="Santa Monica", population=91000
)
us = Country(
    country_id=1, country_name="US", cities=[los_angeles, santa_monica]
)

cebu = City(city_id=3, country_id=2, city_name="Cebu", population=3000000)
philippines = Country(country_id=2, country_name="Philippines", cities=[cebu])

japan = Country(country_id=3, country_name="Japan", cities=[])


countries: list[Country] = [us, philippines, japan]
cities: list[City] = [los_angeles, santa_monica, cebu]
