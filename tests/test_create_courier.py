import allure
from data.urls import Urls
from helpers.courier_helpers import generate_random_string, create_courier


@allure.suite('Создание курьера')
class TestCreateCourier:

    @allure.title('Курьера можно создать')
    def test_create_courier_success(self, create_and_delete_courier):
        login, password, first_name, courier_id = create_and_delete_courier
    
    # Проверяем, что курьер создался
        assert login is not None
        assert password is not None
        assert first_name is not None
    # Проверяем, что courier_id — это число (код ответа был 201)
        assert isinstance(courier_id, int) and courier_id > 0
    

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self, create_and_delete_courier):
        # Создаём первого курьера через фикстуру
        login, password, first_name, courier_id = create_and_delete_courier

        # Пытаемся создать второго с теми же данными
        response = create_courier(login, password, first_name)

        # Проверяем, что вернулась ошибка 409 (Conflict)
        assert response.status_code == 409
        # Проверяем текст ошибки
        assert response.json().get('message') == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Нельзя создать курьера без обязательного поля')
    def test_create_courier_missing_field(self):
        # Генерируем случайный пароль и имя, но не передаём логин
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # Создаём курьера без логина (используем create_courier)
        response = create_courier(None, password, first_name)

        # Проверяем, что вернулась ошибка 400 (Bad Request)
        assert response.status_code == 400
        # Проверяем текст ошибки
        assert response.json().get('message') == 'Недостаточно данных для создания учетной записи'

    @allure.title('Успешный запрос возвращает {{"ok": true}}')
    def test_create_courier_returns_ok_true(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        response = create_courier(login, password, first_name)

        assert response.status_code == 201
        assert response.json() == {"ok": True}