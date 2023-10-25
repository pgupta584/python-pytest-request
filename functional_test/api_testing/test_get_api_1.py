import requests


class TestBasicAPI:
    # Get API Example
    @staticmethod
    def test_get_basic_api():
        req = requests.request('GET', 'https://httpbin.org/get')
        print(req.json())

    @staticmethod
    def test_get_basic_api_2():
        req = requests.request('GET', 'https://reqres.in/api/users?page=2')
        print(req.json())
        assert req.status_code == 200, "API Call is Failed"
        print("API Status Code is Passed")
        total_pages = req.json()['total_pages']
        print("Total page is ", total_pages)
        email = req.json()['data'][0]['email']
        print("email is ", email)
        # Assert Response Object
        assert total_pages == 2, "Page size is wrong"
        assert email == "michael.lawson@reqres.in", "Email is wrong"
        print("Response assertion is Passed")

    @staticmethod
    def test_post_basic_api():
        request_json = {
            "name": "morpheus",
            "job": "leader"
        }
        header = {"Content-Type": "application/json"}
        response = requests.request(method='POST',
                                    url='https://reqres.in/api/users',
                                    json=request_json,
                                    headers=header
                                    )
        print(response.json())
        assert response.status_code == 201, "API Call Failed"
        assert response.json()['createdAt'] is not None, "response is success"

    @staticmethod
    def test_put_basic_api():
        request_json = {
            "name": "morpheus",
            "job": "leader"
        }
        header = {"Content-Type": "application/json"}
        response = requests.request(method='PUT',
                                    url='https://reqres.in/api/users/2',
                                    json=request_json,
                                    headers=header
                                    )
        print(response.json())
        assert response.status_code == 200, "API Call Failed"
        assert response.json()['updatedAt'] is not None, "response is success"
        assert response.json()['job'] == "leader", "response is success"

    @staticmethod
    def test_patch_basic_api():
        request_json = {
            "name": "Pankaj",
            "job": "leader"
        }
        header = {"Content-Type": "application/json"}
        response = requests.request(method='PATCH',
                                    url='https://reqres.in/api/users/2',
                                    json=request_json,
                                    headers=header
                                    )
        print(response.json())
        assert response.status_code == 200, "API Call Failed"
        assert response.json()['updatedAt'] is not None, "response is success"
        assert response.json()['name'] == "Pankaj", "response is success"

    @staticmethod
    def test_delete_basic_api():
        response = requests.request(method='DELETE',
                                    url='https://reqres.in/api/users/2'
                                    )
        assert response.status_code == 204, "API Call Failed"
        print("PASS")


# TestBasicAPI.test_get_basic_api()
# TestBasicAPI.test_get_basic_api_2()
# TestBasicAPI.test_post_basic_api()
# TestBasicAPI.test_put_basic_api()
# TestBasicAPI.test_patch_basic_api()
TestBasicAPI.test_delete_basic_api()


