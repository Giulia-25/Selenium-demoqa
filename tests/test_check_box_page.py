import pytest
from assertpy import soft_assertions, assert_that

from pages.check_box_page import CheckBox


@pytest.fixture
def test_check_box_page(browser):
    return CheckBox(browser)


def test_page(browser, test_check_box_page):
    test_check_box_page.load_page()
    with soft_assertions():
        assert_that(test_check_box_page.get_page_title()).is_equal_to("Check Box")
        assert_that(browser.current_url).is_equal_to(test_check_box_page.URL)
        assert_that(test_check_box_page.is_expand_all_button_displayed()).is_true()
        assert_that(test_check_box_page.is_collapse_all_button_displayed()).is_true()
        assert_that(test_check_box_page.is_home_checkbox_displayed()).is_true()


def test_expand_all_button(browser, test_check_box_page):
    test_check_box_page.load_page()
    test_check_box_page.click_expand_all_button()
    with soft_assertions():
        assert_that(test_check_box_page.is_desktop_checkbox_displayed()).is_true()
        assert_that(test_check_box_page.is_documents_checkbox_displayed()).is_true()
        assert_that(test_check_box_page.is_workspace_checkbox_displayed()).is_true()
        assert_that(test_check_box_page.is_office_checkbox_displayed()).is_true()
        assert_that(test_check_box_page.is_downloads_checkbox_displayed()).is_true()


def test_collapse_all_button (browser, test_check_box_page):
    test_check_box_page.load_page()
    test_check_box_page.click_expand_all_button()
    test_check_box_page.click_collapse_all_button()
    test_check_box_page.click_expand_home_checkbox()
    with soft_assertions():
        assert_that(test_check_box_page.is_desktop_checkbox_displayed()).is_true()
        assert_that(test_check_box_page.is_documents_checkbox_displayed()).is_true()
        assert_that(test_check_box_page.is_downloads_checkbox_displayed()).is_true()
        # assert_that(test_check_box_page.is_workspace_checkbox_displayed()).is_false()
        # NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css s
        # elector","selector":"#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(1)"}


def test_desktop_checkboxes(browser, test_check_box_page):
    test_check_box_page.load_page()
    test_check_box_page.click_home_checkbox()
    test_check_box_page.click_expand_home_checkbox()
    test_check_box_page.click_documents_checkbox()
    test_check_box_page.click_downloads_checkbox()
    test_check_box_page.click_expand_desktop_checkbox()
    with soft_assertions():
        assert_that(test_check_box_page.is_home_checkbox_selected()).is_true()
        assert_that(test_check_box_page.is_notes_checkbox_displayed()).is_true()
        assert_that(test_check_box_page.is_notes_checkbox_selected()).is_true()


def test_angular_checkbox(browser, test_check_box_page):
    test_check_box_page.load_page()
    test_check_box_page.click_expand_all_button()
    test_check_box_page.click_documents_checkbox()
    with soft_assertions():
        assert_that(test_check_box_page.is_angular_file_checkbox_selected()).is_true()
        assert_that(test_check_box_page.is_angular_file_checkbox_displayed()).is_true()
        assert_that(test_check_box_page.is_workspace_checkbox_selected()).is_true()
        assert_that(test_check_box_page.is_documents_checkbox_selected()).is_true()
        assert_that(test_check_box_page.is_home_checkbox_selected()).is_true()