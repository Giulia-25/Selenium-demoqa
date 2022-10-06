from time import sleep

import pytest
from assertpy import soft_assertions, assert_that

from pages.radio_button_page import RadioButton


@pytest.fixture
def test_radio_button_page(browser):
    return RadioButton(browser)


@pytest.mark.skip
def test_radio_buttons_page(browser, test_radio_button_page):
    test_radio_button_page.load_page()
    with soft_assertions():
        assert_that(test_radio_button_page.get_page_title()).is_equal_to("Radio Button")
        assert_that(test_radio_button_page.get_question()).contains("like the site?")
        assert_that(test_radio_button_page.is_yes_button_displayed()).is_true()
        assert_that(test_radio_button_page.is_impressive_button_displayed()).is_true()
        assert_that(test_radio_button_page.is_no_button_displayed()).is_true()


@pytest.mark.skip
def test_yes_radio_button(browser, test_radio_button_page):
    test_radio_button_page.load_page()
    test_radio_button_page.click_yes_button()
    assert_that(test_radio_button_page.is_yes_button_selected()).is_true()
    assert_that(test_radio_button_page.get_text_after_yes()).is_equal_to("You have selected Yes")


@pytest.mark.skip
def test_impressive_button(browser, test_radio_button_page):
    test_radio_button_page.load_page()
    test_radio_button_page.click_impressive_button()
    assert_that(test_radio_button_page.is_impressive_button_selected()).is_true()
    assert_that(test_radio_button_page.get_text_after_impressive()).is_equal_to("You have selected Impressive")


def test_no_button(browser, test_radio_button_page):
    test_radio_button_page.load_page()
    assert_that(test_radio_button_page.is_no_button_selected()).is_false()
    # AssertionError: Expected <False>, but was not.
