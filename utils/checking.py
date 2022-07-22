"""Методы для проверки ответов наших запросов"""
import json

from requests import Response


class Checking():
    """Метод статус код"""

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f"Успешно! Статус код = " + str(response.status_code))
        else:
            print("Провал! статус код = " + str(response.status_code))

    """Метод теста наличия обязательных поля"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    """Метод проверки значений обязательных полей"""

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " " + expected_value + " верен")

    """Метод проверки значений обязательных полей"""

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Слово " + search_word + " присутствует")
        else:
            print("Слово " + search_word + " отсутствует")

    def test_collapse(self: Response, login_token: str, password: str):
        token = login_token
