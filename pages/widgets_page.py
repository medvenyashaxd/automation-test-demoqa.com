from locators.widgets_locators import AccordianLocators
from pages.base_page import BasePage


class WidgetsPage(BasePage):
    locators = AccordianLocators()

    def check_accordian(self, section_num):
        sections = {'section_one':
                    {'header': self.locators.SECTION_ONE,
                        'text': self.locators.TEXT_SECTION_ONE},

                    'section_two':
                    {'header': self.locators.SECTION_TWO,
                        'text': self.locators.TEXT_SECTION_TWO},

                    'section_three':
                    {'header': self.locators.SECTION_THREE,
                        'text': self.locators.TEXT_SECTION_THREE}
                    }

        self.element_is_visible(sections[section_num]['header']).click()
        text_section = self.element_is_visible(sections[section_num]['text']).text

        return len(text_section)