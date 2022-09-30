import random
import time

import allure

from generator_data.generator import generator_book
from locators.book_store_application_locators import BookStoreApplicationLocators
from pages.base_page import BasePage
from data.login_info import LoginInfo


class BookStoreApplicationPage(BasePage):

    login_info = LoginInfo()
    locators = BookStoreApplicationLocators()

    @allure.step('Do log in')
    def check_log_in(self, locator=locators, login=login_info):
        with allure.step('Filling in the login fields'):
            self.element_is_present(locator.USER_NAME).send_keys(login.LOGIN)
            self.element_is_present(locator.PASSWORD).send_keys(login.PASSWORD)

        with allure.step('press the login button'):
            self.element_is_visible(locator.BUTTON_LOGIN).click()

    @allure.step('Check book store')
    def check_book_store(self, locator=locators):

        with allure.step('Clicks the button to go to the store'):
            self.element_is_present(locator.GO_TO_BOOK_STORE).click()

        with allure.step('Set the number of books to search'):
            count = 2

        while count != 0:
            if count > 0:
                book = random.sample(next(generator_book()).book, k=1)

                with allure.step('Insert the generated book into the search'):
                    self.element_is_present(locator.SEARCH_BOOK).clear()
                    self.element_is_present(locator.SEARCH_BOOK).send_keys(book)

                with allure.step('Click on the found book to go to the store'):
                    self.element_is_present(locator.BOOK_TITLE_CLICK).click()

                with allure.step('Add book to collection'):
                    self.element_is_visible(locator.ADD_TO_COLLECTION).click()

                with allure.step('Switch to alert and click accept'):
                    selected_alert = self.switch_to_alert()
                    selected_alert.accept()

                self.element_is_present(locator.BACk_TO_BOOK_STORE).click()
                count -= 1

            else:
                break

    @allure.step('Check delete book')
    def check_delete_book(self, locator=locators):
        self.go_to_element(self.element_is_present(locator.PROFILE_LINK))
        self.element_is_present(locator.PROFILE_LINK).click()
        self.element_is_visible(locator.FIRST_DELETE_BUTTON).click()
        self.element_is_visible(locator.NOTIFICATION_DELETE_BOOK).click()

        alert_delete_book = self.switch_to_alert()
        time.sleep(0.3)
        alert_delete_book_text = alert_delete_book.text
        alert_delete_book.accept()

        self.element_is_present(locator.DELETE_ALL_BOOK).click()
        self.element_is_visible(locator.NOTIFICATION_DELETE_BOOK).click()

        alert_delete_all_book = self.switch_to_alert()
        time.sleep(0.3)
        alert_delete_all_book_text = alert_delete_book.text
        alert_delete_all_book.accept()

        return alert_delete_book_text, alert_delete_all_book_text
