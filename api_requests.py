import allure
import requests

from url import BASE_URL


@allure.step('Отправить запрос на регистрацию пользователя')
def register_user(payload):
    return requests.post(f'{BASE_URL}/auth/register', data=payload)

@allure.step('Отправить запрос на логин пользователя')
def login_user(payload):
    return requests.post(f'{BASE_URL}/auth/login', data=payload)

@allure.step('Отправить запрос на создание заказа')
def create_order(order_payload, headers = None):
    return requests.post(f'{BASE_URL}/orders', json=order_payload, headers=headers)