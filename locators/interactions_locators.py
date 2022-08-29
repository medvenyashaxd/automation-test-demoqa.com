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


class ResizableLocators:
    RESIZABLE_BOX_ARROW = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"] span[class="react-resizable-handle react-resizable-handle-se"]')

    GET_SIZE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')

    RESIZABLE_BOX_OUT_ARROW = (By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')
    GET_SIZE_OUT_BOX = (By.CSS_SELECTOR, 'div[id="resizable"]')