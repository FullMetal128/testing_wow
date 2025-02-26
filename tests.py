import const
import requests

BASE_URL = 'https://petstore.swagger.io/v2'

def test_add_pet(delete_pet):
    response = requests.post(f"{BASE_URL}/pet", json= const.data)
    assert response.status_code == 200, response.text
    get_response = requests.get(f"{BASE_URL}/pet/{const.data['id']}")
    assert get_response.status_code == 200, get_response.text
    assert get_response.json()['id'] == const.data['id'], get_response.text


def test_update_pet(create_test_pet, delete_pet):

    updated_data = const.data.copy()
    updated_data["name"] = "NEWNAME"
    response = requests.put(f"{BASE_URL}/pet", json= updated_data)
    assert response.status_code == 200
    assert response.json()['name'] != 'GALAXY_DESTROYER666'
    assert response.json()['name'] == updated_data['name']



















