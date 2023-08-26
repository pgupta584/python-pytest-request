import requests


class TestGetAPI:

    # Based on Method we can make calls
    @staticmethod
    def test_delete_api_one():
        response = requests.delete("https://reqres.in/api/users/2")
        # ("https://reqres.in/api/users/2", request_json, header) -- Header not required
        print(response)  # In response No json hence not putting .json
