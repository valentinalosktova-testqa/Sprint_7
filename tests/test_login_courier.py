import allure
import pytest
from helpers.courier_helpers import login_courier
from data.urls import Urls
import requests


@allure.suite('Логин курьера')
class TestLoginCourier:

    @allure.title('Курьер может авторизоваться')
    def test_login_courier_success(self, create_and_delete_courier):
        login, password, first_name, courier_id = create_and_delete_courier

        response = login_courier(login, password)

        assert response.status_code == 200
        assert 'id' in response.json()
        assert response.json()['id'] == courier_id

    @allure.title('Система вернёт ошибку при неверном пароле')
    def test_login_wrong_password(self, create_and_delete_courier):
        login, password, first_name, courier_id = create_and_delete_courier

        response = login_courier(login, "wrongpassword")

        assert response.status_code == 404
        assert response.json().get('message') == 'Учетная запись не найдена'

    @allure.title('Если какого-то поля нет, запрос возвращает ошибку')
    def test_login_missing_field(self):
        # Отправляем запрос без пароля (не через login_courier, так как там нужен пароль)
        payload = {"login": "some_login"}
        response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN, data=payload)

        assert response.status_code == 400
        assert response.json().get('message') == 'Недостаточно данных для входа'