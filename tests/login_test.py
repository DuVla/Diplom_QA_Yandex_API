import requests

from url import BASE_URL
from user_generator import generate_user

class TestLogin:
    def test_login_existing_user_returns_success(self):
        payload = generate_user()

        requests.post(f"{BASE_URL}/auth/register", data=payload)
        response = requests.post(f"{BASE_URL}/auth/login", data=payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_login_wrong_credentials_returns_error(self):
        payload = generate_user()

        response = requests.post(f"{BASE_URL}/auth/login", data=payload)
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"