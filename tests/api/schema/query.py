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
                            countryId
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
                                        "countryId": 1,
                                        "population": 3849000,
                                    }
                                },
                                {
                                    "node": {
                                        "cityId": 2,
                                        "cityName": "Santa Monica",
                                        "countryId": 1,
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
                                        "countryId": 2,
                                        "population": 3000000,
                                    }
                                }
                            ]
                        },
                    },
                    {
                        "countryId": 3,
                        "countryName": "Japan",
                        "cities": {"edges": []},
                    },
                ],
                "severErrors": [],
            }
        }
    }
    return query, expected


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


def country_by_name_query() -> (
    tuple[str, dict[str, dict[str, dict[str, Any]]]]
):
    query = """
    query {
        countryByName(countryName: "US") {
            country {
                countryId
                countryName
                cities {
                    edges {
                        node {
                            cityId
                            cityName
                            countryId
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
            "countryByName": {
                "country": {
                    "countryId": 1,
                    "countryName": "US",
                    "cities": {
                        "edges": [
                            {
                                "node": {
                                    "cityId": 1,
                                    "cityName": "Los Angeles",
                                    "countryId": 1,
                                    "population": 3849000,
                                }
                            },
                            {
                                "node": {
                                    "cityId": 2,
                                    "cityName": "Santa Monica",
                                    "countryId": 1,
                                    "population": 91000,
                                }
                            },
                        ]
                    },
                },
                "severErrors": [],
            }
        }
    }
    return query, expected
