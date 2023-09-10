from fastapi import FastAPI

from src.api.schema import graphql_app

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
