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
        book = random.sample(next(generator_book()).book, k=1)
        self.element_is_present(self.locators.GO_TO_BOOK_STORE).click()

        self.element_is_present(self.locators.SEARCH_BOOK).send_keys(book)

        self.element_is_present(self.locators.BOOK_TITLE_CLICK).click()
        print(book)

        self.element_is_present(self.locators.ADD_TO_COLLECTION).click()