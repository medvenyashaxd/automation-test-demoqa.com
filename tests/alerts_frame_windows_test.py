import allure

from pages.alerts_frame_window_page import BrowserWindowPage, AlertPage, FramesPage, NestedFrames, ModalDialogs


@allure.suite('Test alerts frame and window')
class TestAlertsFrameWindows:

    @allure.feature('Test window')
    class TestBrowserWindow:

        @allure.title('Check browser window')
        def test_browser_windows(self, driver):
            browser_windows_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()

            new_tab = browser_windows_page.check_browser_window('new_tab')
            new_window = browser_windows_page.check_browser_window('new_window')
            new_window_message = browser_windows_page.check_browser_window('new_window_message')

            assert new_window_message == 'This is a sample page', 'text does not match'
            assert new_tab == 'This is a sample page', 'text does not match'
            assert new_window == 'This is a sample page', 'text does not match'

    @allure.feature('Test alerts')
    class TestAlerts:
        @allure.title('Check alerts')
        def test_alerts(self, driver):
            alerts_page = AlertPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()

            simple_alert = alerts_page.check_alerts('simple_alert')
            time_alert = alerts_page.check_alerts('time_alert')
            box_alert = alerts_page.check_alerts('box_alert')
            random_text_input_alert, output_text = alerts_page.check_alerts('box_input_alert')

            assert simple_alert == 'You clicked a button', 'button not pressed'
            assert time_alert == 'This alert appeared after 5 seconds', 'button not pressed'
            assert box_alert == 'You selected Ok' or 'You selected Cancel', 'button not pressed'
            assert random_text_input_alert in output_text, 'text does not match'

    @allure.feature('Test frames')
    class TestFrames:

        @allure.title('Test frames')
        def test_frames(self, driver):
            frames_page = FramesPage(driver, 'https://demoqa.com/frames')
            frames_page.open()

            frame1wrapper = frames_page.check_frames('frame1wrapper', 'text')
            frame2wrapper = frames_page.check_frames('frame2wrapper', 'text')

            assert frame1wrapper == ['500px', '350px', 'This is a sample page'], 'info does not match'
            assert frame2wrapper == ['100px', '100px', 'This is a sample page'], 'info does not match'

    @allure.feature('Test nested frames')
    class TestNestedFrames:
        @allure.title('Check nested frames')
        def test_nested_frames(self, driver):
            nested_frames_page = NestedFrames(driver, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()

            frames_info = nested_frames_page.check_nested_frames()

            assert frames_info == ['500px', '350px', 'Parent frame', 'Child Iframe'], 'info does not match'

    @allure.feature('Test modal dialogs')
    class TestModalDialogs:

        @allure.title('Check modal dialogs')
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogs(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()

            small_modal = modal_dialogs_page.check_modal_dialogs('small')
            large_modal = modal_dialogs_page.check_modal_dialogs('large')

            assert small_modal == 47, 'amount letters does not match'
            assert large_modal == 574, 'amount letters does not match'
