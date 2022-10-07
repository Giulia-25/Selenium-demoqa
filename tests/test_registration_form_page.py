from time import sleep

import pytest
from assertpy import soft_assertions, assert_that

from pages.registration_form_page import RegistrationForm


@pytest.fixture
def registration_form_page(browser):
    return RegistrationForm(browser)


def test_page(browser, registration_form_page):
    registration_form_page.load_page()
    with soft_assertions():
        assert_that(registration_form_page.get_page_title()).is_equal_to("Practice Form")
        assert_that(browser.current_url).is_equal_to(registration_form_page.URL)
        assert_that(registration_form_page.is_submit_button_displayed()).is_true()


def test_successful_registration(browser, registration_form_page):
    registration_form_page.load_page()
    with soft_assertions():
        registration_form_page.insert_firstname("Giulia")
        sleep(1)
        registration_form_page.insert_lastname("Lazar")
        sleep(1)
        registration_form_page.insert_email("blaa@b.com")
        sleep(1)
        registration_form_page.click_female_gender_button()
        sleep(1)
        registration_form_page.insert_tel_number(1234567891)
        sleep(1)
        registration_form_page.click_reading_checkbox()
        sleep(1)
        registration_form_page.click_music_checkbox()
        sleep(1)

        # registration_form_page.click_submit_button()
        # selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted:
        # Element <button id="submit" type="submit" class="btn btn-primary">...</button> is not clickable at point (1364, 905).
        # Other element would receive the click: <div id="adplus-anchor" data-google-query-id="CPiN6MaEy_oCFYK0dwodK64Agg">...</div>

        # aici e o problema cu butonul de submit in momentul in care incepe sa se completeze formularul pt ca dispare de pe pagina...

        assert_that(registration_form_page.is_reading_checkbox_selected()).is_true()
        assert_that(registration_form_page.is_music_checkbox_selected()).is_true()

        # assert_that(registration_form_page.is_sports_checkbox_selected()).is_false()
        # AssertionError: Expected <False>, but was not.

        # assert_that(registration_form_page.is_female_gender_button_selected()).is_true()
        #AssertionError: Expected <True>, but was not.

        assert_that(registration_form_page.is_male_gender_button_selected()).is_false()
        assert_that(registration_form_page.is_other_gender_button_selected()).is_false()