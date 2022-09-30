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
    def fill_form_fields(self, locator=locators):

        with allure.step('Through the faker generator we create data about a person and fill in the fields'):
            info = next(generator_info())
            self.element_is_visible(locator.FULL_MAME).send_keys(info.full_name)
            self.element_is_visible(locator.EMAIL).send_keys(info.email)
            self.element_is_visible(locator.CURRENT_ADDRESS).send_keys(info.current_address)
            self.element_is_visible(locator.PERMANENT_ADDRESS).send_keys(info.permanent_address)

            with allure.step('click submit and return info person'):

                self.element_is_visible(locator.SUBMIT).click()

        return [info.full_name, info.email]

    @allure.step('Check the completed form split the text and return at the first index')
    def check_filled_form(self, locator=locators):
        full_name = self.element_is_present(locator.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(locator.CREATED_EMAIL).text.split(':')[1]

        return[full_name, email]


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    @allure.step('Open full list')
    def open_full_list(self, locator=locators):
        self.element_is_visible(locator.EXPAND_ALL_BUTTON).click()

    @allure.step('Click random box')
    def click_random_checkbox(self, locator=locators):
        elements_list = self.elements_are_visible(locator.ELEMENTS_LIST)
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
    def check_checked_box(self, locator=locators):
        check_elements = self.elements_are_present(locator.CHECK_LIST)
        list_check = []

        for check in check_elements:
            element = check.find_element('xpath', locator.CHECK_ELEMENT_CLICK)
            list_check.append(element.text)

        return list_check

    @allure.step('Put the checked text into the list and take the text')
    def get_check_checked_box(self, locator=locators):
        checked_elements = self.elements_are_present(locator.OUTPUT_CHECK_LIST)
        list_check = []

        for checked_text in checked_elements:
            list_check.append(checked_text.text)

        return list_check


class RadioButtonPage(BasePage):

    locators = RadioButtonLocators()

    @allure.step('Click radio Button. if click true return True, if click not true return False')
    def click_radio_button(self, element, locator=locators):
        elements = {'yes': locator.RADIO_BUTTON_YES,
                    'impressive': locator.RADIO_BUTTON_IMPRESSIVE,
                    'no': locator.RADIO_BUTTON_NO}

        try:
            self.element_is_visible(elements[element]).click()

            return True

        except TimeoutException:

            return False

    @allure.step('get text from button')
    def get_output_text_button(self, locator=locators):
        return self.element_is_present(locator.CHECK_RADIO_BUTTON).text


class WebTablesPage(BasePage):

    locators = WebTablesLocators()

    @allure.step('Through the faker generator we create data about a person and fill in the fields')
    def click_add_and_fill_form(self, count, locator=locators):
        while count != 0:
            person_info = next(generator_info())
            first = person_info.first_name
            last = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            if count > 0:
                self.element_is_visible(locator.BUTTON_ADD).click()
                self.element_is_visible(locator.FIRST_NAME).send_keys(first)
                self.element_is_visible(locator.LAST_NAME).send_keys(last)
                self.element_is_visible(locator.EMAIL).send_keys(email)
                self.element_is_visible(locator.AGE).send_keys(age)
                self.element_is_visible(locator.SALARY).send_keys(salary)
                self.element_is_visible(locator.DEPARTMENT).send_keys(department)
                self.element_is_visible(locator.BUTTON_SUBMIT).click()
                count -= 1

            else:
                break

            return [first, last, str(age), email, str(salary), department]

    @allure.step('Verification of the data filled in by the faker')
    def check_web_table(self, locator=locators):
        persons = self.elements_are_visible(locator.TABLE_PERSON)
        persons_info = []

        for person in persons:
            time.sleep(0.4)
            persons_info.append(person.text.splitlines())

        return persons_info

    @allure.step('Search for a person in the table')
    def filling_search(self, type_to_search, locator=locators):
        self.element_is_visible(locator.SEARCH_FIELD).click()
        return self.element_is_visible(locator.SEARCH_FIELD).send_keys(type_to_search)

    @allure.step('Take the found data')
    def check_filling_search(self, locator=locators):
        delete_button = self.element_is_visible(locator.BUTTON_DELETE)
        row = delete_button.find_element('xpath', locator.ROW)

        return row.text.splitlines()

    @allure.step('Create information through the generator, click on change data, clear the data in the age field and\
                 insert new ones')
    def check_edit_info(self, locator=locators):
        with allure.step('Create information through the generator'):
            person_info = next(generator_info())

        with allure.step('click on change data, clear the data in the age field'):
            self.element_is_visible(locator.EDIT_BUTTON).click()
            self.element_is_visible(locator.INPUT_AGE).clear()

        with allure.step('Insert new ones data'):
            new_age = person_info.age
            self.element_is_visible(locator.INPUT_AGE).send_keys(new_age)
            self.element_is_visible(locator.BUTTON_SUBMIT).click()

        return str(new_age)

    @allure.step('Delete info and check')
    def delete_info_and_check(self, locator=locators):
        with allure.step('Delete info in table'):
            self.element_is_visible(locator.BUTTON_DELETE).click()

        with allure.step('Return text no rows found'):
            return self.element_is_visible(locator.NO_ROWS_FOUND).text

    @allure.step('Page rows edit')
    def page_rows_edit(self, locator=locators):
        with allure.step('Change the data in the selected rows'):
            self.element_is_visible(locator.SELECT_ROWS).click()
            self.element_is_visible(locator.ROWS5).click()
            self.element_is_visible(locator.SELECT_ROWS).click()
            self.element_is_visible(locator.ROWS10).click()
            self.element_is_visible(locator.SELECT_ROWS).click()
            self.go_to_element(self.element_is_present(locator.SELECT_ROWS))
            self.element_is_visible(locator.ROWS20).click()

        with allure.step('Click on line selection'):
            self.element_is_visible(locator.SELECT_ROWS).click()

        with allure.step('Click line rows 25'):
            self.element_is_visible(locator.ROWS25).click()


class ButtonsPage(BasePage):

    locators = ButtonsLocators()

    @allure.step('The function gets the click type and performs action')
    def click_button(self, click, locator=locators):
        if click == 'double':
            self.double_click(self.element_is_visible(locator.DOUBLE_CLICK_ME))

            return self.check_click(locator.DONE_A_DOUBLE_CLICK)

        elif click == 'right':
            self.right_click(self.element_is_visible(locator.RIGHT_CLICK_ME))

            return self.check_click(locator.DONE_A_RIGHT_CLICK)

        elif click == 'click':
            self.element_is_visible(locator.CLICK_ME).click()

            return self.check_click(locator.DONE_A_DYNAMIC_CLICK)

    @allure.step('Check click')
    def check_click(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):

    locators = LinksLocators()

    @allure.step('Check the link status code')
    def check_link_opened_in_new_tab(self, button, locator=locators):
        buttons = {'home':
                   {'button': locator.SIMPLE_LINK},

                   'home_random_id':
                       {'button': locator.DYNAMIC_LINK}
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
    def check_link(self, url, button, locator=locators):
        buttons = {'created':
                   {'button': locator.CREATED_LINK},

                   'no_content':
                       {'button': locator.CONTENT_LINK},

                   'moved':
                       {'button': locator.BAD_REQUEST},

                   'not_found':
                       {'button': locator.NOT_FOUND}
                   }

        request = requests.get(url)

        if request.status_code == 200:
            self.element_is_visible(buttons[button]['button']).click()

        else:
            return request.status_code


class BrokenLinksImagesPage(BasePage):
    locators = BrokenLinksImagesLocators()

    @allure.step('Check link status code')
    def check_link(self, url, link, locator=locators):
        links = {'valid_link':
                 {'button': locator.VALID_LINK},

                 'broken_link':
                     {'button': locator.BROKEN_LINK},
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
    def download_file(self, locator=locators):

        with allure.step('get href attribute and decode file'):
            link = self.element_is_present(locator.DOWNLOAD_BUTTON).get_attribute('href').split(',')
            link_b = base64.b64decode(link[1])

        path = fr'C:\Users\xmedv\PycharmProjects\Quality-assurance-tests\tests\SomeImgFile{random.randint(1, 10)}.txt'
        with open(path, 'wb+') as f:
            f.write(link_b)
            check_file = os.path.exists(path)
            f.close()
        os.remove(path)

        return check_file

    @allure.step('Check upload file')
    def upload_file(self, locator=locators):
        path = fr'C:\Users\xmedv\PycharmProjects\Quality-assurance-tests\tests\SomeImgFile{random.randint(1, 10)}.txt'
        file = open(path, 'w')
        file.write(f'qwert{random.randint(1, 100)}')
        file.close()

        self.element_is_present(locator.SELECT_A_FILE).send_keys(path)
        check_file = self.element_is_present(locator.UPLOADED_FILE_PATH).text
        os.remove(path)

        return check_file.split('\\')[-1], path.split('\\')[-1]


class DynamicPropertiesPage(BasePage):

    locators = DynamicPropertiesLocators()

    @allure.step('Get text with element random id')
    def check_text_with_random_id(self, locator=locators):
        check_text = self.element_is_visible(locator.TEXT_WITH_RANDOM_ID).text

        return check_text

    @allure.step('Check_enable_button')
    def check_enable_button_after_5_second(self, locator=locators):
        try:
            time.sleep(6)
            self.element_is_clickable(locator.WILL_ENABLE_5_SECONDS_BUTTON)

            return True

        except TimeoutException:

            return False

    @allure.step('Check change color')
    def check_change_color(self, locator=locators):
        default_color = self.element_is_visible(locator.COLOR_CHANGE_BUTTON)
        change_color = default_color.value_of_css_property('color')
        return change_color

    @allure.step('Check button')
    def check_visible_button_after_5_second(self, locator=locators):
        try:
            self.element_is_visible(locator.VISIBLE_AFTER_5_SECONDS)

            return True

        except TimeoutException:

            return False
