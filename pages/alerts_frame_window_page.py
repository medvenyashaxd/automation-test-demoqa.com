import random
import time
import allure

from locators.alerts_frame_window_locators import BrowserWindowLocators, AlertsLocators, FramesLocators, \
    NestedFramesLocators, ModalDialogsLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowLocators()

    @allure.step('Click on the button, switch to a new tab and take the text')
    def check_browser_window(self, button, locator=locators):
        buttons = {'new_tab':
                   {'button': locator.NEW_TAB,
                    'text': locator.TEXT_IN_TAB},

                   'new_window':
                       {'button': locator.NEW_WINDOW,
                        'text': locator.TEXT_IN_WINDOW},

                   'new_window_message':
                       {'button': locator.NEW_WINDOW_MESSAGE,
                        'text': locator.TEXT_IN_WINDOW_MESSAGE}
                   }

        self.element_is_visible(buttons[button]['button']).click()
        self.switch_to_window(1)
        text = self.element_is_present(buttons[button]['text']).text
        self.switch_to_window(0)

        return text


class AlertPage(BasePage):
    locators = AlertsLocators()

    @allure.step('Click on the button, switch to the notification and take the text')
    def check_alerts(self, alert, locator=locators):
        alerts = {'simple_alert':
                  {'alert': locator.SIMPLE_ALERT},

                  'time_alert':
                      {'alert': locator.TIME_ALERT},

                  'box_alert':
                      {'alert': locator.ALERT_BOX,
                       'text': locator.ALERT_BOX_RESULT},

                  'box_input_alert':
                      {'alert': locator.ALERT_INPUT_BOX,
                       'text': locator.RESULT_ALERT_INPUT_BOX}
                  }

        self.element_is_visible(alerts[alert]['alert']).click()

        if alert == 'simple_alert':
            selected_alert = self.switch_to_alert()
            alert_text = selected_alert.text
            selected_alert.accept()

            return alert_text

        elif alert == 'time_alert':
            time.sleep(5)
            selected_alert = self.switch_to_alert()
            alert_text = selected_alert.text
            selected_alert.accept()

            return alert_text

        elif alert == 'box_alert':
            selected_alert = self.switch_to_alert()
            random_click = random.randint(1, 2)
            if random_click == 1:
                selected_alert.accept()

            else:
                selected_alert.dismiss()
            text_random_click = self.element_is_present(alerts[alert]['text']).text

            return text_random_click

        elif alert == 'box_input_alert':
            random_text_input_alert = f'qwer{random.randint(1, 10)}'
            selected_alert = self.switch_to_alert()
            selected_alert.send_keys(random_text_input_alert)
            selected_alert.accept()
            output_text = self.element_is_present(alerts[alert]['text']).text

            return random_text_input_alert, output_text


class FramesPage(BasePage):
    locators = FramesLocators()

    @allure.step('Switching attention between frames and taking width, height and text')
    def check_frames(self, frame, text, locator=locators):
        frames = {'frame1wrapper':
                  {'window': locator.FRAME1WRAPPER},

                  'frame2wrapper':
                      {'window': locator.FRAME2WRAPPER},

                  'text':
                      {'content': locator.FRAMES_TEXT}
                  }

        frame_wrapper = self.element_is_present(frames[frame]['window'])
        width_frame = frame_wrapper.get_attribute('width')
        height_frame = frame_wrapper.get_attribute('height')
        self.switch_to_frame(frame_wrapper)
        text_frame_wrapper = self.element_is_present(frames[text]['content']).text
        self.switch_to_default_content()

        return [width_frame, height_frame, text_frame_wrapper]


class NestedFrames(BasePage):
    locators = NestedFramesLocators()

    @allure.step('Switching attention between parent and child frames and taking text')
    def check_nested_frames(self, locator=locators):
        parent_frame = self.element_is_present(locator.PARENT_FRAME)
        parent_width = parent_frame.get_attribute('width')
        parent_height = parent_frame.get_attribute('height')
        self.switch_to_frame(parent_frame)
        parent_text = self.element_is_present(locator.PARENT_TEXT).text

        child_frame = self.element_is_present(locator.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.element_is_present(locator.CHILD_TEXT).text

        return [parent_width, parent_height, parent_text, child_text]


class ModalDialogs(BasePage):
    locators = ModalDialogsLocators()

    @allure.step('Switching between Modal Dialogs')
    def check_modal_dialogs(self, dialog, locator=locators):
        modal_dialogs = {'small':
                         {'button': locator.SMALL_MODAL,
                          'text': locator.TEXT_SMALL_MODAL,
                          'close': locator.CLOSE_SMALL_MODAL},

                         'large':
                             {'button': locator.LARGE_MODAL,
                              'text': locator.TEXT_LARGE_MODAL,
                              'close': locator.CLOSE_LARGE_MODAL}
                         }

        self.element_is_visible(modal_dialogs[dialog]['button']).click()
        text_dialog = self.element_is_visible(modal_dialogs[dialog]['text']).text
        self.element_is_visible(modal_dialogs[dialog]['close']).click()

        return len(text_dialog)
