import random
import time
import allure

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Gets link and open browser')
    def open(self):
        self.driver.get(self.url)

    @allure.step('Finds a visible element')
    def element_is_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    @allure.step('Finds a visible elements')
    def elements_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))

    @allure.step('Finds a present element')
    def element_is_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    @allure.step('Finds a present elements')
    def elements_are_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.presence_of_all_elements_located(locator))

    @allure.step('Finds a is not visible element')
    def element_is_not_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))

    @allure.step('Finds a clickable element')
    def element_is_clickable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    @allure.step('Goes to specified element')
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Switches to the desired window')
    def switch_to_window(self, amount):
        self.driver.switch_to.window(self.driver.window_handles[amount])

    @allure.step('Switches attention to browser notification')
    def switch_to_alert(self):
        time.sleep(1)
        alert = self.driver.switch_to.alert
        return alert

    @allure.step('Changes page overview')
    def page_scale(self):
        self.driver.execute_script("document.body.style.zoom = '0.9'")

    @allure.step('Makes a double click on the element')
    def double_click(self, element):
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()

    @allure.step('Makes a right click on the element')
    def right_click(self, element):
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()

    @allure.step('Presses the button up a random number of times')
    def random_choice_date(self):
        actions = ActionChains(self.driver)
        for _ in range(random.randint(10, 50)):
            actions.send_keys(Keys.UP).perform()

    @allure.step('Presses the button down a random number of times')
    def random_choice_location(self):
        actions = ActionChains(self.driver)
        for _ in range(random.randint(1, 3)):
            actions.send_keys(Keys.DOWN).perform()

    @allure.step('Moves screen attention to an element')
    def scroll_to_element(self, locator):
        action = ActionChains(self.driver)
        action.scroll_to_element(locator).perform()

    @allure.step('Presses enter')
    def press_enter(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()

    @allure.step('Drags the element and drop to the target')
    def action_drag_and_drop(self, source, target):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    @allure.step('Drags the element and drop to the coordinates')
    def action_drag_and_drop_by_offset(self, element, x_offset, y_offset):
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(element, x_offset, y_offset).perform()

    @allure.step('Drags the cursor to the element')
    def action_move_to_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    @allure.step('Switches to default content')
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    @allure.step('Switches to frame')
    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)

    @allure.step('Select value by value')
    def select_by_value(self, locator, value):
        select = Select(self.element_is_present(locator))
        select.select_by_value(value)

    @allure.step('Select value by index')
    def select_by_index(self, locator, value):
        select = Select(self.element_is_present(locator))
        select.select_by_index(value)
