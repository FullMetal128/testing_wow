import pytest

@pytest.fixture()
def data():
    data = {'id': 228, 'category': {'id': 228, 'name': 'Good boy'}, 'name': 'doggie', 'photoUrls': ['string'], 'tags': [{'id': 228, 'name': 'Good boy'}], 'status': 'available'}
    return data
