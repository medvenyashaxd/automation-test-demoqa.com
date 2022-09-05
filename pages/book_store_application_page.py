import random
import time

from generator_data.generator import generator_book
from locators.book_store_application_locators import BookStoreApplicationLocators
from pages.base_page import BasePage


class BookStoreApplicationPage(BasePage):
    locators = BookStoreApplicationLocators()

    def check_log_in(self):
        self.element_is_present(self.locators.USER_NAME).send_keys('medvenyasha')
        self.element_is_present(self.locators.PASSWORD).send_keys('dk4r29v#frvDmrK')
        self.element_is_visible(self.locators.LOGIN).click()

    def check_book_store(self):
        self.element_is_present(self.locators.GO_TO_BOOK_STORE).click()

        count = 2
        while count != 0:
            if count > 0:
                book = random.sample(next(generator_book()).book, k=1)
                self.element_is_present(self.locators.SEARCH_BOOK).send_keys(book)

                self.element_is_present(self.locators.BOOK_TITLE_CLICK).click()

                self.element_is_present(self.locators.ADD_TO_COLLECTION).click()

                time.sleep(1)
                selected_alert = self.switch_to_alert()
                selected_alert.accept()

                self.element_is_visible(self.locators.BACk_TO_BOOK_STORE).click()
                count -= 1

            else:
                self.element_is_present(self.locators.PROFILE_LINK).click()
                break

    def check_delete_book(self):
        self.element_is_present(self.locators.PROFILE_LINK).click()
        self.element_is_visible(self.locators.FIRST_DELETE_BUTTON).click()
        self.element_is_present(self.locators.NOTIFICATION_DELETE_BOOK).click()

        time.sleep(1)
        alert_delete_book = self.switch_to_alert()
        alert_delete_book_text = alert_delete_book.text
        alert_delete_book.accept()

        self.element_is_present(self.locators.DELETE_ALL_BOOK).click()
        self.element_is_present(self.locators.NOTIFICATION_DELETE_BOOK).click()

        time.sleep(1)
        alert_delete_all_book = self.switch_to_alert()
        alert_delete_all_book_text = alert_delete_book.text
        alert_delete_all_book.accept()

        return alert_delete_book_text, alert_delete_all_book_text
