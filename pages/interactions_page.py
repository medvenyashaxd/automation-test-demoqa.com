import random

from locators.interactions_locators import SortableLocators, SelectableLocators
from pages.base_page import BasePage


class SortablePage(BasePage):

    locators = SortableLocators()

    def get_order_of_numbers(self, locator):
        numbers_list = self.elements_are_present(locator)
        return [number.text for number in numbers_list]

    def get_number(self, locator):
        numbers_list = self.elements_are_present(locator)
        return [number for number in numbers_list][random.randint(0, 5)]

    def check_sortable(self):
        order_of_numbers_list_before = self.get_order_of_numbers(self.locators.NUMBERS_LIST)
        self.action_drag_and_drop(self.get_number(self.locators.NUMBERS_LIST), self.get_number\
                                                                                        (self.locators.NUMBERS_LIST))
        order_of_numbers_list_after = self.get_order_of_numbers(self.locators.NUMBERS_LIST)

        self.element_is_visible(self.locators.GRID_PAGE).click()
        order_of_numbers_grid_before = self.get_order_of_numbers(self.locators.GRID_LIST)
        self.action_drag_and_drop(self.get_number(self.locators.GRID_LIST), self.get_number(self.locators.GRID_LIST))
        order_of_numbers_grid_after = self.get_order_of_numbers(self.locators.GRID_LIST)

        return order_of_numbers_list_before, order_of_numbers_list_after, order_of_numbers_grid_before,\
               order_of_numbers_grid_after


class SelectablePage(BasePage):

    locators = SelectableLocators()

    def check_clicked_elements(self, locator):
        elements = self.elements_are_present(locator)
        return [element.text for element in elements]

    def click_random_element(self, locator):
        elements = self.elements_are_present(locator)

        count = random.randint(4, 8)

        while count != 0:
            element = elements[random.randint(0, 3)]

            if count > 0:
                element.click()
                count -= 1

            else:
                break

    def check_selectable(self):
        self.click_random_element(self.locators.LIST_ELEMENTS)
        check_clicked_list_elements = self.check_clicked_elements(self.locators.LIST_ACTIVE_ELEMENTS)

        self.element_is_visible(self.locators.GRID_PAGE).click()
        self.click_random_element(self.locators.GRID_ELEMENTS)
        check_clicked_grid_elements = self.check_clicked_elements(self.locators.GRID_ACTIVE_ELEMENTS)

        return len(check_clicked_list_elements), len(check_clicked_grid_elements)
