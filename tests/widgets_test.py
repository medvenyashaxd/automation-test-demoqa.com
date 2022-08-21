from pages.widgets_page import WidgetsPage


class TestWidgets:
    class TestAccordian:

        def test_accordian(self, driver):
            accordian_page = WidgetsPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            section_one = accordian_page.check_accordian('section_one')
            section_two = accordian_page.check_accordian('section_two')
            section_three = accordian_page.check_accordian('section_three')
            assert section_one == 574
            assert section_two == 763
            assert section_three == 613