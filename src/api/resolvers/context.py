from typing import TypeVar, cast

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from strawberry.types import Info

from src.database.session_manager import get_db

RootValueType = TypeVar("RootValueType")
ContextType = dict[str, AsyncSession | Request]


def get_context(
    session: AsyncSession = Depends(get_db),
) -> ContextType:
    return {"session": session}


def get_session(info: Info[ContextType, RootValueType]) -> AsyncSession:
    session = cast(AsyncSession, info.context.get("session"))
    if session is None:
        raise ValueError("Session not found in context.")
    return session


def get_token(info: Info[ContextType, RootValueType]) -> str:
    authorization = cast(Request, info.context["request"]).headers.get(
        "Authorization", ""
    )
    token = authorization.replace("Bearer ", "")
    return token
