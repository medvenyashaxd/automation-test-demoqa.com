import time

from pages.alerts_frame_window_page import BrowserWindowPage, AlertPage, FramesPage, NestedFrames, ModalDialogs


class TestAlertsFrameWindows:
    class TestBrowserWindow:
        def test_browser_windows(self, driver):
            browser_windows_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_new_tab = browser_windows_page.test_new_tab()
            text_new_window = browser_windows_page.test_new_window()

            assert text_new_tab == 'This is a sample page', 'text does not match'
            assert text_new_window == 'This is a sample page', 'text does not match'

    class TestAlerts:
        def test_alerts(self, driver):
            alerts_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            simple_alert_text, text_time_alert, text_box_alert, random_text_input_alert, text_input_box_alert \
                = alerts_page.click_buttons_and_get_text()

            assert simple_alert_text == 'You clicked a button', 'button not pressed'
            assert text_time_alert == 'This alert appeared after 5 seconds', 'button not pressed'
            assert text_box_alert == 'You selected Ok' or 'You selected Cancel', 'button not pressed'
            assert random_text_input_alert in text_input_box_alert, 'text does not match'

    class TestFrames:
        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()
            frames_info = frames_page.check_frames()
            assert frames_info == ['500px', '350px', 'This is a sample page', '100px', '100px',
                                   'This is a sample page'], 'info does not match'

    class TestNestedFrames:
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFrames(driver, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()
            frames_info = nested_frames_page.check_nested_frames()
            assert frames_info == ['500px', '350px', 'Parent frame', 'Child Iframe'], 'info does not match'

    class TestModalDialogs:
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogs(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small_modal = modal_dialogs_page.check_modal_dialogs('small')
            large_modal = modal_dialogs_page.check_modal_dialogs('large')
            assert small_modal == 47, 'amount letters does not match'
            assert large_modal == 574, 'amount letters does not match'
