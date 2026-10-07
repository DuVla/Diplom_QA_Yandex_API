import allure

from api_requests import login_user, create_order, register_user
from user_generator import generate_user
from ingredients import get_ingredient_ids

class TestOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_auth_returns_success(self):
        payload = generate_user()

        response = register_user(payload)
        access_token = response.json()['accessToken']

        ingredient_ids = get_ingredient_ids()
        headers = {'Authorization': access_token}
        order_payload =  {'ingredients': ingredient_ids}

        order_response = create_order(order_payload, headers)

        assert order_response.status_code == 200
        assert order_response.json()['success'] is True

    @allure.title('Создание заказа без авторизации')
    def test_order_creation_without_authorization_returns_success(self):
        ingredient_ids = get_ingredient_ids()
        order_payload = {'ingredients': ingredient_ids}
        order_response = create_order(order_payload)

        assert order_response.status_code == 200
        assert order_response.json()['success'] is True

    @allure.title('Создание заказа без ингредиентов возвращает ошибку')
    def test_create_order_without_ingredients_returns_error(self):
        order_payload = {'ingredients': []}

        order_response = create_order(order_payload)

        assert order_response.status_code == 400
        assert order_response.json()['message'] == 'Ingredient ids must be provided'

    @allure.title('Создание заказа с некорректным хешем ингредиента ')
    def test_create_order_with_invalid_ingredients_hash_return_error(self):
        order_payload = {'ingredients': ['invalid_hash_123']}
        order_response = create_order(order_payload)

        assert order_response.status_code == 500

    @allure.title('Создание заказа с ингредиентами')
    def test_create_order_with_ingredients_returns_success(self):
        ingredient_ids = get_ingredient_ids()
        order_payload = {'ingredients': ingredient_ids}

        order_response = create_order(order_payload)

        assert order_response.status_code == 200
        assert order_response.json()['success'] is True