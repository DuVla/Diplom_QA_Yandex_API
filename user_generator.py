import uuid


def generate_user():
    email = f"{uuid.uuid4()}@yandex.ru"
    password = f"{uuid.uuid4()}"
    name = f"{uuid.uuid4()}"

    return {
        "email": email,
        "password": password,
        "name": name
    }
