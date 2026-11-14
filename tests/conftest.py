import pytest

from api_requests import register_user, delete_user
from user_generator import generate_user

@pytest.fixture
def registered_user():
    payload = generate_user()
    response = register_user(payload)
    assert response.status_code == 200

    access_token = response.json()['accessToken']

    yield {
        'payload': payload,
        'access_token': access_token
    }

    delete_response = delete_user(access_token)
    assert delete_response.status_code == 202