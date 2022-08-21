from selenium.webdriver.common.by import By


class BrowserWindowLocators:
    NEW_TAB = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    NEW_WINDOW = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    NEW_WINDOW_MESSAGE = (By.CSS_SELECTOR, 'button[id="messageWindowButton"]')
    TEXT_IN_TAB = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
    TEXT_IN_WINDOW = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
    TEXT_IN_WINDOW_MESSAGE = (By.CSS_SELECTOR, 'body')

class AlertsLocators:
    SIMPLE_ALERT = (By.CSS_SELECTOR, 'button[id="alertButton"]')
    TIME_ALERT = (By.CSS_SELECTOR, 'button[id="timerAlertButton"]')
    ALERT_BOX = (By.CSS_SELECTOR, 'button[id="confirmButton"]')
    ALERT_BOX_RESULT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    ALERT_INPUT_BOX = (By.CSS_SELECTOR, 'button[id="promtButton"]')
    RESULT_ALERT_INPUT_BOX = (By.CSS_SELECTOR, 'span[id="promptResult"]')


class FramesLocators:
    FRAME1WRAPPER = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    FRAME2WRAPPER = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    FRAMES_TEXT = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')


class NestedFramesLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')

    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'p')


class ModalDialogsLocators:
    SMALL_MODAL = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    CLOSE_SMALL_MODAL = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    TEXT_SMALL_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"]')

    LARGE_MODAL = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    TEXT_LARGE_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"] p')
    CLOSE_LARGE_MODAL = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')


