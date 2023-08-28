import requests

from requests_responses.Requests.reqres.user import User


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

    @staticmethod
    def test_post_api_two():
        request_json = User.CREATE_USER
        request_json['name'] = "Pankaj"
        print("request_json", request_json)
        header = {"content-type": "application/json"}
        response = requests.post("https://reqres.in/api/users", request_json, header)
        print(response.json())

