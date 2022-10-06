from selenium.webdriver.common.by import By


class RadioButton:

    PAGE_TITLE = (By.CLASS_NAME, "main-header")
    QUESTION = (By.CLASS_NAME, "mb-3")
    YES_BUTTON = (By.CSS_SELECTOR, '[for="yesRadio"]')
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, '[for="impressiveRadio"]')
    NO_BUTTON = (By.CSS_SELECTOR, '[for="noRadio"]')
    AFTER_CLICK_TEXT = (By.CLASS_NAME, "mt-3")

    URL = 'https://demoqa.com/radio-button'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_page_title(self):
        return self.browser.find_element(*self.PAGE_TITLE).text

    def get_question(self):
        return self.browser.find_element(*self.QUESTION).text

    def is_yes_button_displayed(self):
        return self.browser.find_element(*self.YES_BUTTON).is_displayed

    def is_impressive_button_displayed(self):
        return self.browser.find_element(*self.IMPRESSIVE_BUTTON).is_displayed

    def is_no_button_displayed(self):
        return self.browser.find_element(*self.NO_BUTTON).is_displayed

    def is_yes_button_selected(self):
        return self.browser.find_element(*self.YES_BUTTON).is_selected

    def is_impressive_button_selected(self):
        return self.browser.find_element(*self.IMPRESSIVE_BUTTON).is_selected

    def is_no_button_selected(self):
        return self.browser.find_element(*self.NO_BUTTON).is_selected

    def click_yes_button(self):
        self.browser.find_element(*self.YES_BUTTON).click()

    def click_impressive_button(self):
        self.browser.find_element(*self.IMPRESSIVE_BUTTON).click()

    def click_no_button(self):
        self.browser.find_element(*self.NO_BUTTON).click()

    def get_text_after_yes(self):
        return self.browser.find_element(*self.AFTER_CLICK_TEXT).text

    def get_text_after_impressive(self):
        return self.browser.find_element(*self.AFTER_CLICK_TEXT).text