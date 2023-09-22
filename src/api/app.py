from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from src.api.schema.schema import graphql_app
from src.database.config import db_config
from src.database.session_manager import sessionmanager


def init_app(init_db: bool = True) -> FastAPI:
    lifespan = None

    if init_db:
        sessionmanager.init(dsn=db_config.dsn)

        @asynccontextmanager
        async def lifespan(app: FastAPI) -> AsyncIterator[None]:
            yield
            if sessionmanager._engine is not None:
                await sessionmanager.close()

    server = FastAPI(title="FastAPI server", lifespan=lifespan)
    server.include_router(graphql_app, prefix="/graphql")

    return server


server = init_app()
