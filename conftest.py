import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function')
def driver():
    #driver = webdriver.Chrome(ChromeDriverManager().install())

    driver_path = \
                r'C:\Users\xmedv\PycharmProjects\weddriver\.wdm\drivers\chromedriver\win32\104.0.5112\chromedriver.exe'

    options = Options()
    options.add_argument(r"user-data-dir=C:\Users\xmedv\AppData\Local\Google\Chrome\User Data\Profile 1")

    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    time.sleep(1)
    yield driver

