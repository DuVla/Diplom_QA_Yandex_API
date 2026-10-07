import requests

from url import BASE_URL

def get_ingredient_ids():
    response = requests.get(f'{BASE_URL}/ingredients/')
    data = response.json()['data']

    return [item['_id'] for item in data[:2]]

