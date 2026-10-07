import requests

from url import BASE_URL
from user_generator import generate_user
from ingredients import get_ingredient_ids

class TestOrder:

    def test_create_order_with_auth_returns_success(self):
        payload = generate_user()

        response = requests.post(f'{BASE_URL}/auth/register', json=payload)
        access_token = response.json()['accessToken']

        ingredient_ids = get_ingredient_ids()
        headers = {'Authorization': access_token}
        order_payload =  {'ingredients': ingredient_ids}

        order_response = requests.post(f'{BASE_URL}/orders', json=order_payload, headers=headers)

        assert order_response.status_code == 200
        assert order_response.json()['success'] is True

    def test_order_creation_without_authorization_returns_success(self):
        ingredient_ids = get_ingredient_ids()
        order_payload = {'ingredients': ingredient_ids}
        order_response = requests.post(f'{BASE_URL}/orders', json=order_payload)

        assert order_response.status_code == 200
        assert order_response.json()['success'] is True