import requests


class TestGetAPI:

    # Based on Method we can make calls
    @staticmethod
    def test_patch_api_one():
        request_json = {
            "name": "morpheus",
            "job": "zion resident"
        }
        header = {"content-type": "application/json"}
        response = requests.patch("https://reqres.in/api/users/2", request_json)
        # ("https://reqres.in/api/users/2", request_json, header) -- Header not required
        print(response.json())
