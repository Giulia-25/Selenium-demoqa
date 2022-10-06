from selenium.webdriver.common.by import By


class TextBox:

    PAGE_TITLE = (By.CLASS_NAME, "main-header")
    NAME_INPUT = (By.ID, "userName")
    EMAIL_INPUT = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    PAGE_LOGO = (By.CSS_SELECTOR, '[src="/images/Toolsqa.jpg"]')
    OUTPUT_MESSAGE = (By.ID, "output")
    FIELD_ERROR = (By.CSS_SELECTOR, "[class *= field-error]")

    URL = 'https://demoqa.com/text-box'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def is_page_logo_displayed(self):
        return self.browser.find_element(*self.PAGE_TITLE).is_displayed

    def get_page_title(self):
        return self.browser.find_element(*self.PAGE_TITLE).text

    def is_submit_button_displayed(self):
        return self.browser.find_element(*self.SUBMIT_BUTTON).is_displayed

    def click_submit_button(self):
        self.browser.find_element(*self.SUBMIT_BUTTON).click()

    def insert_name(self, firstname, lastname):
        self.browser.find_element(*self.NAME_INPUT).send_keys(firstname, lastname)

    def insert_email(self, email):
        self.browser.find_element(*self.EMAIL_INPUT).send_keys(email)

    def insert_current_address(self, current_address):
        self.browser.find_element(*self.CURRENT_ADDRESS).send_keys(current_address)

    def insert_permanent_address(self, permanent_address):
        self.browser.find_element(*self.PERMANENT_ADDRESS).send_keys(permanent_address)

    def is_output_message_displayed(self):
        return self.browser.find_element(*self.OUTPUT_MESSAGE).is_displayed

    def is_field_error_displayed(self):
        return self.browser.find_element(*self.FIELD_ERROR).is_displayed

