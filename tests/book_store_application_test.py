from pages.book_store_application_page import BookStoreApplicationPage


class TestBookApplicationStore:
    class TestLogin:
        def test_book_store_application(self, driver):
            book_store = BookStoreApplicationPage(driver, 'https://demoqa.com/login')
            book_store.open()
            book_store.check_log_in()
            book_store.check_book_store()
            alert_delete_book_text, alert_delete_all_book_text = book_store.check_delete_book()

            assert alert_delete_book_text == 'Book deleted.', 'book not found or deleted'
            assert alert_delete_all_book_text == 'All Books deleted.', 'books not found or deleted'
