from pages.widgets_page import WidgetsPage


class TestWidgets:
    class TestAccordian:

        def test_accordian(self, driver):
            accordian_page = WidgetsPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            text_section_one, text_section_two, text_section_three = accordian_page.check_accordian()
            print(text_section_one, text_section_two, text_section_three)