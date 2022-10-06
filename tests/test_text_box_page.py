from time import sleep

import pytest
from assertpy import soft_assertions, assert_that

from pages.text_box_page import TextBox


@pytest.fixture
def test_text_box_page(browser):
    return TextBox(browser)


@pytest.mark.skip
def test_text_box_page_successful(browser, test_text_box_page):
    test_text_box_page.load_page()
    with soft_assertions():
        assert_that(test_text_box_page.get_page_title()).is_equal_to("Text Box")
        assert_that(browser.current_url).is_equal_to(test_text_box_page.URL)
        assert_that(test_text_box_page.is_submit_button_displayed()).is_true()
        assert_that(test_text_box_page.is_page_logo_displayed()).is_true()


@pytest.mark.skip
def test_registration_successful(browser, test_text_box_page):
    test_text_box_page.load_page()
    test_text_box_page.insert_name("Giulia ", "Lazar")
    sleep(1)
    test_text_box_page.insert_email("blaaa@bla.com")
    sleep(1)
    test_text_box_page.insert_current_address("@home")
    sleep(1)
    test_text_box_page.insert_permanent_address("on the moon")
    sleep(1)
    test_text_box_page.click_submit_button()
    assert_that(test_text_box_page.is_output_message_displayed()).is_true()


def test_registration_negative(browser, test_text_box_page):
    test_text_box_page.load_page()
    test_text_box_page.insert_name("Giulia ", "Lazar")
    sleep(1)
    test_text_box_page.insert_email("...")
    sleep(1)
    test_text_box_page.insert_current_address("@home")
    sleep(1)
    test_text_box_page.insert_permanent_address("on the moon")
    sleep(1)
    test_text_box_page.click_submit_button()
    assert_that(test_text_box_page.is_field_error_displayed()).is_true()