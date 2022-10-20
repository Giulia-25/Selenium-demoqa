
import pytest
from assertpy import soft_assertions, assert_that

from pages.radio_button_page import RadioButton


@pytest.fixture
def test_radio_button_page(browser):
    return RadioButton(browser)


def test_page(browser, test_radio_button_page):
    test_radio_button_page.load_page()
    with soft_assertions():
        assert_that(test_radio_button_page.get_page_title()).is_equal_to("Radio Button")
        assert_that(test_radio_button_page.get_question()).contains("like the site?")
        assert_that(test_radio_button_page.is_yes_button_displayed()).is_true()
        assert_that(test_radio_button_page.is_impressive_button_displayed()).is_true()
        assert_that(test_radio_button_page.is_no_button_displayed()).is_true()


def test_yes_radio_button(browser, test_radio_button_page):
    test_radio_button_page.load_page()
    test_radio_button_page.click_yes_button()
    assert_that(test_radio_button_page.get_text_after_click()).is_equal_to("You have selected Yes")


def test_impressive_button(browser, test_radio_button_page):
    test_radio_button_page.load_page()
    test_radio_button_page.click_impressive_button()
    assert_that(test_radio_button_page.get_text_after_click()).is_equal_to("You have selected Impressive")


def test_no_button(browser, test_radio_button_page):
    test_radio_button_page.load_page()
    test_radio_button_page.click_no_button()
    assert_that(test_radio_button_page.is_displayed_text_after_click()).is_false()

