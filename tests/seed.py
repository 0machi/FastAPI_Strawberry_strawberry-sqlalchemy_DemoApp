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

init_stmts: list[str] = [
    f"INSERT INTO countries VALUES({us.country_id}, '{us.country_name}');",
    f"INSERT INTO cities VALUES({los_angeles.city_id}, {los_angeles.country_id}, '{los_angeles.city_name}', {los_angeles.population});",
    f"INSERT INTO cities VALUES({santa_monica.city_id}, {santa_monica.country_id}, '{santa_monica.city_name}', {santa_monica.population});",
    f"INSERT INTO countries VALUES({philippines.country_id}, '{philippines.country_name}');",
    f"INSERT INTO cities VALUES({cebu.city_id}, {cebu.country_id}, '{cebu.city_name}', {cebu.population});",
    f"INSERT INTO countries VALUES({japan.country_id}, '{japan.country_name}');",
]
