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

    CHECK_RADIO_BUTTON = (By.CSS_SELECTOR, 'p span[class="text-success"]')
