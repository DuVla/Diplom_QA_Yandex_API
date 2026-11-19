import requests

from url import BASE_URL, TIMEOUT

def get_ingredient_ids():
    response = requests.get(
        f'{BASE_URL}/ingredients/',
        timeout=TIMEOUT
    )
    response.raise_for_status()
    data = response.json()['data']

    return [item['_id'] for item in data[:2]]
