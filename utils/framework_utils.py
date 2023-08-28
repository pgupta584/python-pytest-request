import logging

import curlify
import pytest
import requests

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class FrameworkUtils:
    # Custom Method to pass verify as False
    @staticmethod
    def check_status_code_with_custom_header(endPoint=None,
                                             requestMethod="GET",
                                             headers=None,
                                             params=None,
                                             expectedStatusCode=requests.codes.ok,
                                             jsonPayload=None,
                                             verify=None):
        response = requests.request(requestMethod, endPoint, headers=headers, params=params, json=jsonPayload,
                                    verify=verify)
        # Logging cURL - Enable as per requirements
        FrameworkUtils.log_curl_req(response)  # Disabling login cURL due to security constraints

        try:
            assert response.status_code == expectedStatusCode, \
                f"Expected Status Code {expectedStatusCode} and Actual status {response.status_code} code did not match with failure reason {response.json()}"
            return response
        except:
            logger.error(response.headers)
            pytest.fail(
                f"Expected Status Code {expectedStatusCode} and Actual status {response.status_code} code did not match and response is {response.json()}")

    @staticmethod
    def log_curl_req(response):
        logger.info("----------CURLIFY START----------------")
        logger.info("                                       ")
        logger.info("***********REQUEST CURL****************")
        logger.info("                                       ")
        logger.info(curlify.to_curl(response.request))
        logger.info("                                       ")
        logger.info("***********RESPONSE MESSAGE************")
        logger.info("                                       ")
        logger.info(f"Response :{response.text}")
        logger.info("                                       ")
        logger.info("***************************************")
        logger.info("***** Response Time is:" + str(response.elapsed.total_seconds()))
        logger.info("----------CURLIFY ENDS-----------------")
        logger.info("                                       ")
        logger.info(f"status code{response.status_code}")
