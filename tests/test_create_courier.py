import requests
import allure
from data.urls import Urls
from helpers.courier_helpers import register_new_courier_and_return_login_password, generate_random_string


@allure.suite('Создание курьера')
class TestCreateCourier:

    @allure.title('Курьера можно создать')
    def test_create_courier_success(self):
        login, password, first_name = register_new_courier_and_return_login_password()
        
        assert login is not None
        assert password is not None
        assert first_name is not None

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self):
        # Создаём первого курьера
        login, password, first_name = register_new_courier_and_return_login_password()
        
        # Пытаемся создать второго с теми же данными
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE, data=payload)
        
        # Проверяем, что вернулась ошибка 409 (Conflict)
        assert response.status_code == 409
        # Проверяем текст ошибки
        assert response.json().get('message') == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Нельзя создать курьера без обязательного поля')
    def test_create_courier_missing_field(self):
        # Генерируем случайный пароль, но не передаём логин
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        
        payload = {
            "password": password,
            "firstName": first_name
        }
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE, data=payload)
        
        # Проверяем, что вернулась ошибка 400 (Bad Request)
        assert response.status_code == 400
        # Проверяем текст ошибки
        assert response.json().get('message') == 'Недостаточно данных для создания учетной записи'

    @allure.title('Успешный запрос возвращает {{"ok": true}}')
    def test_create_courier_returns_ok_true(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE, data=payload)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}