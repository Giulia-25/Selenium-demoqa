from time import sleep

import pytest
from assertpy import soft_assertions, assert_that

from pages.buttons_page import ButtonsPage


@pytest.fixture
def test_buttons_page(browser):
    return ButtonsPage(browser)


def test_page(browser, test_buttons_page):
    test_buttons_page.load_page()
    with soft_assertions():
        assert_that(test_buttons_page.get_page_title()).is_equal_to("Buttons")
        assert_that(browser.current_url).is_equal_to(test_buttons_page.URL)
        assert_that(test_buttons_page.is_double_click_button_displayed()).is_true()
        assert_that(test_buttons_page.is_right_click_button_displayed()).is_true()
        assert_that(test_buttons_page.is_click_button_displayed()).is_true()

# def test_double_click_button(browser, test_buttons_page):
#     test_buttons_page.load_page()
#     with soft_assertions():



