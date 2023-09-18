from fastapi import FastAPI

from src.api.schema.schema import graphql_app
from src.database.db import db

app = FastAPI()


@app.on_event("startup")
def startup() -> None:
    db.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    await db.disconnect()


app.include_router(graphql_app, prefix="/graphql")
