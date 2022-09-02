import time

from pages.book_store_application_page import BookStoreApplicationPage


class TestBookApplicationStore:
    class TestLogin:
        def test_login(self, driver):
            book_store = BookStoreApplicationPage(driver, 'https://demoqa.com/login')
            book_store.open()
            book_store.check_log_in()
            book_store.check_book_store()
