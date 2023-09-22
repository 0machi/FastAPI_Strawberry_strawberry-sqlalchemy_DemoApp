from typing import Any


def add_country_mutation() -> tuple[str, dict[str, dict[str, dict[str, Any]]]]:
    mutation = """
    mutation {
        addCountry(input : {countryId: 4, countryName: "Switzerland"}) {
            country {
                countryId
                countryName
            }
            severErrors {
                msg
            }
        }
    }
    """
    excepted = {
        "data": {
            "addCountry": {
                "country": {"countryId": 4, "countryName": "Switzerland"},
                "severErrors": [],
            }
        }
    }
    return mutation, excepted
