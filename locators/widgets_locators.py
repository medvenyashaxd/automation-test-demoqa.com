from selenium.webdriver.common.by import By


class AccordianLocators:
    SECTION_ONE = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    TEXT_SECTION_ONE = (By.CSS_SELECTOR, 'div[id="section1Content"] p')

    SECTION_TWO = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    TEXT_SECTION_TWO = (By.CSS_SELECTOR, 'div[id="section2Content"] p')

    SECTION_THREE = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    TEXT_SECTION_THREE = (By.CSS_SELECTOR, 'div[id="section3Content"] p')

