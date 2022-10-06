from selenium.webdriver.common.by import By


class ButtonsPage:

    PAGE_TITLE = (By.CLASS_NAME, "main-header")
    DOUBLE_CLICK_BUTTON = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.ID, "rightClickBtn")
    CLICK_BUTTON = (By.CSS_SELECTOR, ".col-md-6 div div:last-child") # aici se schimba de fiecare data id-ul

    URL = 'https://demoqa.com/buttons'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_page_title(self):
        return self.browser.find_element(*self.PAGE_TITLE).text

    def is_double_click_button_displayed(self):
        return self.browser.find_element(*self.DOUBLE_CLICK_BUTTON).is_displayed

    def is_right_click_button_displayed(self):
        return self.browser.find_element(*self.RIGHT_CLICK_BUTTON).is_displayed

    def is_click_button_displayed(self):
        return self.browser.find_element(*self.CLICK_BUTTON).is_displayed

