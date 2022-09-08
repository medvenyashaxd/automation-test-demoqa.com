import allure

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite('Test interactions')
class TestInteractions:

    @allure.feature('Test sortable')
    class TestSortable:

        @allure.title('Check sortable')
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_of_numbers_list_before, order_of_numbers_list_after, order_of_numbers_grid_before, \
            order_of_numbers_grid_after = sortable_page.check_sortable()

            assert order_of_numbers_list_before != order_of_numbers_list_after, 'values are not swapped'
            assert order_of_numbers_grid_before != order_of_numbers_grid_after, 'values are not swapped'

    @allure.feature('Test selectable')
    class TestSelectable:

        @allure.title('Check selectable')
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            clicked_elements_list, check_clicked_grid = selectable_page.check_selectable()

            assert clicked_elements_list != 0, 'elements are not clicked'
            assert check_clicked_grid != 0, 'elements are not clicked'

    @allure.feature('Test resizable')
    class TestResizable:

        @allure.title('Check resizable')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            box_check_one, box_check_two, check_box_out = resizable_page.change_size()

            assert box_check_one == ['width: 500px; height: 300px;'], 'height and width do not match'
            assert box_check_two == ['width: 150px; height: 150px;'], 'height and width do not match'
            assert check_box_out == ['width: 350px; height: 350px;'], 'height and width do not match'

    @allure.feature('Test droppable')
    class TestDroppable:

        @allure.title('Check droppable')
        def test_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_simple_droppable, text_acceptable_droppable, not_greedy_box_text, not_greedy_text, greedy_box_text, \
            greedy_text = droppable_page.check_droppable()

            assert text_simple_droppable == 'Dropped!', 'the source is not in the target'
            assert text_acceptable_droppable == 'Dropped!', 'the source is not in the target'
            assert not_greedy_box_text == 'Dropped!', 'the source is not in the target'
            assert not_greedy_text == 'Dropped!', 'the source is not in the target'
            assert greedy_box_text == 'Outer droppable', 'target is not greedy'
            assert greedy_text == 'Dropped!', 'the source is not in the target'

    @allure.feature('Test draggable')
    class TestDraggable:

        @allure.title('Check draggable')
        def test_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            simple, restricted_x, restricted_y, in_container, parent_container = draggable_page.check_draggable()

            assert simple == 'position: relative; left: 30px; top: 50px;',\
                'the target does not move or the coordinates do not converge'
            assert restricted_x == 'position: relative; left: 50px; top: 0px;',\
                'the target does not move or the coordinates do not converge'
            assert restricted_y == 'position: relative; left: 0px; top: 100px;',\
                'the target does not move or the coordinates do not converge'
            assert in_container == 'position: relative; left: 120px; top: 15px;',\
                'the target does not move or the coordinates do not converge'
            assert parent_container == 'position: relative; left: 5px; top: 45px;',\
                'the target does not move or the coordinates do not converge'
