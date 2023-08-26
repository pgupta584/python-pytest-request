import requests


class TestGetAPI:

    # Generic Request we can make Any HTTP method Api calls
    @staticmethod
    def test_get_api_read():
        response = requests.get("https://reqres.in/api/users?page=2")
        print("Response --> ", response.json())
        # Reading JSON Object - use Json formatter to read manually & understand
        # Read Total Page & Email
        total_page = response.json()['total_pages']
        print("total_page --> ", total_page)
        email = response.json()['data'][0]['email']
        print("email -- > ", email)


