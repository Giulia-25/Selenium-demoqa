from selenium.webdriver.common.by import By


class RadioButton:

    PAGE_TITLE = (By.CLASS_NAME, "main-header")
    QUESTION = (By.CLASS_NAME, "mb-3")
    YES_BUTTON = (By.CSS_SELECTOR, '[for="yesRadio"]')
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, '[for="impressiveRadio"]')
    NO_BUTTON = (By.CSS_SELECTOR, '[for="noRadio"]')

    URL = 'https://demoqa.com/radio-button'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_page_title(self):
        return self.browser.find_element(*self.PAGE_TITLE).text

    