from main import *
import conftest

def test_connect():

    assert get_info() == 'Success'

def test_add_pet():
    assert add_pet('Good boy') == 200

def test_get_pet(data):
    rezult = data
    assert get_pet(228) == rezult




