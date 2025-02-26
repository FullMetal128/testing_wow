import pytest
import requests
import const

BASE_URL = 'https://petstore.swagger.io/v2'


# отдельная фикстура для очистки
@pytest.fixture(autouse= True)
def delete_pet():
    id = const.data['id']
    yield
    response = requests.delete(f"{BASE_URL}/pet/{id}")
    assert response.status_code in [200, 404], f"Failed to delete pet: {response.text}"


@pytest.fixture(autouse= True)
def create_test_pet(delete_pet):
    response = requests.post(f"{BASE_URL}/pet", json= const.data)
    assert response.status_code in [200, 404], f"Failed to create pet: {response.text}"
    return response.status_code






