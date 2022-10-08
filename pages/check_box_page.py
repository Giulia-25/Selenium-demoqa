from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckBox:

    PAGE_TITLE = (By.CLASS_NAME, "main-header")
    EXPAND_ALL_BUTTON = (By.CLASS_NAME, "rct-icon-expand-all")
    COLLAPSE_ALL_BUTTON = (By.CLASS_NAME, "rct-icon-collapse-all")
    HOME_CHECKBOX = (By.CLASS_NAME, "rct-title")
    DESKTOP_CHECKBOX = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(1)")
    NOTES_CHECKBOX = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(1) "
                                       "> ol > li:nth-child(1) > span > label > span.rct-title")
    DOCUMENTS_CHECKBOX = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2)")
    WORKSPACE_CHECKBOX = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(1)")
    OFFICE_CHECKBOX = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2)")
    DOWNLOADS_CHECKBOX = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(3)")
    EXPAND_HOME_CHECKBOX = (By.CSS_SELECTOR, "#tree-node > ol > li > span > button")
    EXPAND_DESKTOP_CHECKBOX = (By.CSS_SELECTOR, "li > ol > li:nth-child(1) > span > button > svg")


    URL = 'https://demoqa.com/checkbox'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_page_title(self):
        return self.browser.find_element(*self.PAGE_TITLE).text

    def is_expand_all_button_displayed(self):
        return self.browser.find_element(*self.EXPAND_ALL_BUTTON).is_displayed()

    def is_collapse_all_button_displayed(self):
        return self.browser.find_element(*self.COLLAPSE_ALL_BUTTON).is_displayed()

    def click_expand_all_button(self):
        self.browser.find_element(*self.EXPAND_ALL_BUTTON).click()

    def click_collapse_all_button(self):
        self.browser.find_element(*self.COLLAPSE_ALL_BUTTON).click()

    def is_home_checkbox_displayed(self):
        return self.browser.find_element(*self.HOME_CHECKBOX).is_displayed()

    def click_home_checkbox(self):
        self.browser.find_element(*self.HOME_CHECKBOX).click()

    def is_home_checkbox_selected(self):
        return self.browser.find_element(*self.HOME_CHECKBOX).is_selected

    def click_expand_home_checkbox(self):
        self.browser.find_element(*self.EXPAND_HOME_CHECKBOX).click()

    def is_desktop_checkbox_displayed(self):
        return self.browser.find_element(*self.DESKTOP_CHECKBOX).is_displayed()

    def click_desktop_checkbox(self):
        self.browser.find_element(*self.DESKTOP_CHECKBOX).click()

    def is_desktop_checkbox_selected(self):
        return self.browser.find_element(*self.DESKTOP_CHECKBOX).is_selected

    def click_expand_desktop_checkbox(self):
        self.browser.find_element(*self.EXPAND_DESKTOP_CHECKBOX).click()

    def is_notes_checkbox_displayed(self):
        return self.browser.find_element(*self.NOTES_CHECKBOX).is_displayed()

    def is_notes_checkbox_selected(self):
        return self.browser.find_element(*self.NOTES_CHECKBOX).is_selected

    def click_notes_checkbox(self):
        self.browser.find_element(*self.NOTES_CHECKBOX).click()

    def is_documents_checkbox_displayed(self):
        return self.browser.find_element(*self.DOCUMENTS_CHECKBOX).is_displayed()

    def click_documents_checkbox(self):
        self.browser.find_element(*self.DOCUMENTS_CHECKBOX).click()

    def is_workspace_checkbox_displayed(self):
        return self.browser.find_element(*self.WORKSPACE_CHECKBOX).is_displayed()

    def is_office_checkbox_displayed(self):
        return self.browser.find_element(*self.OFFICE_CHECKBOX).is_displayed()

    def is_downloads_checkbox_displayed(self):
        return self.browser.find_element(*self.DOWNLOADS_CHECKBOX).is_displayed()

    def click_downloads_checkbox(self):
        self.browser.find_element(*self.DOWNLOADS_CHECKBOX).click()