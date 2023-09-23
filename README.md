# Demo App using [FastAPI](https://fastapi.tiangolo.com/), GraphQL([Strawberry](https://strawberry.rocks/), [strawberry-sqlalchemy](https://github.com/strawberry-graphql/strawberry-sqlalchemy)), Docker
## System architecture
```mermaid
flowchart LR
    A[Browser] -->|GrapqhQL| B(FastAPI)
    B --> C[Strawberry]
    C --> D[strawberry-sqlalchemy]
    D --> E[SQLAlchemy]
    E --> F[(PostgreSQL)]
```


## How to run
1. Run Docker
- $ docker compose build --no-cache
- $ docker compose up
- $ docker compose start
2. DB migration
- $ task test
  - Before testing, DB migration, formatting by autoflake, black, isort, pyupgrade, and type checking by mypy are performed by [taskipy](https://github.com/taskipy/taskipy).
3. Run FastAPI
- $ uvicorn src.api.app:server --host 0.0.0.0 --reload
4. Access to GraghiQL
- http://localhost:8000/graphql

## Testing
- $ task test

## Render
- https://fastapi-strawberry-strawberry-sqlalchemy.onrender.com/graphql
