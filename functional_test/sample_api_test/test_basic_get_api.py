import requests


class TestGetAPI:

    # Based on Method we can make calls
    @staticmethod
    def test_get_api_one():
        response = requests.get("https://reqres.in/api/users?page=2")
        print(response.json())
