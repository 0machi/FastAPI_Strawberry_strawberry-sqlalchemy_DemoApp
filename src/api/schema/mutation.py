import strawberry
from strawberry.field_extensions import InputMutationExtension

from src.api.resolvers.mutations import Mutations
from src.api.schema.types import (
    AddCountryPayload,
    DeleteCountryPayload,
    UpdateCountryPayload,
)


@strawberry.type
class Mutation:
    add_country: AddCountryPayload = strawberry.mutation(
        resolver=Mutations.add_country, extensions=[InputMutationExtension()]
    )
    update_country: UpdateCountryPayload = strawberry.mutation(
        resolver=Mutations.update_country,
        extensions=[InputMutationExtension()],
    )
    delete_country: DeleteCountryPayload = strawberry.mutation(
        resolver=Mutations.delete_country,
        extensions=[InputMutationExtension()],
    )
