# -*- coding: UTF-8 -*-
from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from google_tests.helpers.page_loader import PageLoader

use_step_matcher('re')


@then(u'waits for page to finish loading')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        PageLoader(),
        "Page not loaded in given timeout"
    )
