from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_MAME = (By.CSS_SELECTOR, 'input[id="userName"')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')
    LIST_FOR_GO_TO_ELEMENT = (By.CSS_SELECTOR, 'div[class="mt-2 row"]')

    CREATED_FULL_NAME = (By.CSS_SELECTOR, 'p[id="name"]')
    CREATED_EMAIL = (By.CSS_SELECTOR, 'p[id="email"]')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, 'p[id="currentAddress"]')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'p[id="permanentAddress"]')


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ELEMENTS_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECK_LIST = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    CHECK_ELEMENT_CLICK = ".//ancestor::span[@class='rct-text']"
    OUTPUT_CHECK_LIST = (By.CSS_SELECTOR, 'span[class="text-success"]')


class RadioButtonLocators:
    RADIO_BUTTON_YES = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for="yesRadio"]')
    RADIO_BUTTON_IMPRESSIVE = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for="impressiveRadio"]')
    RADIO_BUTTON_NO = (By.CSS_SELECTOR, 'input[id="noRadio"]')

    CHECK_RADIO_BUTTON = (By.CSS_SELECTOR, 'p span[class="text-success"]')


class WebTablesLocators:
    BUTTON_ADD = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT = (By.CSS_SELECTOR, 'input[id="department"]')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')
    SCROLL_TO_ELEMENTS = (By.CSS_SELECTOR, 'div[class="mt-2 row"]')

    # for table
    TABLE_PERSON = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    # xpath
    ROW = ".//ancestor::div[@class='rt-tr-group']"

    SEARCH_FIELD = (By.CSS_SELECTOR, ' input[id="searchBox"]')

    BUTTON_DELETE = (By.CSS_SELECTOR, 'span[title="Delete"]')

    EDIT_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    INPUT_AGE = (By.CSS_SELECTOR, 'input[id="age"]')

    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')

    SELECT_ROWS = (By.CSS_SELECTOR, 'span[class="select-wrap -pageSizeOptions"]')

    # edit amount rows
    ROWS5 = (By.CSS_SELECTOR, 'option[value="5"]')
    ROWS10 = (By.CSS_SELECTOR, 'option[value="10"]')
    ROWS20 = (By.CSS_SELECTOR, 'option[value="20"]')
    ROWS25 = (By.CSS_SELECTOR, 'option[value="25"]')


class ButtonsLocators:
    DOUBLE_CLICK_ME = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_ME = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME = (By.XPATH, '//div[3]/button')

    # for output
    DONE_A_DOUBLE_CLICK = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    DONE_A_RIGHT_CLICK = (By.CSS_SELECTOR, 'p[id="rightClickMessage"')
    DONE_A_DYNAMIC_CLICK = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinksLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    DYNAMIC_LINK = (By.XPATH, '//p[2]/a')
    CREATED_LINK = (By.CSS_SELECTOR, 'a[id="created"]')
    CONTENT_LINK = (By.CSS_SELECTOR, 'a[id="no-content"]')
    MOVED_LINK = (By.CSS_SELECTOR, 'a[id="moved"]')
    BAD_REQUEST = (By.CSS_SELECTOR, 'a[id="bad-request"]')
    NOT_FOUND = (By.CSS_SELECTOR, 'a[id="invalid-url"]')


class BrokenLinksImagesLocators:
    VALID_LINK = (By.XPATH, '//div[2]/a[1]')
    BROKEN_LINK = (By.XPATH, '//div[2]/a[2]')
    ELEMENTS = (By.CSS_SELECTOR, 'br')


class UpLoadAndDownLoadLocators:
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, 'a[id="downloadButton"]')
    SELECT_A_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_FILE_PATH = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')


class DynamicPropertiesLocators:
    TEXT_WITH_RANDOM_ID = (By.XPATH, '//div[2]/div[2]/p')
    WILL_ENABLE_5_SECONDS_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    VISIBLE_AFTER_5_SECONDS = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')
