from src.api.types import City, Country, CountryWithCities
from src.libs.supabase.client import supabase_client


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
