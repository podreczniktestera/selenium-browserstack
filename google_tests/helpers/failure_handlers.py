# -*- coding: UTF-8 -*-
import os


def create_dir_if_not_exists(path):
    path = 'failures/' + path
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def save_screenshot(driver, path):
    path = create_dir_if_not_exists(path)
    file = '{}/screenshot.jpg'.format(path)
    driver.save_screenshot(file)


def save_html_source(driver, path):
    path = create_dir_if_not_exists(path)
    file = '{}/html_source.html'.format(path)
    with open(file, 'w', encoding="utf-8") as file:
        file.write(driver.page_source)


def handle_scenario_failure(driver, scenario_name, screenshot=True, page_source=True):
    if screenshot:
        save_screenshot(driver, scenario_name)
    if page_source:
        save_html_source(driver, scenario_name)
