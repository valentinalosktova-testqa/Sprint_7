import requests
import allure
from data.urls import Urls
import pytest

@allure.suite('Логин курьера')
class TestLoginCourier:

    @allure.title('Курьер может авторизоваться')
    def test_login_courier_success(self, create_and_delete_courier):
        login, password, first_name, courier_id = create_and_delete_courier
        
        # Пытаемся авторизоваться
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN, data=payload)
        
        # Проверяем, что авторизация прошла успешно
        assert response.status_code == 200
        assert 'id' in response.json()
        assert response.json()['id'] == courier_id

    @allure.title('Система вернёт ошибку при неверном пароле')
    def test_login_wrong_password(self, create_and_delete_courier):
        login, password, first_name, courier_id = create_and_delete_courier
        
        # Пытаемся авторизоваться с неверным паролем
        payload = {
            "login": login,
            "password": "wrongpassword"
        }
        response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN, data=payload)
        
        # Проверяем, что вернулась ошибка 404
        assert response.status_code == 404
        assert response.json().get('message') == 'Учетная запись не найдена'

    @allure.title('Если какого-то поля нет, запрос возвращает ошибку')
    def test_login_missing_field(self):
        # Проверяем, что сервер отвечает на запрос без пароля
        payload1 = {"login": "some_login"}
        
        try:
            response1 = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN, data=payload1, timeout=5)
            # Если сервер ответил, проверяем, что это ошибка
            assert response1.status_code == 400, f"Ожидался 400, а пришёл {response1.status_code}"
            assert response1.json().get('message') == 'Недостаточно данных для входа'
        except requests.exceptions.ReadTimeout:
            # Если сервер упал в таймаут — это баг, тест падает с понятным сообщением
            pytest.fail("Баг сервера: запрос без пароля уходит в таймаут вместо ошибки 400")