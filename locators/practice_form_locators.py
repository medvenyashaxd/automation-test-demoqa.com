import random
from selenium.webdriver.common.by import By


class PracticeFormLocators:
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    GENDER = (By.CSS_SELECTOR, f'label[for="gender-radio-{random.randint(1, 3)}"]')
    MOBILE_NUMBER = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    SUBJECT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    HOBBIES = (By.CSS_SELECTOR, f'div[class="col-md-9 col-sm-12"] [for="hobbies-checkbox-{random.randint(1, 3)}"]')
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')
    ELEMENTS_CLICK = (By.XPATH, '//div/div/div[1]/span')
    GO_ELEMENTS = (By.CSS_SELECTOR, 'label[class="form-label"]')
    CLOSE = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')
    INFO_IN_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
