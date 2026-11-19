import pytest

from api_requests import register_user, delete_user
from user_generator import generate_user


@pytest.fixture
def registered_user():
    payload = generate_user()
    response = register_user(payload)
    response.raise_for_status()
    access_token = response.json()['accessToken']

    yield {
        'payload': payload,
        'access_token': access_token,
        'response': response,
    }

    delete_user(access_token).raise_for_status()
