from selenium.webdriver.common.by import By


class AccordianLocators:
    SECTION_ONE = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    TEXT_SECTION_ONE = (By.CSS_SELECTOR, 'div[id="section1Content"] p')

    SECTION_TWO = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    TEXT_SECTION_TWO = (By.CSS_SELECTOR, 'div[id="section2Content"] p')

    SECTION_THREE = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    TEXT_SECTION_THREE = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompleteLocators:
    MULTIPLE_COLORS_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'div[class="css-xb97g8 auto-complete__multi-value__remove"] path[d]')
    CLEAR_ALL = (By.CSS_SELECTOR, 'div[class="auto-complete__indicators css-1wy0on6"] path[d]')

    BUTTONS_COLOR_TEXT = (By.CSS_SELECTOR, 'div[class="css-12jo7m5 auto-complete__multi-value__label"]')

    SINGLE_COLOR_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    BUTTON_COLOR_TEXT = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')


class DatePickerLocators:
    SELECT_DATE = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
