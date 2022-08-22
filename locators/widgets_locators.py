from selenium.webdriver.common.by import By


class AccordianLocators:
    SECTION_ONE = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    TEXT_SECTION_ONE = (By.CSS_SELECTOR, 'div[id="section1Content"] p')

    SECTION_TWO = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    TEXT_SECTION_TWO = (By.CSS_SELECTOR, 'div[id="section2Content"] p')

    SECTION_THREE = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    TEXT_SECTION_THREE = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompleteLocators:
    MULTIPLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTIPLE_COLORS = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    DELETE_COLORS = (By.CSS_SELECTOR, 'div[class="css-xb97g8 auto-complete__multi-value__remove"] path[d]')
    CLEAR_COLORS = (By.CSS_SELECTOR, 'div[class="auto-complete__indicators css-1wy0on6"] path[d]')

    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_TEXT = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')