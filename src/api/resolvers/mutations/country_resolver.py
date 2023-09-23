from strawberry.types import Info

from src.api.resolvers.context import ContextType, RootValueType, get_session
from src.api.resolvers.stmts import country_stmt
from src.api.schema.types import (
    AddCountryPayload,
    DeleteCountryPayload,
    ServerError,
    UpdateCountryPayload,
)
from src.database.models import Country


class CountryResolver:
    async def add_country(
        self,
        info: Info[ContextType, RootValueType],
        country_id: int,
        country_name: str,
    ) -> AddCountryPayload:
        session = get_session(info)
        new_country = await country_stmt.add_country(
            session=session,
            country=Country(
                country_id=country_id, country_name=country_name, cities=[]
            ),
        )
        if new_country is None:
            return AddCountryPayload(
                country=None, severErrors=[ServerError(msg="Failed add_country.")]  # type: ignore
            )
        added_country = await country_stmt.get_country_by_name(
            session=session, country_name=country_name
        )
        if added_country is None:
            return AddCountryPayload(
                country=None, severErrors=[ServerError(msg="Failed add_country.")]  # type: ignore
            )
        return AddCountryPayload(
            country=added_country, severErrors=[]  # type: ignore
        )

    async def update_country(
        self,
        info: Info[ContextType, RootValueType],
        old_country_name: str,
        new_country_name: str,
    ) -> UpdateCountryPayload:
        session = get_session(info)
        country = await country_stmt.get_country_by_name(
            session=session, country_name=old_country_name
        )
        if country is None:
            return UpdateCountryPayload(
                country=None,
                severErrors=[
                    ServerError(msg=f"{old_country_name=} not found.")
                ],
            )
        updated_country = await country_stmt.update_country(
            session=session,
            old_country_name=old_country_name,
            new_country_name=new_country_name,
        )
        if updated_country is None:
            return UpdateCountryPayload(
                country=None,
                severErrors=[
                    ServerError(msg=f"{old_country_name=} not found.")
                ],
            )
        return UpdateCountryPayload(
            country=Country(**updated_country._asdict() | {"cities": []}),  # type: ignore
            severErrors=[],
        )

    async def delete_country(
        self, info: Info[ContextType, RootValueType], country_name: str
    ) -> DeleteCountryPayload:
        session = get_session(info)
        country = await country_stmt.get_country_by_name(
            session=session, country_name=country_name
        )
        if country is None:
            return DeleteCountryPayload(
                country=None,
                severErrors=[ServerError(msg=f"{country_name=} not found.")],
            )
        deleted_country = await country_stmt.delete_country(
            session=session, country_name=country_name
        )
        if deleted_country is None:
            return DeleteCountryPayload(
                country=None,
                severErrors=[ServerError(msg=f"{country_name=} not found.")],
            )
        return DeleteCountryPayload(
            country=Country(**deleted_country._asdict() | {"cities": []}),  # type: ignore
            severErrors=[],
        )
