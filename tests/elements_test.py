import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_full_name, input_email, input_curr_addr, input_per_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_addrr, output_per_addrr = text_box_page.check_filled_form()
            assert input_full_name == output_name, 'error name'
            assert  input_email == output_email, 'error email'
            assert  input_curr_addr == output_curr_addrr, 'error cur addrr'
            assert  input_per_address == output_per_addrr, 'error per addrr'
            time.sleep(2)
