import strawberry
from strawberry.field_extensions import InputMutationExtension

from src.api.types import Country, InternalServerError, NotFoundError, Ok
from src.libs.supabase.client import supabase_client


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
