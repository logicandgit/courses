# -*- coding: utf-8 -*-
import json
import requests


class Test(object):

    def test_create_user(self):
        data = {
            "id": 1,
            "username": "UserName",
            "firstName": "FirstName",
            "lastName": "LastName",
            "email": "email@email.email",
            "password": "password",
            "phone": 1234567,
            "userStatus": 0
        }
        header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        baseUrl = 'http://petstore.swagger.io/v2/user'
        method = ''
        response = requests.post(baseUrl + method, headers=header, data=json.dumps(data))

        assert response.status_code == 200
        # assert response.json() == 'no content'

    def test_login_user(self):
        header = {
            'Accept': 'application/json'
        }
        username = 'UserName'
        password = 'Password'
        baseUrl = 'http://petstore.swagger.io/v2/user/login?username={}&password={}'.format(username, password)
        response = requests.get(baseUrl, headers=header)
        print response.status_code
        assert response.status_code == 200

    def test_logout_user(self):
        header = {
            'Accept': 'application/json'
        }
        baseUrl = 'http://petstore.swagger.io/v2/user/logout'
        response = requests.get(baseUrl, headers=header)
        print response.status_code
        assert response.status_code == 200

    def test_delete_user(self):
        header = {
            'Accept': 'application/json'
        }
        username = 'UserName'
        baseUrl = 'http://petstore.swagger.io/v2/user/{}'.format(username)
        response = requests.delete(baseUrl, headers=header)
        print response.status_code
        assert response.status_code == 200

    def test_get_user(self):
        header = {
            'Accept': 'application/json'
        }
        username = 'UserName'
        baseUrl = 'http://petstore.swagger.io/v2/user/{}'.format(username)
        response = requests.get(baseUrl, headers=header)
        print response.status_code
        assert response.status_code == 200
        # assert response.json() == user

    def test_update_user(self):
        data = {
            "id": 1,
            "username": "newUserName",
            "firstName": "newFirstName",
            "lastName": "newLastName",
            "email": "new.email@email.email",
            "password": "password",
            "phone": 7654321,
            "userStatus": 1
        }
        header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        username = 'UserName'
        baseUrl = 'http://petstore.swagger.io/v2/user/{}'.format(username)
        method = ''
        response = requests.put(baseUrl + method, headers=header,
                                 data=json.dumps(data))

        assert response.status_code == 200

if __name__ == '__main__':
    tests = Test()
    tests.test_create_user()
    tests.test_login_user()
    tests.test_logout_user()
    tests.test_get_user()
    tests.test_update_user()
    tests.test_delete_user()
