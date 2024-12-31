import requests
from pytest import mark

from config.api_config import ApiURLs
from requests_responses.Requests.reqres.user import User
from utils.common_utils import CommonUtils
from utils.framework_utils import FrameworkUtils
from utils.json_compare import json_compare_schema


class TestGetAPI:

    # Generic Request we can make Any HTTP method Api calls
    @mark.jsonTest
    def test_get_api_read(self):
        header = {"content-type": "application/json"}
        print("header", header)
        url = ApiURLs.get_user_info(2)
        print("url", url)
        response = FrameworkUtils.check_status_code_with_custom_header(endPoint=url,
                                             requestMethod="GET",
                                             headers=header,
                                             params=None,
                                             expectedStatusCode=requests.codes.ok,
                                             jsonPayload=None)

        print("Response --> ", response.json())
        # Verify Json Schema
        json_compare_schema(actual=response.json(),
                            expected="python-pytest-request/requests_responses/Responses/reqres/user_res.json")
        # # Reading JSON Object - use Json formatter to read manually & understand
        # # Read Total Page & Email
        # total_page = response.json()['total_pages']
        # print("total_page --> ", total_page)
        # email = response.json()['data'][0]['email']
        # print("email -- > ", email)
        # Extract Json key directly using utility
        email = CommonUtils.json_extract(response.json(), "email")
        print("email", email)

    @mark.jsonTest
    def test_post_api_read(self):
        header = {"content-type": "application/json"}
        print("header", header)
        url = ApiURLs.CREATE_USER
        print("url", url)
        request_payload = User.CREATE_USER
        request_payload['name'] = "Pankaj G"
        print("request_payload", request_payload)
        response = FrameworkUtils.check_status_code_with_custom_header(endPoint=url,
                                                                       requestMethod="GET",
                                                                       headers=header,
                                                                       params=None,
                                                                       expectedStatusCode=requests.codes.ok,
                                                                       jsonPayload=request_payload)

        print("Response --> ", response.json())
        # Verify Json Schema
        json_compare_schema(actual=response.json(),
                            expected="python-pytest-request/requests_responses/Responses/reqres/user_res.json")
        # # Reading JSON Object - use Json formatter to read manually & understand
        # # Read Total Page & Email
        # total_page = response.json()['total_pages']
        # print("total_page --> ", total_page)
        # email = response.json()['data'][0]['email']
        # print("email -- > ", email)
        # Extract Json key directly using utility
        email = CommonUtils.json_extract(response.json(), "email")
        print("email", email)
