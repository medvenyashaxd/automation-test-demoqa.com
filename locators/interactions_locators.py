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
    RESIZABLE_BOX_ARROW = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]\
                                                        span[class="react-resizable-handle react-resizable-handle-se"]')

    GET_SIZE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')

    RESIZABLE_BOX_OUT_ARROW = (By.CSS_SELECTOR, 'div[id="resizable"]\
                                                        span[class="react-resizable-handle react-resizable-handle-se"]')

    GET_SIZE_OUT_BOX = (By.CSS_SELECTOR, 'div[id="resizable"]')


class DroppableLocators:
    SIMPLE_DRAGGABLE = (By.CSS_SELECTOR, 'div #draggable')
    SIMPLE_DROP_HERE = (By.CSS_SELECTOR, ' div[id="droppableExample-tabpane-simple"] #droppable')
    SIMPLE_TEXT = (By.CSS_SELECTOR, ' div[id="droppableExample-tabpane-simple"] #droppable p')


    ACCEPT_PAGE = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    NOT_ACCEPTABLE_NOTIFICATION = (By.CSS_SELECTOR, 'div #notAcceptable')
    ACCEPTABLE_NOTIFICATION = (By.CSS_SELECTOR, 'div #acceptable')
    ACCEPTABLE_DROP_HERE = (By.CSS_SELECTOR, 'div #droppableExample-tabpane-accept div #droppable')
    ACCEPTABLE_TEXT = (By.CSS_SELECTOR, 'div #droppableExample-tabpane-accept div #droppable p')

    PREVENT_PROPAGATION_PAGE = (By.CSS_SELECTOR, 'nav #droppableExample-tab-preventPropogation')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, 'div #dragBox')
    NOT_GREEDY_BOX = (By.CSS_SELECTOR, 'div #notGreedyInnerDropBox')
    TEXT_NOT_GREEDY_BOX = (By.XPATH, '//div[2]/div/div[3]/div/div[2]/div[1]/p')
    TEXT_NOT_GREEDY = (By.CSS_SELECTOR, 'div #notGreedyDropBox  [class="drop-box ui-droppable ui-state-highlight"] p')
    #greedy
    GREEDY_BOX = (By.CSS_SELECTOR, 'div #greedyDropBoxInner')
    GREEDY_BOX_TEXT = (By.XPATH, '//div[2]/div[2]/p')
    GREEDY_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] [class="drop-box ui-droppable ui-state-highlight"] P')

    REVERT_DRAG_ME_PAGE = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.CSS_SELECTOR, 'div #revertable')
    DROP_HERE_REVERT_BOX = (By.CSS_SELECTOR, 'div [id="droppableExample-tabpane-revertable"] div[id="droppable"]')
    DROP_HERE_REVERT_TEXT = (By.CSS_SELECTOR, 'div [id="droppableExample-tabpane-revertable"] div[id="droppable"] p')

    NOT_REVERT = (By.CSS_SELECTOR, 'div #notRevertable')
