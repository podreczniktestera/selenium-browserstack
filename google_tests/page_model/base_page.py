# -*- coding: UTF-8 -*-
from google_tests.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)
