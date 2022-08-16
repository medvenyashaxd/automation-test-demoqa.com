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
        self.element_is_visible(self.locators.SIMPLE_ALERT).click()
        simple_alert = self.switch_to_alert()
        text_simple_button = simple_alert.text
        simple_alert.accept()
        self.element_is_visible(self.locators.TIME_ALERT).click()
        time.sleep(5)
        time_alert = self.switch_to_alert()
        text_time_alert = time_alert.text
        time_alert.accept()
        return text_simple_button, text_time_alert
