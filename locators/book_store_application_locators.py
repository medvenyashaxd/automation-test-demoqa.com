from selenium.webdriver.common.by import By


class BookStoreApplicationLocators:
    # login
    USER_NAME = (By.CSS_SELECTOR, 'div #userName')
    PASSWORD = (By.CSS_SELECTOR, 'div #password')
    LOGIN = (By.CSS_SELECTOR, 'div #login')

    # profile
    SEARCH_BOOK = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    GO_TO_BOOK_STORE = (By.CSS_SELECTOR, 'div #gotoStore')

    BOOK_TITLE_CLICK = (By.CSS_SELECTOR, 'span[class="mr-2"]')

    ADD_TO_COLLECTION = (By.XPATH, '//div[9]/div[2]/button')

    BACk_TO_BOOK_STORE = (By.CSS_SELECTOR, 'div [class="text-left fullButton"]')

    FIRST_DELETE_BUTTON = (By.XPATH, '//div[1]/div/div[5]/div/span')
    NOTIFICATION_DELETE_BOOK = (By.CSS_SELECTOR, 'button[id="closeSmallModal-ok"]')
    DELETE_ALL_BOOK = (By.XPATH, '//div[3]/div[3]/button')

    PROFILE_LINK = (By.XPATH, '//div[6]/div/ul/li[3]/span')
