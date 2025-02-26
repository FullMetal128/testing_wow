import requests
import json
import logging



def get_pet(id):
    url = f"https://petstore.swagger.io/v2/pet/{id}"
    r = requests.get(url)
    return r.json()

def delete_pet(id):
    url = f"https://petstore.swagger.io/v2/pet/{id}"
    r = requests.delete(url)
    return r.status_code

logging.basicConfig(level=logging.DEBUG)
#delete_pet(666)
logging.info(get_pet(666))