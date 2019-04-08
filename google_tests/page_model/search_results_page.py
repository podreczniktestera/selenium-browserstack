# -*- coding: UTF-8 -*-
from google_tests.page_model.base_page import BasePage
from google_tests.locators.search_results_page import SearchResultsPageLocators


class SearchResultsPage(BasePage):
    @property
    def is_loaded(self):
        return "/search" in self.driver.current_url

    def link_contains_match_for(self, term):
        result_section = self.driver.find_element(*SearchResultsPageLocators.RESULT_SECTION)
        elements = result_section.find_elements(*SearchResultsPageLocators.RESULT_ELEMENTS)
        return any(term in element.text for element in elements)
