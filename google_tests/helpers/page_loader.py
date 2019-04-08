# -*- coding: UTF-8 -*-


def require_loaded(func):
    def load_page(page, *params, **kwds):
        if not page.is_loaded:
            page.load()
        assert page.is_loaded, "page should be loaded by now"
        return func(page, *params, **kwds)
    return load_page


class PageLoader(object):
    def __call__(self, driver):
        page_state = driver.execute_script('return document.readyState;')
        return page_state == 'complete'
