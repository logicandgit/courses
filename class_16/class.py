# -*- coding: utf-8 -*-
import json
import requests

tut = requests.get('http://tut.by')
print tut
print tut.ok

pet = requests.get('http://petstore.swagger.io/v2/pet/2')
print pet.ok
print pet.json()
print pet.headers

pet_post_data = {
    "id": 42,
    "category": {"id": 1, "name": "catting"},
    "name": "My Dog 1",
    "photoUrls": ["string"],
    "tags": [{"id": 1, "name": "tag string"}],
    "status": "available"
}

pet_post_headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
baseUrl = 'http://petstore.swagger.io/v2'
method = '/pet'
body = json.dumps(pet_post_data)

pet_post = requests.post(baseUrl + method, headers=pet_post_headers,
                         data=body)
print pet_post.status_code
print pet_post.json()
print requests.get(baseUrl + method + '/' + str(pet_post_data['id'])).json()

assert pet_post.json()['name'] == 'My Dog 1'

def test_create_pet():
    data = {}
    header = {}
    baseUrl = ''
    method = ''
    response = requests.post(baseUrl + method, header=header, data=data)
    assert response.json()['name'] == 'My Dog 1'


