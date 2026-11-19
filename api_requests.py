import allure
import requests

from url import BASE_URL, TIMEOUT

@allure.step('Отправить запрос на регистрацию пользователя')
def register_user(payload):
    return requests.post(f'{BASE_URL}/auth/register', data=payload, timeout=TIMEOUT)

@allure.step('Отправить запрос на логин пользователя')
def login_user(payload):
    return requests.post(f'{BASE_URL}/auth/login', data=payload, timeout=TIMEOUT)

@allure.step('Отправить запрос на создание заказа')
def create_order(order_payload, headers = None):
    return requests.post(f'{BASE_URL}/orders', json=order_payload, headers=headers, timeout=TIMEOUT)

@allure.step('Удалить тестового пользователя')
def delete_user(access_token):
    return requests.delete(f'{BASE_URL}/auth/user', headers={'Authorization': access_token}, timeout=TIMEOUT)