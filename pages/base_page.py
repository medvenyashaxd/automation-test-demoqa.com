import random

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_window(self, amount):
        self.driver.switch_to.window(self.driver.window_handles[amount])

    def switch_to_alert(self):
        alert = self.driver.switch_to.alert
        return alert

    def page_scale(self):
        self.driver.execute_script("document.body.style.zoom = '0.9'")

    def double_click(self, element):
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

    def right_click(self, element):
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()

    def random_choice_date(self):
        actions = ActionChains(self.driver)
        for _ in range(random.randint(10, 50)):
            actions.send_keys(Keys.UP).perform()

    def random_choice_location(self):
        actions = ActionChains(self.driver)
        for _ in range(random.randint(1, 3)):
            actions.send_keys(Keys.DOWN).perform()

    def press_enter(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()

    def action_drag_and_drop_by_offset(self, element, x_offset, y_offset):
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(element, x_offset, y_offset).perform()

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)

    def select_by_value(self, locator, value):
        select = Select(self.element_is_present(locator))
        select.select_by_value(value)

