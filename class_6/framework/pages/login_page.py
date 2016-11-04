# -*- coding: utf-8 -*-
from class_6.framework.locators.locator import PASSWORD_FIELD, SUBMIT_BUTTON, USER_NAME_FIELD


def login(user):
    username, password = user.items()[0]
    print('In {user_field} input send value {user_name}'.format(user_field=USER_NAME_FIELD, user_name=username))
    print('In {pass_field} input send value {password}'.format(pass_field=PASSWORD_FIELD, password=password))
    print('Click {submit} button'.format(submit=SUBMIT_BUTTON))

