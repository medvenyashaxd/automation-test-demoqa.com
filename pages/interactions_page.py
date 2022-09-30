import random
import time
import allure

from locators.interactions_locators import SortableLocators, SelectableLocators, ResizableLocators, DroppableLocators, \
    DraggableLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortableLocators()

    @allure.step('Gets the order of the numbers')
    def get_order_of_numbers(self, locator):
        with allure.step('Loop through the data and add it to the list'):
            numbers_list = self.elements_are_visible(locator)
            return [number.text for number in numbers_list]

    @allure.step('Picks numbers randomly')
    def get_number(self, locator):
        numbers_list = self.elements_are_visible(locator)
        return [number for number in numbers_list][random.randint(0, 5)]

    @allure.step('Check sortable')
    def check_sortable(self, locator=locators):
        order_of_numbers_list_before = self.get_order_of_numbers(locator.NUMBERS_LIST)

        with allure.step('Move the numbers'):
            self.action_drag_and_drop(self.get_number(locator.NUMBERS_LIST), self.get_number(locator.NUMBERS_LIST))

        order_of_numbers_list_after = self.get_order_of_numbers(locator.NUMBERS_LIST)

        with allure.step('Go to grid tab'):
            self.element_is_visible(locator.GRID_PAGE).click()

        order_of_numbers_grid_before = self.get_order_of_numbers(locator.GRID_LIST)

        with allure.step('Move the numbers'):
            self.action_drag_and_drop(self.get_number(locator.GRID_LIST), self.get_number(locator.GRID_LIST))
        order_of_numbers_grid_after = self.get_order_of_numbers(locator.GRID_LIST)

        return order_of_numbers_list_before, order_of_numbers_list_after, order_of_numbers_grid_before, \
               order_of_numbers_grid_after


class SelectablePage(BasePage):
    locators = SelectableLocators()

    @allure.step('Takes the name from the button')
    def check_clicked_elements(self, locator):
        elements = self.elements_are_visible(locator)
        time.sleep(0.3)
        return [element.text for element in elements]

    @allure.step('Click random element')
    def click_random_element(self, locator):
        elements = self.elements_are_visible(locator)

        count = random.randint(4, 8)

        while count != 0:
            element = elements[random.randint(0, 3)]

            if count > 0:
                element.click()
                count -= 1
                time.sleep(0.3)

            else:
                break

    @allure.step('Check selectable')
    def check_selectable(self, locator=locators):
        self.click_random_element(locator.LIST_ELEMENTS)
        time.sleep(0.3)
        check_clicked_list_elements = self.check_clicked_elements(locator.LIST_ACTIVE_ELEMENTS)

        with allure.step('Switch to grid tab'):
            self.element_is_visible(locator.GRID_PAGE).click()
        self.click_random_element(locator.GRID_ELEMENTS)
        check_clicked_grid_elements = self.check_clicked_elements(locator.GRID_ACTIVE_ELEMENTS)

        return len(check_clicked_list_elements), len(check_clicked_grid_elements)


class ResizablePage(BasePage):
    locators = ResizableLocators()

    @allure.step('Get size')
    def get_size(self, locator):
        return [self.element_is_present(locator).get_attribute('style')]

    @allure.step('Drags around the corner to the desired coordinates')
    def move_arrow(self, locator, x, y):
        self.action_drag_and_drop_by_offset(self.element_is_visible(locator), x, y)

    @allure.step('Change size')
    def change_size(self, locator=locators):
        time.sleep(1)
        self.move_arrow(locator.RESIZABLE_BOX_ARROW, 600, 400)
        box_check_one = self.get_size(locator.GET_SIZE_BOX)

        self.move_arrow(locator.RESIZABLE_BOX_ARROW, -550, -450)
        box_check_two = self.get_size(locator.GET_SIZE_BOX)

        self.go_to_element(self.element_is_visible(locator.GET_SIZE_OUT_BOX))
        self.move_arrow(locator.RESIZABLE_BOX_OUT_ARROW, 150, 150)
        check_box_out = self.get_size(locator.GET_SIZE_OUT_BOX)

        return box_check_one, box_check_two, check_box_out


class DroppablePage(BasePage):
    locators = DroppableLocators()

    @allure.step('Get text')
    def get_text(self, locator):
        return self.element_is_visible(locator).text

    @allure.step('Move element to target')
    def move_to_target(self, element, target):
        self.action_drag_and_drop(self.element_is_visible(element), self.element_is_visible(target))

    @allure.step('Check droppable')
    def check_droppable(self, locator=locators):
        with allure.step('Move element to target and get text in a container'):
            self.move_to_target(locator.SIMPLE_DRAGGABLE, locator.SIMPLE_DROP_HERE)
            text_simple_droppable = self.get_text(locator.SIMPLE_TEXT)

        with allure.step('switch to the accept tab'):
            self.element_is_visible(locator.ACCEPT_PAGE).click()

        with allure.step('Move element to target and get text in a container'):
            self.move_to_target(locator.NOT_ACCEPTABLE_NOTIFICATION, locator.ACCEPTABLE_DROP_HERE)
            self.move_to_target(locator.ACCEPTABLE_NOTIFICATION, locator.ACCEPTABLE_DROP_HERE)
            text_acceptable_droppable = self.get_text(locator.ACCEPTABLE_TEXT)

        with allure.step('not Greedy container test'):
            self.element_is_visible(locator.PREVENT_PROPAGATION_PAGE).click()
            self.move_to_target(locator.DRAG_ME_PREVENT, locator.NOT_GREEDY_BOX)
            not_greedy_box_text = self.get_text(locator.TEXT_NOT_GREEDY_BOX)
            not_greedy_text = self.get_text(locator.TEXT_NOT_GREEDY)

        with allure.step('Greedy container test'):
            self.move_to_target(locator.DRAG_ME_PREVENT, locator.GREEDY_BOX)
            greedy_box_text = self.get_text(locator.GREEDY_BOX_TEXT)
            greedy_text = self.get_text(locator.GREEDY_TEXT)

        with allure.step('Go to revert draggable tab'):
            self.element_is_visible(locator.REVERT_DRAG_ME_PAGE).click()

        with allure.step('Check revert box'):
            self.move_to_target(locator.WILL_REVERT, locator.DROP_HERE_REVERT_BOX)

        with allure.step('Check not revert box'):
            self.move_to_target(locator.NOT_REVERT, locator.DROP_HERE_REVERT_BOX)
            self.move_to_target(locator.NOT_REVERT, locator.WILL_REVERT)

        return text_simple_droppable, text_acceptable_droppable, not_greedy_box_text, not_greedy_text, greedy_box_text, \
               greedy_text


class DraggablePage(BasePage):
    locators = DraggableLocators()

    @allure.step('Move to x and y coordinates')
    def move_to_x_y(self, locator, x, y):
        self.action_drag_and_drop_by_offset(self.element_is_present(locator), x, y)

    @allure.step('Get element attribute')
    def get_element_attribute(self, element):
        attribute = self.element_is_present(element).get_attribute('style')
        return attribute

    @allure.step('Check draggable')
    def check_draggable(self, locator=locators):
        with allure.step('Moving a simple box'):
            self.move_to_x_y(locator.DRAG_ME_SIMPLE, 30, 50)

        attribute_simple = self.get_element_attribute(locator.DRAG_ME_SIMPLE)

        with allure.step('Switch to tab axis restricted'):
            self.element_is_visible(locator.AXIS_RESTRICTED_TAB).click()

        with allure.step('Move a box that only moves in x coordinates'):
            self.move_to_x_y(locator.BOX_ONLY_X, 50, 0)
        attribute_restricted_x = self.get_element_attribute(locator.BOX_ONLY_X)

        with allure.step('Move a box that only moves in y coordinates'):
            self.move_to_x_y(locator.BOX_ONLY_Y, 0, 100)
        attribute_restricted_y = self.get_element_attribute(locator.BOX_ONLY_Y)

        with allure.step('Switch to tab container restricted tab'):
            self.element_is_visible(locator.CONTAINER_RESTRICTED_TAB).click()

        with allure.step('Moving a container within a container'):
            self.move_to_x_y(locator.BOX_WITHIN_CONTAINER, 120, 15)
        attribute_box_in_container = self.get_element_attribute(locator.BOX_WITHIN_CONTAINER)

        with allure.step('Moving a box parent container'):
            self.move_to_x_y(locator.BOX_PARENT_CONTAINER, 5, 45)
        attribute_box_parent_container = self.get_element_attribute(locator.BOX_PARENT_CONTAINER)

        return attribute_simple, attribute_restricted_x, attribute_restricted_y, attribute_box_in_container, \
               attribute_box_parent_container
