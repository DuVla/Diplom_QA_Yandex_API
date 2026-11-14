import allure


from user_generator import generate_user
from api_requests import register_user, delete_user

class TestRegister:

    @allure.title('Создание уникального пользователя')
    def test_register_unique_user_returns_success(self):
        payload = generate_user()
        response = register_user(payload)
        data = response.json()
        access_token = data.get('accessToken')

        try:
            assert response.status_code == 200
            assert data['success'] is True
        finally:
            if access_token:
                delete_response = delete_user(access_token)
                assert delete_response.status_code == 202
    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_register_existing_user_returns_error(self, registered_user):
        response = register_user(registered_user['payload'])

        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.title('Регистрация без обязательного поля возвращает ошибку')
    def test_register_missing_field_returns_error(self):
        payload = generate_user()
        del payload["password"]

        response = register_user(payload)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"
