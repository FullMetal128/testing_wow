import pytest
import requests


URL = 'https://petstore.swagger.io/v2'


@pytest.fixture()
def create_pet():
    data = {'id': 229, 'category': {'id': 229, 'name': 'GOOOOD BOY1'}, 'name': 'GOOOOD BOY1', 'photoUrls': ['string'], 'tags': [{'id': 229, 'name': 'GOOOOD BOY1'}], 'status': 'available'}
    response = requests.post(f"{URL}/pet", json = data)
    return response.json()['id']


@pytest.fixture()
def delete_pet():
    response = requests.delete(f'{URL}/pet/229')

