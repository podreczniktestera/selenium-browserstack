# -*- coding: UTF-8 -*-
from behave import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from google_tests.locators.home_page import HomePageLocators
from google_tests.page_model.home_page import HomePage

use_step_matcher('re')


@given(u'user is at google home page')
def step_impl(context):
    page = HomePage(context.driver)
    page.load()
    WebDriverWait(context.driver, 10).until(
        expected_conditions.presence_of_element_located(HomePageLocators.SEARCH_BAR)
    )
