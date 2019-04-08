# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By


class HomePageLocators:
    GOOGLE_LOGO = By.ID, 'hplogo'
    SEARCH_BAR = By.NAME, 'q'
    SEARCH_BUTTON = By.NAME, 'btnG'
    FEELING_LUCKY_BUTTON = By.NAME, 'btnI'
