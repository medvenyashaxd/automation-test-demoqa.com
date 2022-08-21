import random
import time
from locators.alerts_frame_window_locators import BrowserWindowLocators, AlertsLocators, FramesLocators, \
    NestedFramesLocators, ModalDialogsLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowLocators()

    def test_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB).click()
        self.switch_to_window(1)
        text_in_new_tab = self.element_is_present(self.locators.TEXT_IN_TAB).text
        self.switch_to_window(0)
        return text_in_new_tab

    def test_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW).click()
        self.switch_to_window(1)
        text_in_new_window = self.element_is_present(self.locators.TEXT_IN_WINDOW).text
        return text_in_new_window


class AlertPage(BasePage):
    locators = AlertsLocators()

    def click_buttons_and_get_text(self):
        self.element_is_visible(self.locators.SIMPLE_ALERT).click()
        simple_alert = self.switch_to_alert()
        text_simple_button = simple_alert.text
        simple_alert.accept()

        self.element_is_visible(self.locators.TIME_ALERT).click()
        time.sleep(5)
        time_alert = self.switch_to_alert()
        text_time_alert = time_alert.text
        time_alert.accept()

        self.element_is_visible(self.locators.ALERT_BOX).click()
        box_alert = self.switch_to_alert()
        random_click = random.randint(1, 2)
        if random_click == 1:
            box_alert.accept()
        else:
            box_alert.dismiss()
        text_random_click = self.element_is_present(self.locators.ALERT_BOX_RESULT).text

        self.go_to_element(self.element_is_present(self.locators.ALERT_INPUT_BOX))
        self.element_is_visible(self.locators.ALERT_INPUT_BOX).click()
        random_text_input_alert = f'qwer{random.randint(1, 10)}'
        input_box_alert = self.switch_to_alert()
        input_box_alert.send_keys(random_text_input_alert)
        input_box_alert.accept()
        text_input_box_alert = (self.element_is_present(self.locators.RESULT_ALERT_INPUT_BOX)).text
        return text_simple_button, text_time_alert, text_random_click, random_text_input_alert, text_input_box_alert


class FramesPage(BasePage):
    locators = FramesLocators()

    def check_frames(self):
        frame1wrapper = self.element_is_present(self.locators.FRAME1WRAPPER)
        width_frame1 = frame1wrapper.get_attribute('width')
        height_frame1 = frame1wrapper.get_attribute('height')
        self.switch_to_frame(frame1wrapper)
        text_frame1wrapper = self.element_is_present(self.locators.FRAMES_TEXT).text
        self.switch_to_default_content()

        frame2wrapper = self.element_is_present(self.locators.FRAME2WRAPPER)
        width_frame2 = frame2wrapper.get_attribute('width')
        height_frame2 = frame2wrapper.get_attribute('height')
        self.switch_to_frame(frame2wrapper)
        text_frame2wrapper = self.element_is_present(self.locators.FRAMES_TEXT).text
        return [width_frame1, height_frame1, text_frame1wrapper, width_frame2, height_frame2, text_frame2wrapper]


class NestedFrames(BasePage):
    locators = NestedFramesLocators()

    def check_nested_frames(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        parent_width = parent_frame.get_attribute('width')
        parent_height = parent_frame.get_attribute('height')
        self.switch_to_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text

        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return [parent_width, parent_height, parent_text, child_text]


class ModalDialogs(BasePage):
    locators = ModalDialogsLocators()

    def check_modal_dialogs(self, dialogs):
        modal_dialogs = {'small':
                             {'button': self.locators.SMALL_MODAL,
                              'text': self.locators.TEXT_SMALL_MODAL,
                              'close': self.locators.CLOSE_SMALL_MODAL},

                         'large':
                             {'button': self.locators.LARGE_MODAL,
                              'text': self.locators.TEXT_LARGE_MODAL,
                              'close': self.locators.CLOSE_LARGE_MODAL}
                         }

        self.element_is_visible(modal_dialogs[dialogs]['button']).click()
        time.sleep(1)
        text_dialog = self.element_is_present(modal_dialogs[dialogs]['text']).text
        self.element_is_visible(modal_dialogs[dialogs]['close']).click()
        return len(text_dialog)