from main import *
import conftest
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
    assert response.json()['pet']['name'] == data['name']

def test_get_pet(data):
    None


