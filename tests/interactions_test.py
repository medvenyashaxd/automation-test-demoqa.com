from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


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

    class TestResizable:
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            box_check_one, box_check_two, check_box_out = resizable_page.change_size()

            assert box_check_one == ['width: 500px; height: 300px;'], 'height and width do not match'
            assert box_check_two == ['width: 150px; height: 150px;'], 'height and width do not match'
            assert check_box_out == ['width: 350px; height: 350px;'], 'height and width do not match'