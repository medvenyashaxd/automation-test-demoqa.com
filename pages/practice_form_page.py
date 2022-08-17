import os
import random
import time
from generator_data.generator import generator_info, generator_subject
from locators.practice_form_locators import PracticeFormLocators
from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    locators = PracticeFormLocators()

    def fill_fields(self):
        self.element_is_visible(self.locators.ELEMENTS_CLICK).click()
        elements = self.elements_are_visible(self.locators.GO_ELEMENTS)
        for element in elements:
            self.go_to_element(element)

        info = next(generator_info())
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(info.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(info.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(info.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE_NUMBER).send_keys(info.mobile_number)

        self.element_is_visible(self.locators.DATE_OF_BIRTH).click()
        self.random_choice_date()
        time.sleep(1)
        self.press_enter()

        self.element_is_visible(self.locators.SUBJECT).send_keys(generator_subject())
        time.sleep(1)
        self.press_enter()

        self.element_is_visible(self.locators.HOBBIES).click()
        time.sleep(1)

        path = fr'C:\Users\xmedv\PycharmProjects\Quality-assurance-tests\pages{random.randint(1, 10)}.txt'
        file = open(path, 'w')
        file.write(f'qwert{random.randint(1, 100)}')
        file.close()
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)

        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(info.current_address)
        self.element_is_visible(self.locators.STATE).click()
        self.random_choice_location()
        self.press_enter()

        self.element_is_visible(self.locators.CITY).click()
        self.random_choice_location()
        self.press_enter()

        self.element_is_visible(self.locators.SUBMIT).click()
        return info

    def check_submitting_form(self):
        info_in_table = self.elements_are_present(self.locators.INFO_IN_TABLE)

        info = []
        for attribute in info_in_table:
            self.go_to_element(attribute)
            info.append(attribute.text)

        self.element_is_visible(self.locators.CLOSE).click()
        return info
