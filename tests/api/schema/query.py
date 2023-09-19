from typing import Any


def countries_query() -> tuple[str, dict[str, dict[str, dict[str, Any]]]]:
    query = """
    query {
        countries {
            countries {
                countryId
                countryName
                cities {
                    edges {
                        node {
                            cityId
                            cityName
                            population
                        }
                    }
                }
            }
            severErrors {
                msg
            }
        }
    }
    """
    expected = {
        "data": {
            "countries": {
                "countries": [
                    {
                        "countryId": 1,
                        "countryName": "US",
                        "cities": {
                            "edges": [
                                {
                                    "node": {
                                        "cityId": 1,
                                        "cityName": "Los Angeles",
                                        "population": 3849000,
                                    }
                                },
                                {
                                    "node": {
                                        "cityId": 2,
                                        "cityName": "Santa Monica",
                                        "population": 91000,
                                    }
                                },
                            ]
                        },
                    },
                    {
                        "countryId": 2,
                        "countryName": "Philippines",
                        "cities": {
                            "edges": [
                                {
                                    "node": {
                                        "cityId": 3,
                                        "cityName": "Cebu",
                                        "population": 3000000,
                                    }
                                }
                            ]
                        },
                    },
                ],
                "severErrors": [],
            }
        }
    }
    return query, expected
