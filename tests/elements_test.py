import time

from pages.elements_page import TextBoxPage, CheckBoxPage


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



    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            check = check_box_page.check_cheked_box()
            check_output = check_box_page.get_check_cheked_box()
            print(check)
            print(check_output)