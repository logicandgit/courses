# -*- coding: utf-8 -*-
from locators import MainPageLocators
from locators import DropdownPageLocators
from selenium.webdriver.support.ui import Select


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here"""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "The Internet" in self.driver.title

    def is_main_page(self):
        return "Welcome to the Internet" in self.driver.page_source

    def click_by_link_dropdown(self):
        """Trigger open new page"""
        element = self.driver.find_element(*MainPageLocators.DROPDOWN_LINK)
        # element = self.driver.find_element(By.LINK_TEXT, 'Dropdown')
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source


class DropdownPage(BasePage):

    def is_dropdow_page(self):
        return "Dropdown List" in self.driver.page_source

    def choose_option1(self):
        element = self.driver.find_element(*DropdownPageLocators.OPTION1)
        element.click()

    def choose_option2(self):
        element = self.driver.find_element(*DropdownPageLocators.OPTION2)
        element.click()

    def is_option_active(self, name_option):
        options = Select(self.driver.find_element(*DropdownPageLocators.OPTIONS))
        selected_option = options.first_selected_option
        # element = self.driver.find_element(*DropdownPageLocators.OPTION1)
        return selected_option.text == name_option
