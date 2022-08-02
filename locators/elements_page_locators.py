from selenium.webdriver.common.by import By

class TextBoxPageLocators:
    FULL_MAME = (By.CSS_SELECTOR, 'input[id="userName"')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ELEMENTS_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECK_LIST = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    CHECK_ELEMENT_CLICK = ".//ancestor::span[@class='rct-text']"
    OUTPUT_CHECK_LIST = (By.CSS_SELECTOR, 'span[class="text-success"]')



