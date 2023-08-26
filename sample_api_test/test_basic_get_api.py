import requests


class TestGetAPI:
    @staticmethod
    def test_get_api_one():
        response = requests.request("GET",
                                    "https://reqres.in/api/users?page=2",
                                    headers=None,
                                    params=None)
        print(response.json())
