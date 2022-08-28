from selenium.webdriver.common.by import By


class SortableLocators:
    NUMBERS_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')

    GRID_PAGE = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_LIST = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectableLocators:
    LIST_ELEMENTS = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ACTIVE_ELEMENTS = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')

    GRID_PAGE = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ELEMENTS = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')
    GRID_ACTIVE_ELEMENTS = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')
