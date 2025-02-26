import pytest
import requests
import const

BASE_URL = 'https://petstore.swagger.io/v2'


# отдельная фикстура для очистки
@pytest.fixture()
def delete_pet():
    print('No')
    yield
    response = requests.delete(f"{BASE_URL}/pet/{const.data['id']}")
    assert response.status_code in [200, 404], f"Failed to delete pet: {response.text}"


@pytest.fixture()
def create_test_pet():
    response = requests.post(f"{BASE_URL}/pet", json= const.data)
    assert response.status_code in [200, 404], f"Failed to create pet: {response.text}"
    return response.status_code






