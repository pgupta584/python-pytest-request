import requests
import random

class TestUserCreation:
    @staticmethod
    def test_get_basic_api_2():
        header = {"Authorization": "Bearer 37838a5836d84104e99491b431ead98ea4a725b7efbf4129d2614e9bab3663c8",
                  "Content-Type": "application/json"}
        request_body = {
            "name": "Pankaj G",
            "gender": "male",
            "email": f"pankajte1130960@1555ce.com",
            "status": "active"
        }
        req = requests.request(method='POST',
                               url='https://gorest.co.in/public/v2/users',
                               json=request_body,
                               headers=header
                               )
        print(req.json())
        assert req.status_code == 201, "API Call is Failed"
        assert req.json() is not None, "API Call is Failed"
        print("API Status Code is Passed")
        user_id = req.json()['id']

        user_res = requests.request(method='GET',
                                    url='https://gorest.co.in/public/v2/users',
                                    headers=header
                                    )
        print(user_res.json())
        # assert user_id in user_res.json(), "User ID not available"
        print("Test Success")
        # Iterate all the User Object
        list_user = user_res.json()
        for user in list_user:
            if user['id'] == user_id:
                print("Test Data is available")
                break
        print("E2E API Test Success")





TestUserCreation.test_get_basic_api_2()
