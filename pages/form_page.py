import os
import random
import time
import allure

from generator_data.generator import generator_info, generator_subject
from locators.practice_form_locators import PracticeFormLocators
from pages.base_page import BasePage


class PracticeFormPage(BasePage):

    locators = PracticeFormLocators()

    @allure.step('Fill all fields')
    def fill_fields(self, locator=locators):

        with allure.step('Expand the page and iterate through the elements to see the subscribe button'):
            self.element_is_visible(locator.ELEMENTS_CLICK).click()
            elements = self.elements_are_visible(locator.GO_ELEMENTS)
            for element in elements:
                self.go_to_element(element)

        with allure.step('Fill in the fields using the faker generator'):
            info = next(generator_info())
            self.element_is_visible(locator.FIRST_NAME).send_keys(info.first_name)
            self.element_is_visible(locator.LAST_NAME).send_keys(info.last_name)
            self.element_is_visible(locator.EMAIL).send_keys(info.email)
            self.element_is_visible(locator.GENDER).click()
            self.element_is_visible(locator.MOBILE_NUMBER).send_keys(info.mobile_number)

        self.element_is_visible(locator.DATE_OF_BIRTH).click()
        self.random_choice_date()
        time.sleep(1)
        self.press_enter()

        with allure.step('Through a random sample, we pull out the subject from the generator in one amount and fill\
                        in the field'):
            self.element_is_visible(locator.SUBJECT).send_keys(random.sample(next(generator_subject()).subject, k=1))
            time.sleep(1)
            self.press_enter()

        with allure.step('Random click hobbies button'):
            self.element_is_visible(locator.HOBBIES).click()

        with allure.step('Create a file and upload to the site'):
            path = fr'C:\Users\xmedv\PycharmProjects\automation-test-demoqa.com\pages{random.randint(1, 10)}.txt'
            file = open(path, 'w')
            file.write(f'qwert{random.randint(1, 100)}')
            file.close()
            self.element_is_visible(locator.UPLOAD_FILE).send_keys(path)

        with allure.step('Delete file'):
            os.remove(path)

        with allure.step('Fill in the country and city fields'):
            self.element_is_visible(locator.CURRENT_ADDRESS).send_keys(info.current_address)
            self.element_is_visible(locator.STATE).click()
            self.random_choice_location()
            self.press_enter()

            self.element_is_visible(locator.CITY).click()
            self.random_choice_location()
            self.press_enter()

        with allure.step('Click button submit'):
            self.element_is_visible(locator.SUBMIT).click()

        return info

    @allure.step('Check submitting form')
    def check_submitting_form(self, locator=locators):

        with allure.step('Put all the data in a list'):
            info_in_table = self.elements_are_visible(locator.INFO_IN_TABLE)

            info = []
            for attribute in info_in_table:
                self.go_to_element(attribute)
                info.append(attribute.text)

        with allure.step('Click close button'):
            self.element_is_visible(locator.CLOSE).click()

        return info
