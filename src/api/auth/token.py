import os
from datetime import datetime, timedelta

from jose import jwt

try:
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
    ACCESS_TOKEN_EXPIRE_MINUTES = float(
        os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"]
    )
except KeyError as e:
    print(f"Environment variable not set: {e}")


def create_access_token(data: dict[str, str | datetime]) -> str:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": expire})
    return str(jwt.encode(claims=data, key=JWT_SECRET_KEY, algorithm="HS256"))


def get_access_token_data(token: str) -> dict[str, str | datetime]:
    return dict(
        jwt.decode(token=token, key=JWT_SECRET_KEY, algorithms=["HS256"])
    )
