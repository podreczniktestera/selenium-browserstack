# -*- coding: UTF-8 -*-
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from google_tests.helpers.page_loader import require_loaded
from google_tests.locators.home_page import HomePageLocators
from google_tests.page_model.base_page import BasePage


class HomePage(BasePage):  
    @property
    def url(self):
        return 'https://google.com/'

    @property
    def search_bar(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.SEARCH_BAR),
            "Search bar is not visible"
        )

    @property
    def search_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.SEARCH_BUTTON),
            "Search button is not visible"
        )

    @property
    def feeling_lucky_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomePageLocators.FEELING_LUCKY_BUTTON),
            "I'm feeling lucky button is not visible"
        )

    @property
    def is_loaded(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(HomePageLocators.GOOGLE_LOGO)
            )
            return True
        except TimeoutException:
            return False

    def load(self):
        self.driver.get(self.url)

    @require_loaded
    def type_in_search_bar(self, text):
        element = self.search_bar
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ESCAPE)

    @require_loaded
    def click_search_button(self):
        self.search_button.click()

    @require_loaded
    def click_feeling_lucky_button(self):
        self.feeling_lucky_button.click()

    def search_for(self, text):
        self.type_in_search_bar(text)
        self.click_search_button()
