import base64
import os
import random
import time
import allure
import requests

from selenium.common import TimeoutException
from generator_data.generator import generator_info
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators, \
    WebTablesLocators, ButtonsLocators, LinksLocators, BrokenLinksImagesLocators, UpLoadAndDownLoadLocators, \
    DynamicPropertiesLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    @allure.step('Fill all fields')
    def fill_form_fields(self):

        with allure.step('Through the faker generator we create data about a person and fill in the fields'):
            info = next(generator_info())
            self.element_is_visible(self.locators.FULL_MAME).send_keys(info.full_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(info.email)
            self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(info.current_address)
            self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(info.permanent_address)

            with allure.step('click submit and return info person'):

                self.element_is_visible(self.locators.SUBMIT).click()

        return [info.full_name, info.email]

    @allure.step('Check the completed form split the text and return at the first index')
    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]

        return[full_name, email]


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    @allure.step('Open full list')
    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('Click random box')
    def click_random_checkbox(self):
        elements_list = self.elements_are_visible(self.locators.ELEMENTS_LIST)
        count = 15

        while count != 0:
            element = elements_list[random.randint(1, 15)]

            if count > 0:
                self.go_to_element(element)
                element.click()
                count -= 1

            else:
                break

    @allure.step('Put the checked boxes into the list and take the text')
    def check_checked_box(self):
        check_elements = self.elements_are_present(self.locators.CHECK_LIST)
        list_check = []

        for check in check_elements:
            element = check.find_element('xpath', self.locators.CHECK_ELEMENT_CLICK)
            list_check.append(element.text)

        return list_check

    @allure.step('Put the checked text into the list and take the text')
    def get_check_checked_box(self):
        checked_elements = self.elements_are_present(self.locators.OUTPUT_CHECK_LIST)
        list_check = []

        for checked_text in checked_elements:
            list_check.append(checked_text.text)

        return list_check


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    @allure.step('Click radio Button. if click true return True, if click not true return False')
    def click_radio_button(self, element):
        elements = {'yes': self.locators.RADIO_BUTTON_YES,
                    'impressive': self.locators.RADIO_BUTTON_IMPRESSIVE,
                    'no': self.locators.RADIO_BUTTON_NO}

        try:
            self.element_is_visible(elements[element]).click()

            return True

        except TimeoutException:

            return False

    @allure.step('get text from button')
    def get_output_text_button(self):
        return self.element_is_present(self.locators.CHECK_RADIO_BUTTON).text


class WebTablesPage(BasePage):
    locators = WebTablesLocators()

    @allure.step('Through the faker generator we create data about a person and fill in the fields')
    def click_add_and_fill_form(self, count):
        while count != 0:
            person_info = next(generator_info())
            first = person_info.first_name
            last = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            if count > 0:
                self.element_is_visible(self.locators.BUTTON_ADD).click()
                self.element_is_visible(self.locators.FIRST_NAME).send_keys(first)
                self.element_is_visible(self.locators.LAST_NAME).send_keys(last)
                self.element_is_visible(self.locators.EMAIL).send_keys(email)
                self.element_is_visible(self.locators.AGE).send_keys(age)
                self.element_is_visible(self.locators.SALARY).send_keys(salary)
                self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
                self.element_is_visible(self.locators.BUTTON_SUBMIT).click()
                count -= 1

            else:
                break

            return [first, last, str(age), email, str(salary), department]

    @allure.step('Verification of the data filled in by the faker')
    def check_web_table(self):
        persons = self.elements_are_present(self.locators.TABLE_PERSON)
        persons_info = []

        for person in persons:
            persons_info.append(person.text.splitlines())

        return persons_info

    @allure.step('Search for a person in the table')
    def filling_search(self, type_to_search):
        time.sleep(1)
        return self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(type_to_search)

    @allure.step('Take the found data')
    def check_filling_search(self):
        delete_button = self.element_is_visible(self.locators.BUTTON_DELETE)
        row = delete_button.find_element('xpath', self.locators.ROW)

        return row.text.splitlines()

    @allure.step('Create information through the generator, click on change data, clear the data in the age field and\
                 insert new ones')
    def check_edit_info(self):
        with allure.step('Create information through the generator'):
            person_info = next(generator_info())

        with allure.step('click on change data, clear the data in the age field'):
            self.element_is_visible(self.locators.EDIT_BUTTON).click()
            self.element_is_visible(self.locators.INPUT_AGE).clear()

        with allure.step('Insert new ones data'):
            new_age = person_info.age
            self.element_is_visible(self.locators.INPUT_AGE).send_keys(new_age)
            self.element_is_visible(self.locators.BUTTON_SUBMIT).click()

        return str(new_age)

    @allure.step('Delete info and check')
    def delete_info_and_check(self):
        with allure.step('Delete info in table'):
            self.element_is_visible(self.locators.BUTTON_DELETE).click()

        with allure.step('Return text no rows found'):
            return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    @allure.step('Page rows edit')
    def page_rows_edit(self):
        with allure.step('Change the data in the selected rows'):
            self.element_is_present(self.locators.SELECT_ROWS).click()
            self.element_is_present(self.locators.ROWS5).click()
            self.element_is_present(self.locators.SELECT_ROWS).click()
            self.element_is_present(self.locators.ROWS10).click()
            self.element_is_present(self.locators.SELECT_ROWS).click()
            self.element_is_present(self.locators.ROWS20).click()
            elements = self.elements_are_present(self.locators.TABLE_PERSON)

        with allure.step('Move to line selection'):
            for element in elements:
                self.go_to_element(element)

        with allure.step('Click on line selection'):
            self.element_is_present(self.locators.SELECT_ROWS).click()

        with allure.step('Click line rows 25'):
            self.element_is_visible(self.locators.ROWS25).click()


class ButtonsPage(BasePage):
    locators = ButtonsLocators()

    @allure.step('The function gets the click type and performs action')
    def click_button(self, click):
        if click == 'double':
            self.double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_ME))

            return self.check_click(self.locators.DONE_A_DOUBLE_CLICK)

        elif click == 'right':
            self.right_click(self.element_is_visible(self.locators.RIGHT_CLICK_ME))

            return self.check_click(self.locators.DONE_A_RIGHT_CLICK)

        elif click == 'click':
            self.element_is_visible(self.locators.CLICK_ME).click()

            return self.check_click(self.locators.DONE_A_DYNAMIC_CLICK)

    @allure.step('Check click')
    def check_click(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksLocators()

    @allure.step('Check the link status code')
    def check_link_opened_in_new_tab(self, button):
        buttons = {'home':
                   {'button': self.locators.SIMPLE_LINK},

                   'home_random_id':
                       {'button': self.locators.DYNAMIC_LINK}
                   }

        link = self.element_is_present(buttons[button]['button'])
        href_link = link.get_attribute('href')
        request = requests.get(href_link)

        if request.status_code == 200:
            link.click()
            self.switch_to_window(1)
            url = self.driver.current_url
            self.switch_to_window(0)

            return [url, request.status_code]

        else:

            return [href_link, request.status_code]

    @allure.step('Check link status code')
    def check_link(self, url, button):
        buttons = {'created':
                   {'button': self.locators.CREATED_LINK},

                   'no_content':
                       {'button': self.locators.CONTENT_LINK},

                   'moved':
                       {'button': self.locators.BAD_REQUEST},

                   'not_found':
                       {'button': self.locators.NOT_FOUND}
                   }

        request = requests.get(url)

        if request.status_code == 200:
            self.element_is_visible(buttons[button]['button']).click()

        else:
            return request.status_code


class BrokenLinksImagesPage(BasePage):
    locators = BrokenLinksImagesLocators()

    @allure.step('Check link status code')
    def check_link(self, url, link):
        links = {'valid_link':
                 {'button': self.locators.VALID_LINK},

                 'broken_link':
                     {'button': self.locators.BROKEN_LINK},
                 }

        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(links[link]['button']).click()

            return request.status_code

        else:

            return request.status_code


class UpLoadAndDownLoadPage(BasePage):
    locators = UpLoadAndDownLoadLocators()

    @allure.step('Check download file and remove')
    def download_file(self):

        with allure.step('get href attribute and decode file'):
            link = self.element_is_present(self.locators.DOWNLOAD_BUTTON).get_attribute('href').split(',')
            link_b = base64.b64decode(link[1])

        path = fr'C:\Users\xmedv\PycharmProjects\Quality-assurance-tests\tests\SomeImgFile{random.randint(1, 10)}.txt'
        with open(path, 'wb+') as f:
            f.write(link_b)
            check_file = os.path.exists(path)
            f.close()
        os.remove(path)

        return check_file

    @allure.step('Check upload file')
    def upload_file(self):
        path = fr'C:\Users\xmedv\PycharmProjects\Quality-assurance-tests\tests\SomeImgFile{random.randint(1, 10)}.txt'
        file = open(path, 'w')
        file.write(f'qwert{random.randint(1, 100)}')
        file.close()

        self.element_is_present(self.locators.SELECT_A_FILE).send_keys(path)
        check_file = self.element_is_present(self.locators.UPLOADED_FILE_PATH).text
        os.remove(path)

        return check_file.split('\\')[-1], path.split('\\')[-1]


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesLocators()

    @allure.step('Get text with element random id')
    def check_text_with_random_id(self):
        check_text = self.element_is_visible(self.locators.TEXT_WITH_RANDOM_ID).text

        return check_text

    @allure.step('Check_enable_button')
    def check_enable_button_after_5_second(self):
        try:
            self.element_is_clickable(self.locators.WILL_ENABLE_5_SECONDS_BUTTON)

            return True

        except TimeoutException:

            return False

    @allure.step('Check change color')
    def check_change_color(self):
        default_color = self.element_is_visible(self.locators.COLOR_CHANGE_BUTTON)
        change_color = default_color.value_of_css_property('color')
        return change_color

    @allure.step('Check button')
    def check_visible_button_after_5_second(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_5_SECONDS)

            return True

        except TimeoutException:

            return False
