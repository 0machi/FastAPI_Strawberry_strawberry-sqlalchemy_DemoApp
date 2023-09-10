import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.field_extensions import InputMutationExtension

from src.libs.supabase.client import supabase_client


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


async def get_country() -> list[Country]:
    try:
        result = supabase_client.table("countries").select("*").execute()
        return [Country(**country) for country in result.data]
    except Exception:
        return []


async def get_countries() -> list[Country]:
    try:
        result = supabase_client.table("countries").select("*").execute()
        return [Country(**country) for country in result.data]
    except Exception:
        return []


async def get_cities() -> list[City]:
    try:
        result = supabase_client.table("cities").select("*").execute()
        return [City(**city) for city in result.data]
    except Exception:
        return []


async def get_country_with_cities() -> list[CountryWithCities]:
    try:
        result = (
            supabase_client.table("countries").select("*, cities(*)").execute()
        )
        return [
            CountryWithCities(
                country=Country(
                    country_id=row["country_id"],
                    country_name=row["country_name"],
                ),
                cities=[City(**city) for city in row["cities"]],
            )
            for row in result.data
        ]
    except Exception:
        return []


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


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_country(
        self, country_id: int, country_name: str
    ) -> Country | InternalServerError:
        try:
            result = (
                supabase_client.table("countries")
                .insert(
                    {"country_id": country_id, "country_name": country_name}
                )
                .execute()
            )
            return Country(**result.data[0])
        except Exception as e:
            return InternalServerError(msg=f"Internal server error {e=}.")

    @strawberry.mutation(extensions=[InputMutationExtension()])
    async def update_country(
        self, country_id: int, country_name: str
    ) -> Country | NotFoundError | InternalServerError:
        try:
            result = (
                supabase_client.table("countries")
                .select("*")
                .eq("country_id", country_id)
                .execute()
            )
            if not result.data:
                return NotFoundError(msg=f"{country_id=} not found.")
            result = (
                supabase_client.table("countries")
                .update({"country_name": country_name})
                .eq("country_id", country_id)
                .execute()
            )
            return Country(**result.data[0])
        except Exception as e:
            return InternalServerError(msg=f"Internal server error {e=}.")

    @strawberry.mutation
    async def delete_country(
        self, country_id: int
    ) -> Ok | NotFoundError | InternalServerError:
        try:
            result = (
                supabase_client.table("countries")
                .select("*")
                .eq("country_id", country_id)
                .execute()
            )
            if not result.data:
                return NotFoundError(msg=f"{country_id=} not found.")
            supabase_client.table("countries").delete().eq(
                "country_id", country_id
            ).execute()
            return Ok(msg=f"Delete success {country_id=}.")
        except Exception as e:
            return InternalServerError(msg=f"Internal server error {e=}.")


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter[object, object](schema=schema)
