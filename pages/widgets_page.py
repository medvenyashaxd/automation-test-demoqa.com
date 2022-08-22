import random
import time

from selenium.common import TimeoutException

from generator_data.generator import generator_color
from locators.widgets_locators import AccordianLocators, AutoCompleteLocators
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


class AutoCompletePage(BasePage):
    locators = AutoCompleteLocators()

    def check_multiple_auto_complete(self):
        colors = random.sample(next(generator_color()).color, k=(random.randint(3, 5)))

        for color in colors:
            self.element_is_present(self.locators.MULTIPLE_INPUT).send_keys(color)

            time.sleep(1)

            self.press_enter()

        return len(colors)

    def delete_auto_complete(self):
        buttons = self.elements_are_present(self.locators.DELETE_COLORS)
        buttons[random.randint(0, 2)].click()

        colors = self.elements_are_present(self.locators.MULTIPLE_COLORS)
        list_color = []

        for color in colors:
            list_color.append(color.text)

        return len(list_color)

    def clear_auto_complete(self):
        self.element_is_present(self.locators.CLEAR_COLORS).click()

        try:
            colors = self.elements_are_present(self.locators.MULTIPLE_COLORS)
            list_color = []

            for color in colors:
                list_color.append(color.text)

            return list_color

        except TimeoutException:

            return True

    def check_auto_complete_single_color(self):
        colors = random.sample(next(generator_color()).color, k=1)
        time.sleep(1)
        self.element_is_present(self.locators.SINGLE_INPUT).send_keys(colors)

        time.sleep(1)

        self.press_enter()
        text = self.element_is_present(self.locators.SINGLE_TEXT).text

        return colors, [text]
