import random

from locators.interactions_locators import SortableLocators
from pages.base_page import BasePage


class SortablePage(BasePage):

    locators = SortableLocators()

    def get_order_of_numbers(self, locator):
        numbers_list = self.elements_are_present(locator)
        return [number.text for number in numbers_list]

    def get_number(self, locator):
        numbers_list = self.elements_are_present(locator)
        return [number for number in numbers_list][random.randint(0, 5)]

    def move_number_sortable_list(self):
        order_of_numbers_before = self.get_order_of_numbers(self.locators.NUMBERS_LIST)
        self.action_drag_and_drop(self.get_number(self.locators.NUMBERS_LIST), self.get_number\
                                                                                        (self.locators.NUMBERS_LIST))
        order_of_numbers_after = self.get_order_of_numbers(self.locators.NUMBERS_LIST)

        return order_of_numbers_before, order_of_numbers_after

    def move_number_sortable_grid(self):
        self.element_is_visible(self.locators.GRID_PAGE).click()

        order_of_numbers_before = self.get_order_of_numbers(self.locators.GRID_LIST)
        self.action_drag_and_drop(self.get_number(self.locators.GRID_LIST), self.get_number(self.locators.GRID_LIST))
        order_of_numbers_after = self.get_order_of_numbers(self.locators.GRID_LIST)

        return order_of_numbers_before, order_of_numbers_after