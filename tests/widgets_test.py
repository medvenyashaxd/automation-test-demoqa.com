import time

from pages.widgets_page import WidgetsPage, AutoCompletePage


class TestWidgets:
    class TestAccordian:

        def test_accordian(self, driver):
            accordian_page = WidgetsPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            section_one = accordian_page.check_accordian('section_one')
            section_two = accordian_page.check_accordian('section_two')
            section_three = accordian_page.check_accordian('section_three')

            assert section_one == 574, 'the number of letters does not match'
            assert section_two == 763, 'the number of letters does not match'
            assert section_three == 613, 'the number of letters does not match'

    class TestAutoComplete:
        def test_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            time.sleep(2)
            added_colors = auto_complete_page.check_multiple_auto_complete()
            result_colors = auto_complete_page.delete_auto_complete()
            clear = auto_complete_page.clear_auto_complete()
            input_colors, output_colors = auto_complete_page.check_auto_complete_single_color()

            assert added_colors != result_colors, 'color is not removed'
            assert clear is True, 'input not cleared'
            assert input_colors == output_colors, 'color is does not match'