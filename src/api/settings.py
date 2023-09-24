import os
from dataclasses import dataclass


@dataclass
class Settings:
    env: str


try:
    env = os.environ["ENV"]
except KeyError as e:
    print(f"Environment variable not set: {e}")

settings = Settings(env=env)
