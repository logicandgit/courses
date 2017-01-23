# -*- coding: utf-8 -*- 
import page
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class TestHerokuappCom(object):

    @pytest.fixture(scope='class')
    def browser(self, request):
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.implicitly_wait(3)
        request.cls.browser = browser
        yield browser
        browser.quit()

    @pytest.fixture()
    def open_page(self, request, browser):
        browser.get('http://the-internet.herokuapp.com/')

    def test_dropdown(self, open_page):
        """
        Tests dropdown.
        This test verifies that the Dropdown page is opened.
        """

        # Load the main page.
        # In this case the home page of the-internet.herokuapp.com
        main_page = page.MainPage(self.browser)

        # Checks if the word "The Internet" is in title
        assert main_page.is_title_matches(), \
            "the-internet.herokuapp.com title doesn't match."

        # open 'Dropdown List' page
        main_page.click_by_link_dropdown()
        wait = WebDriverWait(self.browser, 15)
        wait.until(lambda _: not main_page.is_main_page())
        # Verifies that page is correct
        dropdwon_page = page.DropdownPage(self.browser)
        assert dropdwon_page.is_dropdow_page(), "It's not Dropdown page."

    def test_select_1(self, open_page):
        """
        Tests select Option 1.
        This test verifies that the User can select Option 1.
        """
        # Load the main page.
        # In this case the home page of the-internet.herokuapp.com
        main_page = page.MainPage(self.browser)

        # Checks if the word "The Internet" is in title
        assert main_page.is_title_matches(), \
            "the-internet.herokuapp.com title doesn't match."

        # open page 'Dropdown List'
        main_page.click_by_link_dropdown()
        wait = WebDriverWait(self.browser, 15)
        wait.until(lambda _: not main_page.is_main_page())
        # Verifies that page is correct
        dropdown_page = page.DropdownPage(self.browser)
        assert dropdown_page.is_dropdow_page(), "It's not Dropdown page."
        # Select 1 options
        dropdown_page.choose_option1()
        assert dropdown_page.is_option_active('Option 1'), \
            'Option 1 is not select'

    def test_select_2(self, open_page):
        """
        Tests select Option 2.
        This test verifies that the User can select Option 2.
        """

        # Load the main page.
        # In this case the home page of the-internet.herokuapp.com
        main_page = page.MainPage(self.browser)

        # Checks if the word "The Internet" is in title
        assert main_page.is_title_matches(), \
            "the-internet.herokuapp.com title doesn't match."

        # open page 'Dropdown List'
        main_page.click_by_link_dropdown()
        wait = WebDriverWait(self.browser, 15)
        wait.until(lambda _: not main_page.is_main_page())
        # Verifies that page is correct
        dropdown_page = page.DropdownPage(self.browser)
        assert dropdown_page.is_dropdow_page(), "It's not Dropdown page."
        # Select 2 options
        dropdown_page.choose_option2()
        assert not dropdown_page.is_option_active('Option 1'), 'Option 1 is select'
        assert dropdown_page.is_option_active('Option 2'), \
            'Option 2 is not select'
