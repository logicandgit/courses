# -*- coding: utf-8 -*-
import json
import pytest
import random
import requests
import string

default_header = {
    'Accept': 'application/json'
}
default_url = 'http://petstore.swagger.io/v2/user'


def generate_string(size=10, symbols=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(symbols) for _ in range(size))


def generate_number(count_numbers=5):
    return random.randrange(1, 10 ** count_numbers)


def generate_email(domain='domain.email'):
    return '{}@{}'.format(generate_string(), domain)


def verify_empty_response(response):
    assert response.status_code == 200
    assert response.content == ''


def verify_login_response(response):
    assert response.status_code == 200
    assert 'logged in user session:' in response.content


def verify_get_user(response, user):
    assert response.status_code == 200
    assert response.json() == user


def verify_update_user(response, user):
    assert response.status_code == 200
    url = '{}/{}'.format(default_url, user['username'])
    assert requests.get(url, headers=default_header).json() == user


class TestSwagger(object):
    
    def delete_user(self, user_name):
        url = '{}/{}'.format(default_url, user_name)
        requests.delete(url, headers=default_header)

    def logout_user(self):
        url = '{}/logout'.format(default_url)
        requests.get(url, headers=default_header)

    @pytest.fixture()
    def user_data(self):
        return {
            "id": generate_number(2),
            "username": generate_string(),
            "firstName": generate_string(),
            "lastName": generate_string(),
            "email": generate_email(),
            "password": generate_string(),
            "phone": str(generate_number(7)),
            "userStatus": 0
        }

    @pytest.fixture()
    def user(self, request, user_data):
        header = {
            'Content-Type': 'application/json'
        }
        header.update(default_header)

        response = requests.post(default_url,
                                 headers=header,
                                 data=json.dumps(user_data))

        assert response.ok
        request.addfinalizer(lambda: self.delete_user(user_data['username']))
        return user_data

    @pytest.fixture()
    def login_user(self, request, user):
        url = '{}/login'.format(
            default_url, auth=(user['username'], user['password']))
        requests.get(url, headers=default_header)
        request.addfinalizer(lambda: self.logout_user())

    def test_create_user(self, user_data):
        header = {
            'Content-Type': 'application/json'
        }
        header.update(default_header)

        response = requests.post(default_url,
                                 headers=header,
                                 data=json.dumps(user_data))

        verify_empty_response(response)

    def test_login_user(self, user):
        url = '{}/login'.format(default_url,
                                auth=(user['username'], user['password']))
        response = requests.get(url, headers=default_header)

        verify_login_response(response)

    def test_logout_user(self, login_user):
        url = '{}/logout'.format(default_url)
        response = requests.get(url, headers=default_header)
        verify_empty_response(response)

    def test_delete_user(self, user):
        url = '{}/{}'.format(default_url, user['username'])
        response = requests.delete(url, headers=default_header)
        verify_empty_response(response)

    def test_get_user(self, user):
        url = '{}/{}'.format(default_url, user['username'])
        response = requests.get(url, headers=default_header)
        verify_get_user(response, user)

    def test_update_user(self, user):
        new_name = 'newName'
        new_data = {
            "id": 1,
            "username": new_name,
            "firstName": "newFirstName",
            "lastName": "newLastName",
            "email": "new.email@email.email",
            "password": "password",
            "phone": '7654321',
            "userStatus": 1
        }
        
        header = {
            'Content-Type': 'application/json'
        }
        header.update(default_header)

        url = '{}/{}'.format(default_url, user['username'])
        response = requests.put(url,
                                headers=header,
                                data=json.dumps(new_data))

        verify_update_user(response, new_data)
