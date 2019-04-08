# -*- coding: UTF-8 -*-
from behave import *
from google_tests.page_model.home_page import HomePage
from google_tests.page_model.search_results_page import SearchResultsPage

use_step_matcher('re')


@then(u'results page shows up')
def step_impl(context):
    page = SearchResultsPage(context.driver)
    assert page.is_loaded


# "(?P<thing>.*)" (?:is|are)
@then(u'results* for "(.*)" (is|are) displayed')
def step_impl(context, thing, form):
    page_hp = HomePage(context.driver)
    page_srp = SearchResultsPage(context.driver)

    assert context.driver.title, "Page title is empty"

    if form == "are":
        assert "google" in context.driver.title.lower(), \
            "google is not in page title: {}".format(context.driver.title.lower())
        assert page_srp.link_contains_match_for(thing), \
            "Search results are not related to {}".format(thing)
    elif form == "is":
        assert not page_srp.is_loaded, "Search results page is loaded when it shouldn't"
        assert not page_hp.is_loaded, "Google home page is loaded when it shouldn't"

        assert "google" not in context.driver.title.lower(), \
            "Google is in page title: {}".format(context.driver.title.lower())
        assert thing.lower() in context.driver.title.lower(), \
            "{} is not in page title: {}".format(thing, context.driver.title.lower())
    else:
        raise Exception("Unknown form")
