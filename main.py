import requests
import json
import logging

def get_info():
    r = requests.get('https://petstore.swagger.io/v2/swagger.json')
    if r.status_code == 200:
        return 'Success'
    else:
        return 'Fail'

def add_pet(name):
    url = "https://petstore.swagger.io/v2/pet"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "id": 228,
        "category": {
            "id": 228,
            "name": name
        },
        "name": name,
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 228,
                "name": name
            }
        ],
        "status": "available"
    }
    response = requests.post(url, json=data, headers=headers)
    return response.status_code

def get_pet(id):
    url = f"https://petstore.swagger.io/v2/pet/{id}"
    r = requests.get(url)
    return r.json()

#add_pet('GOOOOD BOY')
logging.basicConfig(level=logging.DEBUG)
logging.info(get_pet(228))