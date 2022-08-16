from pages.alerts_frame_window_page import BrowserWindowPage, AlertPage


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
            alerts_page.click_buttons_and_get_text()
