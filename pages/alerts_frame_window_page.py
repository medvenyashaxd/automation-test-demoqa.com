from locators.alerts_frame_window_locators import BrowserWindowLocators
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
