# -*- coding: utf-8 -*-
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver1 = webdriver.Chrome()
#
# # driver1.get('http://tut.by')
#
# # driver1.refresh()
# # driver1.back()
# # driver1.forward()
# driver1.get('http://the-internet.herokuapp.com/')
# links = driver1.find_elements_by_css_selector('a')
# # print(len(links))
# # print [link.text for link in links]
# target_link = filter(lambda x: 'Form Authentication' in x.text, links)
# # print(len(target_link))
# target_link[0].click()
# assert 'login' in driver1.current_url
#
# time.sleep(5)
# driver1.close()


class TestHerokuapp(object):

    @pytest.fixture(scope='class')
    def browser(self, request):
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.implicitly_wait(3)
        request.cls.browser = browser
        yield browser
        browser.quit()

    @pytest.fixture()
    def open_page(self, request, browser):
        browser.get('http://the-internet.herokuapp.com/')

    def test_login(self, open_page):
        self.browser.find_element_by_link_text('Form Authentication').click()
        username = self.browser.find_element_by_css_selector('#username')
        password = self.browser.find_element_by_css_selector('#password')
        login_button = self.browser.find_element_by_css_selector('button[type="submit"]')

        username.send_keys('tomsmith')
        password.send_keys('SuperSecretPassword!')
        login_button.click()
        time.sleep(3)
        assert 'You logged into a secure area!' in self.browser.find_element_by_css_selector('#flash[class="flash success"]').text
        assert self.browser.find_element_by_css_selector('[href="/logout"]').is_displayed()

    def test_waite_for_visibilety(self, open_page):
        self.browser.find_element_by_link_text('Dynamic Loading').click()
        self.browser.find_element_by_partial_link_text('Example 1').click()
        finish_message = self.browser.find_element_by_id('finish')
        assert not finish_message.is_displayed()
        start_button = self.browser.find_element_by_css_selector('#start button')
        start_button.click()
        wait = WebDriverWait(self.browser, 15)
        # wait.until_not(EC.visibility_of(start_button))
        wait.until(lambda _ : not start_button.is_displayed())
        assert not start_button.is_displayed()
        wait.until(EC.visibility_of(finish_message))
        assert finish_message.is_displayed()

    def test_waite_for_example2(self, open_page):
        self.browser.find_element_by_link_text('Dynamic Loading').click()
        self.browser.find_element_by_partial_link_text('Example 2').click()

        assert not self.browser.find_elements_by_id('finish')

        start_button = self.browser.find_element_by_css_selector('#start button')
        start_button.click()
        wait = WebDriverWait(self.browser, 15)
        # wait.until_not(EC.visibility_of(start_button))
        wait.until(lambda _: not start_button.is_displayed())
        assert not start_button.is_displayed()

        wait.until(lambda _: wait.until(EC.presence_of_element_located((By.ID, 'finish'))))
        finish_message = self.browser.find_element_by_id('finish')
        # wait.until(EC.visibility_of(finish_message))
        assert finish_message.is_displayed()
