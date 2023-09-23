import strawberry
from strawberry.field_extensions import InputMutationExtension

from src.api.resolvers.mutations.country_resolver import CountryResolver
from src.api.schema.types import (
    AddCountryPayload,
    DeleteCountryPayload,
    UpdateCountryPayload,
)


@strawberry.type
class CountryMutation:
    add_country: AddCountryPayload = strawberry.mutation(
        resolver=CountryResolver.add_country,
        extensions=[InputMutationExtension()],
    )
    update_country: UpdateCountryPayload = strawberry.mutation(
        resolver=CountryResolver.update_country,
        extensions=[InputMutationExtension()],
    )
    delete_country: DeleteCountryPayload = strawberry.mutation(
        resolver=CountryResolver.delete_country,
        extensions=[InputMutationExtension()],
    )
