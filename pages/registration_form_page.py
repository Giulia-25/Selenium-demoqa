from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class RegistrationForm:

    PAGE_TITLE = (By.CLASS_NAME, "main-header")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    FIRSTNAME_INPUT = (By.ID, "firstName")
    LASTNAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    MALE_GENDER_RADIOBUTTON = (By.CSS_SELECTOR, '[for ="gender-radio-1"]')
    FEMALE_GENDER_RADIOBUTTON = (By.CSS_SELECTOR, '[for ="gender-radio-2"]')
    OTHER_GENDER_RADIOBUTTON = (By.CSS_SELECTOR, '[for ="gender-radio-3"]')
    TEL_NUMBER_INPUT = (By.ID, "userNumber") #min/max length = 10
    # SPORTS_CHECKBOX = (By.ID, "hobbies-checkbox-1")
    SPORTS_CHECKBOX = (By.CSS_SELECTOR, '[for = "hobbies-checkbox-1"]')
    # READING_CHECKBOX = (By.ID, "hobbies-checkbox-2")
    READING_CHECKBOX = (By.CSS_SELECTOR, '[for = "hobbies-checkbox-2"]')
    # MUSIC_CHECKBOX = (By.ID, "hobbies-checkbox-3")
    MUSIC_CHECKBOX = (By.CSS_SELECTOR, '[for = "hobbies-checkbox-3"]')

    CHOOSE_FILE_BUTTON = (By.ID, "uploadPicture")

    URL = 'https://demoqa.com/automation-practice-form'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_page_title(self):
        return self.browser.find_element(*self.PAGE_TITLE).text

    def is_submit_button_displayed(self):
        return self.browser.find_element(*self.SUBMIT_BUTTON).is_displayed

    def click_submit_button(self):
        self.browser.find_element(*self.SUBMIT_BUTTON).click()

    def insert_firstname(self, firstname):
        self.browser.find_element(*self.FIRSTNAME_INPUT).send_keys(firstname)

    def insert_lastname(self, lastname):
        self.browser.find_element(*self.LASTNAME_INPUT).send_keys(lastname)

    def insert_email(self, email):
        self.browser.find_element(*self.EMAIL_INPUT).send_keys(email)

    def click_male_gender_button(self):
        self.browser.find_element(*self.MALE_GENDER_RADIOBUTTON).click()

    def click_female_gender_button(self):
        self.browser.find_element(*self.FEMALE_GENDER_RADIOBUTTON).click()

    def click_other_gender_button(self):
        self.browser.find_element(*self.OTHER_GENDER_RADIOBUTTON).click()

    def is_male_gender_button_selected(self):
        return self.browser.find_element(*self.MALE_GENDER_RADIOBUTTON).is_selected()

    def is_female_gender_button_selected(self):
        return self.browser.find_element(*self.FEMALE_GENDER_RADIOBUTTON).is_selected()

    def is_other_gender_button_selected(self):
        return self.browser.find_element(*self.OTHER_GENDER_RADIOBUTTON).is_selected()

    def insert_tel_number(self, number=10):
        self.browser.find_element(*self.TEL_NUMBER_INPUT).send_keys(number)

    def click_sports_checkbox(self):
        self.browser.find_element(*self.SPORTS_CHECKBOX).click()

    def click_reading_checkbox(self):
        self.browser.find_element(*self.READING_CHECKBOX).click()

    def click_music_checkbox(self):
        self.browser.find_element(*self.MUSIC_CHECKBOX).click()

    def is_sports_checkbox_selected(self):
        return self.browser.find_element(*self.SPORTS_CHECKBOX).is_selected

    def is_reading_checkbox_selected(self):
        return self.browser.find_element(*self.READING_CHECKBOX).is_selected

    def is_music_checkbox_selected(self):
        return self.browser.find_element(*self.MUSIC_CHECKBOX).is_selected

