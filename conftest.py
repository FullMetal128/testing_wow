import pytest
import requests


URL = 'https://petstore.swagger.io/v2'


@pytest.fixture()
def create_pet():
    data = {'id': 229, 'category': {'id': 229, 'name': 'GOOOOD BOY1'}, 'name': 'GOOOOD BOY1', 'photoUrls': ['string'], 'tags': [{'id': 229, 'name': 'GOOOOD BOY1'}], 'status': 'available'}
    response = requests.post(f"{URL}/pet", json = data)

    yield response.json()['id'] #это оказывается было нужно!

    delete_response = requests.delete(f'{URL}/pet/{229}')
    assert delete_response.status_code == 200, f'Failed to delete user : {delete_response.text}'

#это не нужно!
@pytest.fixture()
def delete_pet():
    response = requests.delete(f'{URL}/pet/{229}')
    return response.status_code
