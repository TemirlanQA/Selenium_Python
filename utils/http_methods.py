import allure
import requests
from utils import logger

class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
            logger.Logger.add_request(url, method="GET")
            result = requests.get(url=url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            logger.Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            logger.Logger.add_request(url, method="POST")
            result = requests.post(url=url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            logger.Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            logger.Logger.add_request(url, method="PUT")
            result = requests.put(url=url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            logger.Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            logger.Logger.add_request(url, method="DELETE")
            result = requests.delete(url=url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            logger.Logger.add_response(result)
            return result

