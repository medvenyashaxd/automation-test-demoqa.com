import time

from locators.alerts_frame_window_locators import BrowserWindowLocators, AlertsLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowLocators()

    def test_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        self.switch_to_window(1)
        text_in_new_tab = self.element_is_present(self.locators.TEXT_IN_TAB).text
        self.switch_to_window(0)
        return text_in_new_tab

    def test_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.switch_to_window(1)
        text_in_new_window = self.element_is_present(self.locators.TEXT_IN_WINDOW).text
        return text_in_new_window


class AlertPage(BasePage):
    locators = AlertsLocators()

    def click_buttons_and_get_text(self):
        self.element_is_visible(self.locators.SAMPLE_BUTTON).click()
        alert = self.switch_to_alert()
        text_sample_button = alert.text
        alert.accept()

        return text_sample_button
