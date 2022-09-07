import time
import allure
import pytest

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#@pytest.fixture(scope='function')
#def driver():
    #driver_path = \
                #r'C:\Users\xmedv\PycharmProjects\webdriver\.wdm\drivers\chromedriver\win32\105.0.5195\chromedriver.exe'

    #options = Options()
    #options.add_argument(r"user-data-dir=C:\Users\xmedv\AppData\Local\Google\Chrome\User Data\Profile 1")

    #driver = webdriver.Chrome(executable_path=driver_path, options=options)
    #time.sleep(1)

    #yield driver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f'Screenshot{datetime.today()}', attachment_type=allure.attachment_type.PNG)
    driver.quit()
