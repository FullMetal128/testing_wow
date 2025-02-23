import pytest
import requests
import const

BASE_URL = 'https://petstore.swagger.io/v2'

@pytest.fixture
def pet_data():
    return const.data

@pytest.fixture
def add_pet(pet_data):
    response = requests.post(f"{BASE_URL}/pet", json=pet_data)
    assert response.status_code == 200, f"Failed to add pet: {response.text}"
    yield pet_data

    # зачистка
    pet_id = pet_data["id"]
    delete_response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert delete_response.status_code in [200, 404], f"Failed to delete pet: {delete_response.text}"

# отдельная фикстура для очистки
@pytest.fixture
def delete_pet():
    def _delete_pet(pet_id): # вроде, так можно
        response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
        assert response.status_code in [200, 404], f"Failed to delete pet: {response.text}"

    return _delete_pet



