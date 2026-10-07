import allure

from api_requests import register_user, login_user
from user_generator import generate_user

class TestLogin:
    @allure.title('Вход под существующим пользователем')
    def test_login_existing_user_returns_success(self):
        payload = generate_user()

        register_user(payload)
        response = login_user(payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Вход с неверным логином и паролем')
    def test_login_wrong_credentials_returns_error(self):
        payload = generate_user()

        response = login_user(payload)
        assert response.status_code == 401
        assert response.json()["message"] == "email or password are incorrect"