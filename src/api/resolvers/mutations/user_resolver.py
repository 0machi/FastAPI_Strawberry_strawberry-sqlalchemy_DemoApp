from uuid import UUID

from strawberry.types import Info

from src.api.auth.password import verify_password
from src.api.auth.token import create_access_token
from src.api.resolvers.context import ContextType, RootValueType, get_session
from src.api.resolvers.stmts import user_stmt
from src.api.schema.types import LoginPayload, ServerError


class UserResolver:
    async def login(
        self,
        info: Info[ContextType, RootValueType],
        id: UUID,
        password: str,
    ) -> LoginPayload:
        session = get_session(info)
        user = await user_stmt.get_user_by_id(session=session, id=id)

        if user is None:
            return LoginPayload(
                access_token=None,
                token_type=None,
                severErrors=[
                    ServerError(msg="UserId or password is invalid.")
                ],
            )

        if not verify_password(
            plain_password=password, hashed_password=user.encrypted_password
        ):
            return LoginPayload(
                access_token=None,
                token_type=None,
                severErrors=[
                    ServerError(msg="UserId or password is invalid.")
                ],
            )

        access_token = create_access_token(data={"sub": str(user.id)})
        return LoginPayload(
            access_token=access_token, token_type="bearer", severErrors=[]
        )
