import const
import requests

BASE_URL = 'https://petstore.swagger.io/v2'

def test_add_pet(add_pet):
    pet_id = add_pet["id"]
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200
    assert response.json()["id"] == pet_id


def test_update_pet_status(add_pet):
    pet_id = add_pet["id"]
    updated_data = add_pet.copy()
    updated_data["status"] = "sold"
    response = requests.put(f"{BASE_URL}/pet", json=updated_data)
    assert response.status_code == 200

    get_response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert get_response.status_code == 200
    assert get_response.json()["status"] == "sold"


def test_delete_pet(add_pet, delete_pet):
    pet_id = add_pet["id"]
    delete_pet(pet_id)
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 404
















