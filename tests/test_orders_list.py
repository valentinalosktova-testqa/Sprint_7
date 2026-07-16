import requests
import allure
from data.urls import Urls


@allure.suite('Список заказов')
class TestOrdersList:

    @allure.title('Тело ответа содержит список заказов')
    def test_orders_list_returns_list(self):
        response = requests.get(Urls.BASE_URL + Urls.ORDERS_LIST)
        
        # Проверяем, что запрос успешный
        assert response.status_code == 200
        # Проверяем, что в ответе есть поле 'orders'
        assert 'orders' in response.json()
        # Проверяем, что 'orders' — это список
        assert isinstance(response.json()['orders'], list)