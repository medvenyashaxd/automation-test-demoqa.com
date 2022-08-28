import random
import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from generator_data.generator import generator_color
from locators.widgets_locators import AccordianLocators, AutoCompleteLocators, DatePickerLocators, SliderLocators, \
    ProgressBarLocators, TabsLocators, ToolTipsLocators, MenuLocators, SelectMenuLocators
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


class SliderPage(BasePage):
    locators = SliderLocators()

    def move_the_slider(self):
        slider = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_by_offset(slider, random.randint(1, 100), 0)

        value = self.element_is_present(self.locators.SLIDER_VALUE)
        changed_value = value.get_attribute('value')

        return changed_value


class ProgressBarPage(BasePage):
    locators = ProgressBarLocators()

    def check_progress_bar(self):
        slider = self.element_is_present(self.locators.PROGRESS_SLIDER)
        status_slider = slider.get_attribute('aria-valuenow')

        self.element_is_present(self.locators.BUTTON_START).click()
        time.sleep(11)

        status_after = slider.get_attribute('aria-valuenow')

        return status_slider, status_after


class TabsPage(BasePage):
    locators = TabsLocators()

    def check_tabs(self, tab):
        tabs = {'whats':
                {'tab': self.locators.TAB_WHAT,
                 'text': self.locators.TEXT_WHAT},

                'origin':
                {'tab': self.locators.TAB_ORIGIN,
                 'text': self.locators.TEXT_ORIGIN},

                'use':
                {'tab': self.locators.TAB_USE,
                 'text': self.locators.TEXT_USE},

                'more':
                {'tab': self.locators.TAB_MORE}
                }
        try:
            self.element_is_visible(tabs[tab]['tab']).click()

            text = self.element_is_present(tabs[tab]['text']).text

            return len(text)

        except ElementClickInterceptedException:

            return False


class ToolTipsPage(BasePage):
    locators = ToolTipsLocators()

    def check_tool_tips_page(self, element):
        elements = {'button':
                    {'locator': self.locators.BUTTON},

                    'input':
                    {'locator': self.locators.INPUT},

                    'contrary':
                    {'locator': self.locators.CONTRARY},

                    'numbers':
                    {'locator': self.locators.NUMBERS}
                    }

        self.go_to_element(self.element_is_present(elements[element]['locator']))

        self.action_move_to_element(self.element_is_present(elements[element]['locator']))

        time.sleep(1)

        tool_tip_text = self.element_is_visible(self.locators.TEXT).text

        return tool_tip_text


class MenuPage(BasePage):
    locators = MenuLocators()

    def check_menu(self):
        href_links = self.elements_are_present(self.locators.HREF)

        list_menu = []

        for link in href_links:
            self.action_move_to_element(link)
            list_menu.append(link.text)

        return list_menu


class SelectMenuPage(BasePage):
    locators = SelectMenuLocators()

    def check_select_menu(self, select):

        selects = {'select_value':
                    {'menu': self.locators.SELECT_VALUE,
                     'click_value': self.locators.SELECT_VALUE_MENU},

                   'select_one':
                    {'menu': self.locators.SELECT_ONE,
                     'click_value': self.locators.SELECT_ONE_MENU},

                   'multiselect':
                    {'menu': self.locators.MULTISELECT,
                     'click_value': self.locators.MULTISELECT_VALUE}
                   }

        self.element_is_visible(selects[select]['menu']).click()
        self.element_is_present(selects[select]['click_value']).click()

        self.select_by_value(self.locators.SELECT_STYLE, value=f"{random.randint(1, 10)}")

        self.select_by_index(self.locators.CARS, value=f"{random.randint(0, 3)}")

        return True
