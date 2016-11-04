# -*- coding: utf-8 -*-
from class_6.framework.assertions.custom_assert import assert_on_home_page, assert_on_login_page
from class_6.framework.dto.user import NAME, PASSWORD
from class_6.framework.helpers.navigator import get
from class_6.framework.pages import home_page
from class_6.framework.pages import login_page


def test_login():
    user = {NAME: PASSWORD}
    get(login_page)
    assert_on_login_page()
    login_page.login(user)
    assert_on_home_page()
    home_page.logout()
    assert_on_login_page()

if __name__ == '__main__':
    test_login()
