# Demo App using [FastAPI](https://fastapi.tiangolo.com/), GraphQL([Strawberry](https://strawberry.rocks/), [strawberry-sqlalchemy](https://github.com/strawberry-graphql/strawberry-sqlalchemy)), Docker
## System Architecture
### dev
```mermaid
flowchart LR
    A[Browser] -->|GrapqhQL| B(FastAPI)
subgraph Docker
    services.demo-app
    services.postgresql
end
subgraph services.demo-app
    B --> C[Strawberry]
    C --> D[strawberry-sqlalchemy]
    D --> E[SQLAlchemy]
end
subgraph services.postgresql
    E --> F[(PostgreSQL)]
end
```

### prod
```mermaid
flowchart LR
    A[Browser] -->|GrapqhQL| B(FastAPI)
subgraph Render
    DockerFile
end
subgraph DockerFile
    B --> C[Strawberry]
    C --> D[strawberry-sqlalchemy]
    D --> E[SQLAlchemy]
end
subgraph Supabase
    E --> F[(PostgreSQL)]
end
```

## How to Run
1. Run Docker
- $ docker compose build --no-cache
- $ docker compose up
2. Access to GraghiQL
- http://localhost:8000/graphql

## Testing
- $ task test
  - Before testing, formatting by autoflake, black, isort, pyupgrade, and type checking by mypy are performed by [taskipy](https://github.com/taskipy/taskipy).

## Demo with Render
1. Get token
```bash
$ curl -Ss \
-X POST \
-H "Content-Type: application/json" \
--data '{ "query": "mutation { login(input: { id: \"fceef692-010b-480f-899c-5a6e8bab23a7\", password: \"admin\" }) { tokenType accessToken severErrors { msg } } }" }' \
https://fastapi-strawberry-strawberry-sqlalchemy.onrender.com/graphql | jq .
```
```json
{
  "data": {
    "login": {
      "tokenType": "bearer",
      "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmY2VlZjY5Mi0wMTBiLTQ4MGYtODk5Yy01YTZlOGJhYjIzYTciLCJleHAiOjE2OTU1NDg0MTh9.YFvZL07ZTFDURfdzaU_Xk096iz2nLdeJ2gBcgmL6xSA",
      "severErrors": []
    }
  }
}
```

2. Excec query
```bash
curl -Ss \
-X POST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmY2VlZjY5Mi0wMTBiLTQ4MGYtODk5Yy01YTZlOGJhYjIzYTciLCJleHAiOjE2OTU1NDg0MTh9.YFvZL07ZTFDURfdzaU_Xk096iz2nLdeJ2gBcgmL6xSA" \
--data '{ "query": "query { cities { cities { cityId cityName population } } }" }' \
https://fastapi-strawberry-strawberry-sqlalchemy.onrender.com/graphql | jq .
```
```json
{
  "data": {
    "cities": {
      "cities": [
        {
          "cityId": 1,
          "cityName": "Los Angeles",
          "population": 3849000
        },
        {
          "cityId": 2,
          "cityName": "Santa Monica",
          "population": 91000
        },
        {
          "cityId": 3,
          "cityName": "Cebu",
          "population": 3000000
        }
      ]
    }
  }
}
```
