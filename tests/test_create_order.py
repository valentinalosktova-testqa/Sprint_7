import allure
import pytest
from helpers.courier_helpers import create_order


@allure.suite('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с разными вариантами цвета')
    @pytest.mark.parametrize('color', [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_colors(self, color):
        payload = {
            "firstName": "Анна",
            "lastName": "Тестова",
            "address": "Центральная 1",
            "metroStation": 4,
            "phone": "+79998887766",
            "rentTime": 3,
            "deliveryDate": "2026-07-20",
            "comment": "Тест",
            "color": color
        }

        response = create_order(payload)

        assert response.status_code == 201
        assert 'track' in response.json()
        assert response.json()['track'] is not None

    @allure.title('Тело ответа содержит track при создании заказа')
    def test_create_order_returns_track(self):
        payload = {
            "firstName": "Иван",
            "lastName": "Петров",
            "address": "Ленина 10",
            "metroStation": 2,
            "phone": "+79998887777",
            "rentTime": 5,
            "deliveryDate": "2026-07-25",
            "comment": "Тест track",
            "color": []
        }

        response = create_order(payload)

        assert response.status_code == 201
        assert 'track' in response.json()
        assert isinstance(response.json()['track'], int)