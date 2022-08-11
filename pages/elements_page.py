import os
import random
import requests
from generator.person_generator import generator_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonLocators, \
    WebTablesLocators, ButtonsLocators, LinksLocators, BrokenLinksImages, UpLoadAndDownload
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

    def check_checked_box(self):
        check_elements = self.elements_are_present(self.locators.CHECK_LIST)
        list_check = []
        for check in check_elements:
            element = check.find_element('xpath', self.locators.CHECK_ELEMENT_CLICK)
            list_check.append(element.text)
        return list_check

    def get_check_checked_box(self):
        output_elements = self.elements_are_present(self.locators.OUTPUT_CHECK_LIST)
        list_check = []
        for check in output_elements:
            list_check.append(check.text)
        return list_check


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def click_radio_button(self, element):
        elements = {'yes': self.locators.RADIO_BUTTON_YES,
                    'impressive': self.locators.RADIO_BUTTON_IMPRESSIVE}
        self.element_is_visible(elements[element]).click()

    def output_text_button(self):
        return self.element_is_present(self.locators.CHECK_RADIO_BUTTON).text


class WebTablesPage(BasePage):
    locators = WebTablesLocators()

    def click_add_and_fill_form(self, count):
        while count != 0:
            person_info = next(generator_person())
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

    def check_web_table(self):
        persons = self.elements_are_present(self.locators.TABLE_PERSON)
        persons_info = []
        for person in persons:
            persons_info.append(person.text.splitlines())
        return persons_info

    def filling_search(self, type_to_search):
        return self.element_is_visible(self.locators.SEARCH_FIELD).send_keys(type_to_search)

    def check_filling_search(self):
        delete_button = self.element_is_visible(self.locators.BUTTON_DELETE)
        row = delete_button.find_element('xpath', self.locators.ROW)
        return row.text.splitlines()

    def check_edit_info(self):
        person_info = next(generator_person())
        self.element_is_visible(self.locators.EDIT_BUTTON).click()
        self.element_is_visible(self.locators.INPUT_AGE).clear()
        new_age = person_info.age
        self.element_is_visible(self.locators.INPUT_AGE).send_keys(new_age)
        self.element_is_visible(self.locators.BUTTON_SUBMIT).click()
        return str(new_age)

    def delete_info_and_check(self):
        self.element_is_visible(self.locators.BUTTON_DELETE).click()
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def page_rows_edit(self):
        self.element_is_present(self.locators.SELECT_ROWS).click()
        self.element_is_present(self.locators.ROWS5).click()
        self.element_is_present(self.locators.SELECT_ROWS).click()
        self.element_is_present(self.locators.ROWS10).click()
        self.element_is_present(self.locators.SELECT_ROWS).click()
        self.element_is_present(self.locators.ROWS20).click()
        elements = self.elements_are_present(self.locators.TABLE_PERSON)
        for element in elements:
            self.go_to_element(element)
        self.element_is_present(self.locators.SELECT_ROWS).click()
        self.element_is_visible(self.locators.ROWS25).click()


class ButtonsPage(BasePage):
    locators = ButtonsLocators()

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

    def check_click(self, element):
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksLocators()

    def check_link_in_handles(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        href_link = simple_link.get_attribute('href')
        request = requests.get(href_link)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return href_link, url
        else:
            return href_link, request.status_code

    def check_dynamic_link(self):
        dynamic_link = self.element_is_visible(self.locators.DYNAMIC_LINK)
        href_link = dynamic_link.get_attribute('href')
        request = requests.get(href_link)
        if request.status_code == 200:
            dynamic_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return href_link, url
        else:
            return href_link, request.status_code

    def check_created_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.CREATED_LINK).click()
        else:
            return request.status_code

    def check_no_content_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.CONTENT_LINK).click()
        else:
            return request.status_code

    def check_moved_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.MOVED_LINK).click()
        else:
            return request.status_code

    def check_bad_request_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code

    def check_not_found_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.NOT_FOUND).click()
        else:
            return request.status_code


class BrokenLinksImagesPage(BasePage):
    locators = BrokenLinksImages()

    def check_valid_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            elements = self.elements_are_present(self.locators.ELEMENTS)
            for element in elements:
                self.go_to_element(element)
            self.element_is_visible(self.locators.VALID_LINK).click()
            url = self.driver.current_url
            return url, request.status_code
        else:
            return url, request.status_code

    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            elements = self.elements_are_present(self.locators.ELEMENTS)
            for element in elements:
                self.go_to_element(element)
            self.element_is_visible(self.locators.BROKEN_LINK).click()
            url = self.driver.current_url
            return url, request.status_code
        else:
            return url, request.status_code

class UpLoadAndDownLoadPage(BasePage):
    locators = UpLoadAndDownload()

    def up_load_file(self):
        file = open('SomeFile.txt', 'w')
        file.write('qwer')
        self.element_is_present(self.locators.SELECT_A_FILE).send_keys(file)
        file.close()
        os.remove('SomeFile.txt')

