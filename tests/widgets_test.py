from pages.widgets_page import WidgetsPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage


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

    class TestSlider:
        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            changed_value = slider_page.move_the_slider()
            assert changed_value != '25', 'value has not changed'

    class TestProgressBar:
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            status_slider, status_after = progress_bar_page.check_progress_bar()

            assert status_slider == '0', 'button not pressed'
            assert status_after == '100', 'slider not reached value'

    class TestTabs:
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            text_tab_whats = tabs_page.check_tabs('whats')
            text_tab_origin = tabs_page.check_tabs('origin')
            text_tab_use = tabs_page.check_tabs('use')
            text_tab_more = tabs_page.check_tabs('more')

            assert text_tab_whats == 574, 'the number of letters does not match'
            assert text_tab_origin == 763, 'the number of letters does not match'
            assert text_tab_use == 613, 'the number of letters does not match'
            assert text_tab_more is False, 'the button is clickable'
