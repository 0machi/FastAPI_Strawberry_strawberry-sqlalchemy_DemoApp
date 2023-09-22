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


def update_country_mutation() -> (
    tuple[str, dict[str, dict[str, dict[str, Any]]]]
):
    mutation = """
    mutation {
        updateCountry(input : { oldCountryName: "Japan", newCountryName: "JP"}) {
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
            "updateCountry": {
                "country": {"countryId": 3, "countryName": "JP"},
                "severErrors": [],
            }
        }
    }
    return mutation, excepted
