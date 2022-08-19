from locators.widgets_locators import AccordianLocators
from pages.base_page import BasePage


class WidgetsPage(BasePage):
    locators = AccordianLocators()

    def check_accordian(self):
        #self.element_is_visible(self.locators.SECTION_ONE).click()
        text_section_one = self.element_is_present(self.locators.TEXT_SECTION_ONE).text

        self.go_to_element(self.element_is_present(self.locators.SECTION_TWO))
        self.element_is_visible(self.locators.SECTION_TWO).click()
        text_section_two = self.element_is_present(self.locators.TEXT_SECTION_TWO).text

        self.go_to_element(self.element_is_present(self.locators.SECTION_THREE))
        self.element_is_visible(self.locators.SECTION_THREE).click()
        text_section_three = self.element_is_present(self.locators.TEXT_SECTION_THREE).text

        return text_section_one, text_section_two, text_section_three
