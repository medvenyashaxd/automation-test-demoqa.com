import random
import time

from selenium.common import TimeoutException
from generator_data.generator import generator_color
from locators.widgets_locators import AccordianLocators, AutoCompleteLocators, DatePickerLocators
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

    def check_multiple_color(self):
        colors = random.sample(next(generator_color()).color, k=(random.randint(2, 4)))
        multiple_input = self.element_is_present(self.locators.MULTIPLE_COLORS_INPUT)

        for color in colors:
            multiple_input.send_keys(color)
            self.press_enter()

        buttons_delete = self.elements_are_present(self.locators.DELETE_BUTTON)
        buttons_delete[random.randint(0, 1)].click()

        color_after = self.elements_are_present(self.locators.BUTTONS_COLOR_TEXT)
        buttons_color_text = []
        for button in color_after:
            buttons_color_text.append(button.text)

        return colors, buttons_color_text

    def clear_all(self):
        self.element_is_present(self.locators.CLEAR_ALL).click()
        try:
            color_after = self.elements_are_present(self.locators.BUTTONS_COLOR_TEXT)
            buttons_color_text = []

            for button in color_after:
                buttons_color_text.append(button.text)

        except TimeoutException:

            return True

    def check_single_color(self):
        single_color = random.sample(next(generator_color()).color, k=1)
        self.element_is_present(self.locators.SINGLE_COLOR_INPUT).send_keys(single_color)
        self.press_enter()
        get_single_color = self.element_is_present(self.locators.BUTTON_COLOR_TEXT).text
        return single_color, [get_single_color]


class DatePickerPage(BasePage):
    locators = DatePickerLocators()

    def set_time(self):
        select_date = self.element_is_visible(self.locators.SELECT_DATE)
        date = select_date.get_attribute('value')
        select_date.click()

        self.select_by_value(self.locators.SELECT_MONTH, value=f"{random.randint(0, 11)}")

        self.select_by_value(self.locators.SELECT_YEAR, value=f"{random.randint(1985, 2005)}")

        days = self.elements_are_present(self.locators.SELECT_DAY)
        days[random.randint(2, 28)].click()
        date_after = select_date.get_attribute('value')
        return date, date_after