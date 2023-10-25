import requests


class TestBasicAPI:
    # Get API Example
    # @staticmethod
    # def test_get_basic_api():
    #     req = requests.request('GET', 'https://httpbin.org/get')
    #     print(req.json())

    @staticmethod
    def test_get_basic_api():
        req = requests.get('https://httpbin.org/get')
        print(req.json())


TestBasicAPI.test_get_basic_api()
