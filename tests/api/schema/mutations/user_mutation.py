from typing import Any


def login_mutation() -> tuple[str, dict[str, dict[str, dict[str, Any]]]]:
    mutation = """
    mutation {
        login(input : { id: "fceef692-010b-480f-899c-5a6e8bab23a7", password: "admin" }) {
            tokenType
            accessToken
            severErrors {
                msg
            }
        }
    }
    """
    excepted = {
        "data": {
            "login": {
                "tokenType": "bearer",
                "accessToken": "accessToken",
                "severErrors": [],
            }
        }
    }
    return mutation, excepted
