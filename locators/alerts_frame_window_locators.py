from selenium.webdriver.common.by import By


class BrowserWindowLocators:
    NEW_TAB = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, 'button[id="messageWindowButton"]')
    TEXT_IN_TAB = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
    TEXT_IN_WINDOW = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')