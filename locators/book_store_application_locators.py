from selenium.webdriver.common.by import By


class BookStoreApplicationLocators:
    # login
    USER_NAME = (By.CSS_SELECTOR, 'div #userName')
    PASSWORD = (By.CSS_SELECTOR, 'div #password')
    LOGIN = (By.CSS_SELECTOR, 'div #login')

    # profile
    SEARCH_BOOK = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    PROFILE_PAGE = (By.XPATH, '//div[2]/div/label/a')
    GO_TO_BOOK_STORE = (By.CSS_SELECTOR, 'div #gotoStore')
    DELETE_ALL_BOOK = (By.XPATH, '//div[3]/div[3]/button')

    BOOK_TITLE_CLICK = (By.CSS_SELECTOR, 'span[class="mr-2"]')

    ADD_TO_COLLECTION = (By.XPATH, '//div[9]/div[2]/button')