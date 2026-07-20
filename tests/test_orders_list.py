import allure
from helpers.courier_helpers import get_orders_list


@allure.suite('Список заказов')
class TestOrdersList:

    @allure.title('Тело ответа содержит список заказов')
    def test_orders_list_returns_list(self):
        response = get_orders_list()

        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)