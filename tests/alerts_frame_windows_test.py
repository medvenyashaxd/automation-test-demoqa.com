from pages.alerts_frame_window_page import BrowserWindowPage


class TestAlertsFrameWindows:
    class TestBrowserWindow:

        def test_browser_windows(self, driver):
            browser_windows_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_new_tab = browser_windows_page.test_new_tab()
            text_new_window = browser_windows_page.test_new_window()
            assert text_new_tab == 'This is a sample page', 'text does not match'
            assert text_new_window == 'This is a sample page', 'text does not match'
