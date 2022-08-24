from pages.widgets_page import WidgetsPage, AutoCompletePage, DatePickerPage


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
            colors, color_after = auto_complete_page.check_multiple_color()
            clear = auto_complete_page.clear_all()
            singe_color, get_single_color = auto_complete_page.check_single_color()

            assert singe_color == get_single_color, 'colors do not match'
            assert colors != color_after, 'color is not removed'
            assert clear is True, 'colors not cleared'

    class TestDatePicker:
        def test_date_picker(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date, date_after = date_picker_page.set_time()
            assert date != date_after, 'date has not changed'
