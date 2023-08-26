import requests


class TestGetAPI:

    # Generic Request we can make Any HTTP method Api calls
    @staticmethod
    def test_get_api_two():
        response = requests.request("GET",
                                    "https://reqres.in/api/users?page=2",
                                    headers=None,
                                    params=None)
        print(response.json())

    @staticmethod
    def test_post_api_one():
        request_json = {
            "name": "morpheus",
            "job": "leader"
        }
        header = {"content-type": "application/json"}
        # response = requests.post("https://reqres.in/api/users", request_json, header)
        response = requests.request("POST",
                                    "https://reqres.in/api/users",
                                    headers=header,
                                    params=None,
                                    json=request_json)
        print(response.json())

    @staticmethod
    def test_put_api_one():
        request_json = {
            "name": "morpheus",
            "job": "zion resident"
        }
        # header = {"content-type": "application/json"}
        # response = requests.put("https://reqres.in/api/users/2", request_json)
        # ("https://reqres.in/api/users/2", request_json, header) -- Header not required
        response = requests.request("PUT",
                                    "https://reqres.in/api/users/2",
                                    headers=None,
                                    params=None,
                                    json=request_json)
        print(response.json())

    @staticmethod
    def test_patch_api_one():
        request_json = {
            "name": "morpheus",
            "job": "zion resident"
        }
        header = {"content-type": "application/json"}
        # response = requests.patch("https://reqres.in/api/users/2", request_json)
        # ("https://reqres.in/api/users/2", request_json, header) -- Header not required
        response = requests.request("PUT",
                                    "https://reqres.in/api/users/2",
                                    headers=header,
                                    params=None,
                                    json=request_json)
        print(response.json())
