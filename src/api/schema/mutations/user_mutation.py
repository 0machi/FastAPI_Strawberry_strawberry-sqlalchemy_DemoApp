import strawberry
from strawberry.field_extensions import InputMutationExtension

from src.api.resolvers.mutations.user_resolver import UserResolver
from src.api.schema.types import LoginPayload


@strawberry.type
class UserMutation:
    login: LoginPayload = strawberry.mutation(
        resolver=UserResolver.login,
        extensions=[InputMutationExtension()],
    )
