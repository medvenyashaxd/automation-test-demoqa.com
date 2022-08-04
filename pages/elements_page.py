import random

from generator.person_generator import generator_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators, \
    WebTablesLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generator_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_MAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        go_to_elements = self.elements_are_visible(self.locators.LIST_FOR_GO_TO_ELEMENT)
        for element in go_to_elements:
            self.go_to_element(element)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        elements_list = self.elements_are_visible(self.locators.ELEMENTS_LIST)
        count = 21
        while count != 0:
            element = elements_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(element)
                element.click()
                count -= 1
            else:
                break

    def check_cheked_box(self):
        check_elements = self.elements_are_present(self.locators.CHECK_LIST)
        list_check = []
        for check in check_elements:
            element = check.find_element('xpath', self.locators.CHECK_ELEMENT_CLICK)
            list_check.append(element.text)
        return list_check


    def get_check_cheked_box(self):
        output_elements = self.elements_are_present(self.locators.OUTPUT_CHECK_LIST)
        list_check = []
        for check in output_elements:
            list_check.append(check.text)
        return list_check


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_radio_button(self, element):
        elements = {'yes' : self.locators.RADIO_BUTTON_YES,
                    'impressive' : self.locators.RADIO_BUTTON_IMPRESSIVE}
        self.element_is_visible(elements[element]).click()

    def output_text_button(self):
        return self.element_is_present(self.locators.CHECK_RADIO_BUTTON).text



class WebTablesPage(BasePage):
    locators = WebTablesLocators()

    def click_add_and_fill_form(self, count):
        person_info = next(generator_person())
        first = person_info.first_name
        last = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department

        while count != 0:
            if count > 0:
                self.element_is_visible(self.locators.BUTTON_ADD).click()
                self.element_is_visible(self.locators.FIRST_NAME).send_keys(first)
                self.element_is_visible(self.locators.LAST_NAME).send_keys(last)
                self.element_is_visible(self.locators.EMAIL).send_keys(email)
                self.element_is_visible(self.locators.AGE).send_keys(age)
                self.element_is_visible(self.locators.SALARY).send_keys(salary)
                self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
                elements = self.elements_are_visible(self.locators.SCROLL_TO_ELEMENTS)
                for element in elements:
                    self.go_to_element(element)
                self.element_is_visible(self.locators.BUTTON_SUBMIT).click()
                count -= 1
            else:
                break

        return [first, last, str(age), email, str(salary), department]


    def check_web_table(self):
        persons = self.elements_are_present(self.locators.TABLE_PERSON)
        persons_info = []
        for person in persons:
            persons_info.append(person.text.splitlines())
        return persons_info
