import os
from dataclasses import dataclass, field


@dataclass
class Config:
    db: str
    user: str
    password: str
    host: str
    dsn: str = field(init=False)

    def __post_init__(self) -> None:
        self.dsn = f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:5432/{self.db}"


try:
    POSTGRES_DB = os.environ["POSTGRES_DB"]
    POSTGRES_USER = os.environ["POSTGRES_USER"]
    POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
    POSTGRES_HOST = os.environ["POSTGRES_HOST"]
except KeyError as e:
    print(f"Environment variable not set: {e}")

db_config = Config(
    db=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
)
