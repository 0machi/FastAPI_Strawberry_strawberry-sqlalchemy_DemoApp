from typing import TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from strawberry.types import Info

RootValueType = TypeVar("RootValueType")
ContextType = dict[str, AsyncSession]


def get_session(info: Info[ContextType, RootValueType]) -> AsyncSession:
    session = info.context.get("session")
    if session is None:
        raise ValueError("Session not found in context.")
    return session
