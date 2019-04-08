# -*- coding: UTF-8 -*-
from behave import *
from google_tests.page_model.home_page import HomePage

use_step_matcher('re')


# "(?P<thing>.*)"
@when(u'search for "(.*)"')
def step_impl(context, thing):
    page = HomePage(context.driver)
    page.search_for(thing)


@when(u'user types "(.*)" in search bar')
def step_impl(context, text):
    page = HomePage(context.driver)
    page.type_in_search_bar(text)

    typed_text = page.search_bar.get_attribute('value')
    assert text == typed_text, "{} NOT EQUAL {}".format(text, typed_text)


@when(u'clicks on "(.*)" button')
def step_impl(context, button):
    page = HomePage(context.driver)
    if button == "I'm feeling lucky":
        page.click_feeling_lucky_button()
    elif button == "Search":
        page.click_search_button()
    else:
        raise Exception('No such button')
