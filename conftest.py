import pytest
from helpers.courier_helpers import register_new_courier_and_return_login_password, login_courier, delete_courier


@pytest.fixture
def create_and_delete_courier():
    """
    Фикстура:
    - Создаёт курьера перед тестом
    - Возвращает его логин, пароль, имя и ID
    - Удаляет курьера после теста
    """
    # Создаём курьера
    login, password, first_name = register_new_courier_and_return_login_password()
    
    # Если курьер не создался — фикстура не работает
    if login is None:
        pytest.fail("Не удалось создать курьера для фикстуры")
    
    # Логинимся, чтобы получить ID курьера
    response = login_courier(login, password)
    courier_id = response.json().get('id')
    
    # Возвращаем данные курьера
    yield login, password, first_name, courier_id
    
    # После теста удаляем курьера
    if courier_id:
        delete_courier(courier_id)