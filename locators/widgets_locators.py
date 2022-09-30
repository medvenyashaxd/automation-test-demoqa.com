import random

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
    SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    SELECT_DAY = (By.CSS_SELECTOR, 'div[class*="react-datepicker__day react-datepicker__day--"]')


class DatePickerLocators:
    SELECT_DATE = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    SELECT_DAY = (By.CSS_SELECTOR, 'div[class*="react-datepicker__day react-datepicker__day--"]')


class SliderLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarLocators:
    BUTTON_START = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRESS_SLIDER = (By.CSS_SELECTOR, 'div[role="progressbar"]')


class TabsLocators:
    TAB_WHAT = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    TEXT_WHAT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"] p[class]')

    TAB_ORIGIN = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    TEXT_ORIGIN = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"] p[class]')

    TAB_USE = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    TEXT_USE = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"] p[class]')

    TAB_MORE = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')


class ToolTipsLocators:
    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    INPUT = (By.CSS_SELECTOR, 'input[class=" mr-sm-2 form-control"]')
    CONTRARY = (By.XPATH, '//div[2]/div[2]/div[3]/a[1]')
    NUMBERS = (By.XPATH, '//div[2]/div[3]/a[2]')

    TEXT = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')


class MenuLocators:
    HREF = (By.CSS_SELECTOR, 'a[href="#"]')


class SelectMenuLocators:
    SELECT_VALUE = (By.CSS_SELECTOR, 'div[id="withOptGroup"]')
    SELECT_VALUE_MENU = (By.CSS_SELECTOR, f'div[id="react-select-2-option-{random.randint(0, 1)}-{random.randint(0, 1)}"]')

    SELECT_ONE = (By.CSS_SELECTOR, 'div[id="selectOne"]')
    SELECT_ONE_MENU = (By.CSS_SELECTOR, f'div[id="react-select-3-option-0-{random.randint(0, 5)}"]')

    SELECT_STYLE = (By.CSS_SELECTOR, 'select[id="oldSelectMenu"]')

    MULTISELECT = (By.XPATH, '//div[7]/div/div')
    MULTISELECT_VALUE = (By.CSS_SELECTOR, f'div[id="react-select-4-option-{random.randint(0, 3)}"]')

    CARS = (By.CSS_SELECTOR, 'select[id="cars"]')
