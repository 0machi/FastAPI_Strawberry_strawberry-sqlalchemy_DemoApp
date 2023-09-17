import strawberry
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from strawberry.fastapi import GraphQLRouter

from src.api.mutation import Mutation
from src.api.query import Query
from src.database.db import db


def get_context(
    session: AsyncSession = Depends(db.get_db),
) -> dict[str, AsyncSession]:
    return {"session": session}


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter[object, object](
    schema=schema, context_getter=get_context
)
