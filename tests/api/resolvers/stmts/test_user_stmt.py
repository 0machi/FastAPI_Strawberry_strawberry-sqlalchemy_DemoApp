from uuid import UUID

import pytest

from src.api.resolvers.stmts.user_stmt import get_user_by_id
from src.database.session_manager import DatabaseSessionManager
from tests.seed import admin


@pytest.mark.asyncio
async def test_get_user_by_id(session: DatabaseSessionManager) -> None:
    async with session.session() as s:
        actual = await get_user_by_id(
            session=s, id=UUID("fceef692-010b-480f-899c-5a6e8bab23a7")
        )
        assert actual == admin
