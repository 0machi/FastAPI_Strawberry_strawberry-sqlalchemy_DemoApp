from typing import Any


def cities_query() -> tuple[str, dict[str, dict[str, dict[str, Any]]]]:
    query = """
    query {
        cities {
            cities {
                cityId
                cityName
                countryId
                population
            }
            severErrors {
                msg
            }
        }
    }
    """

    expected = {
        "data": {
            "cities": {
                "cities": [
                    {
                        "cityId": 1,
                        "cityName": "Los Angeles",
                        "countryId": 1,
                        "population": 3849000,
                    },
                    {
                        "cityId": 2,
                        "cityName": "Santa Monica",
                        "countryId": 1,
                        "population": 91000,
                    },
                    {
                        "cityId": 3,
                        "cityName": "Cebu",
                        "countryId": 2,
                        "population": 3000000,
                    },
                ],
                "severErrors": [],
            }
        }
    }

    return query, expected
