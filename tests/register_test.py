import requests

from url import BASE_URL
from user_generator import generate_user

class TestRegister:

    def test_register_unique_user_returns_success(self):
        payload = generate_user()

        response = requests.post(f'{BASE_URL}/auth/register', data=payload)
        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_register_existing_user_returns_error(self):
        payload = generate_user()

        requests.post(f'{BASE_URL}/auth/register', data=payload)
        response = requests.post(f'{BASE_URL}/auth/register', data=payload)

        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    def test_register_missing_field_returns_error(self):
        payload = generate_user()
        del payload["password"]

        response = requests.post(f'{BASE_URL}/auth/register', data=payload)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"
