from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ButtonsPage:

    PAGE_TITLE = (By.CLASS_NAME, "main-header")
    DOUBLE_CLICK_BUTTON = (By.ID, "doubleClickBtn")
    RIGHT_CLICK_BUTTON = (By.ID, "rightClickBtn")
    DYNAMIC_CLICK_BUTTON = (By.CSS_SELECTOR, '[class="col-12 mt-4 col-md-6"]>div:nth-child(2)>div:nth-child(3)>button')
    DOUBLE_CLICK_MESSAGE = (By.CSS_SELECTOR, '[id="doubleClickMessage"]')
    RIGHT_CLICK_MESSAGE = (By.CSS_SELECTOR, '[id="rightClickMessage"]')
    DYNAMIC_CLICK_MESSAGE = (By.ID, "dynamicClickMessage")

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
        return self.browser.find_element(*self.DYNAMIC_CLICK_BUTTON).is_displayed

    def click_double_click_button(self):
        action = ActionChains(self.browser)
        action.double_click(self.browser.find_element(*self.DOUBLE_CLICK_BUTTON)).perform()

    def click_right_click_button(self):
        action = ActionChains(self.browser)
        action.context_click(self.browser.find_element(*self.RIGHT_CLICK_BUTTON)).perform()

    def click_dynamic_click_button(self):
        self.browser.find_element(*self.DYNAMIC_CLICK_BUTTON).click()

    def is_double_click_message_displayed(self):
        double_click_message = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[id="doubleClickMessage"]')))
        return double_click_message.is_displayed()

    def is_right_click_message_displayed(self):
        right_click_message = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, "rightClickMessage")))
        return right_click_message.is_displayed()

    def is_dynamic_click_message_displayed(self):
        dynamic_click_message = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, "dynamicClickMessage")))
        return dynamic_click_message.is_displayed()

    def get_double_click_message(self):
        return self.browser.find_element(*self.DOUBLE_CLICK_MESSAGE).text

    def get_right_click_message(self):
        return self.browser.find_element(*self.RIGHT_CLICK_MESSAGE).text

    def get_dynamic_click_message(self):
        return self.browser.find_element(*self.DYNAMIC_CLICK_MESSAGE).text
