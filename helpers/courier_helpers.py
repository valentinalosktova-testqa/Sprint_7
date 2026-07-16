import requests
import random
import string
from data.urls import Urls


def generate_random_string(length):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def register_new_courier_and_return_login_password():
    """
    Регистрирует нового курьера с случайными логином, паролем и именем.
    Возвращает кортеж (login, password, first_name).
    Если регистрация не удалась, возвращает (None, None, None).
    """
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Urls.BASE_URL + Urls.COURIER_CREATE, data=payload)

    if response.status_code == 201:
        return login, password, first_name
    return None, None, None


def login_courier(login, password):
    """Авторизует курьера и возвращает ответ"""
    payload = {
        "login": login,
        "password": password
    }
    response = requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN, data=payload)
    return response


def delete_courier(courier_id):
    """Удаляет курьера по ID"""
    response = requests.delete(Urls.BASE_URL + Urls.COURIER_DELETE + str(courier_id))
    return response