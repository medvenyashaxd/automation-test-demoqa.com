from pages.interactions_page import SortablePage, SelectablePage


class TestInteractions:
    class TestSortable:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_of_numbers_list_before, order_of_numbers_list_after, order_of_numbers_grid_before, \
            order_of_numbers_grid_after = sortable_page.check_sortable()

            assert order_of_numbers_list_before != order_of_numbers_list_after, 'values are not swapped'
            assert order_of_numbers_grid_before != order_of_numbers_grid_after, 'values are not swapped'


    class TestSelectable:
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            clicked_elements_list, check_clicked_grid = selectable_page.check_selectable()

            assert clicked_elements_list != 0, 'elements are not clicked'
            assert check_clicked_grid != 0, 'elements are not clicked'
