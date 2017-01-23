# -*- coding: utf-8 -*- 
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    """A class for main page locators.
    All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    DROPDOWN_LINK = (By.LINK_TEXT, 'Dropdown')


class SearchResultsPageLocators(object):
    """A class for search results locators.
    All search results locators should come here"""
    pass


class DropdownPageLocators(object):
    OPTIONS = (By.ID, 'dropdown')
    OPTION1 = (By.CSS_SELECTOR, 'option[value="1"]')
    OPTION2 = (By.CSS_SELECTOR, 'option[value="2"]')
