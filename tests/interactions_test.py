from pages.interactions_page import SortablePage


class TestInteractions:
    class TestSortable:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_of_numbers_before_list, order_of_numbers_after_list = sortable_page.move_number_sortable_list()
            order_of_numbers_before_grid, order_of_numbers_after_grid = sortable_page.move_number_sortable_grid()

            assert order_of_numbers_before_list != order_of_numbers_after_list, 'values are not swapped'
            assert order_of_numbers_before_grid != order_of_numbers_after_grid, 'values are not swapped'
