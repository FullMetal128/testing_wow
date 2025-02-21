from main import *

URL = 'https://petstore.swagger.io/v2'

def test_connect():
    assert get_info() == 'Success'

def test_add_pet():
    assert add_pet('Good boy') == 200

def test_get_pet(data):
    rezult = data
    assert get_pet(228) == rezult


def test_add_pet(data):
    response = requests.post(f"{URL}/pet", json = data)
    assert response.status_code == 200
    assert response.json()['name'] == data['name']

def test_get_pet(data):
    pet_id = data['id']
    response = requests.get(f"{URL}/pet/{pet_id}")
    assert response.status_code == 200
    assert response.json()['id'] == pet_id

def test_update_pet(data):
    data['name'] = 'GALAXY_____DESTROYER_____3000'
    data['category']['name'] = 'GALAXY_____DESTROYER_____3000'
    response = requests.put(f'{URL}/pet', json = data)
    assert response.status_code == 200
    assert response.json()['name'] == data['name']
    assert response.json()['category']['name'] == data['category']['name']


'''
def test_delete_pet(data):
    pet_id = data['id']
    response = requests.delete(f'{URL}/pet/{pet_id}')
    assert response.status_code == 200
    response = requests.get(f'{URL}/pet/{pet_id}')
    assert response.status_code == 404
'''

