import strawberry
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from strawberry.fastapi import GraphQLRouter

from src.api.resolvers.context import ContextType
from src.api.schema.mutation import Mutation
from src.api.schema.query import Query
from src.api.schema.types import strawberry_sqlalchemy_mapper
from src.database.db import db


def get_context(
    session: AsyncSession = Depends(db.get_db),
) -> ContextType:
    return {"session": session}


strawberry_sqlalchemy_mapper.finalize()
additional_types = list(strawberry_sqlalchemy_mapper.mapped_types.values())
schema = strawberry.Schema(
    query=Query, mutation=Mutation, types=additional_types
)
graphql_app = GraphQLRouter[object, object](
    schema=schema, context_getter=get_context
)
