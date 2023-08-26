import requests


class TestGetAPI:

    # Based on Method we can make calls
    @staticmethod
    def test_post_api_one():
        request_json = {
            "name": "morpheus",
            "job": "leader"
        }
        header = {"content-type": "application/json"}
        response = requests.post("https://reqres.in/api/users", request_json, header)
        print(response.json())
