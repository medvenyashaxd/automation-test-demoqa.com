import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage


class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_full_name, input_email, input_curr_addr, input_per_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_addrr, output_per_addrr = text_box_page.check_filled_form()
            assert input_full_name == output_name, 'error name'
            assert input_email == output_email, 'error email'
            assert input_curr_addr == output_curr_addrr, 'error cur addrr'
            assert input_per_address == output_per_addrr, 'error per addrr'

    class TestCheckBox:
        # bug! Wrong output filename when output check
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            check = check_box_page.check_checked_box()
            check_output = check_box_page.get_check_checked_box()
            print(check)
            print(check_output)

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.output_text_button()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.output_text_button()
            assert output_yes == 'Yes', 'error yes'
            assert output_impressive == 'Impressive', 'error impressive'

    class TestWebTables:
        def test_web_tables(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            input_table = web_tables_page.click_add_and_fill_form(1)
            output_table = web_tables_page.check_web_table()
            assert input_table in output_table, 'the person was not found in the table'

        def test_search_table(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            person_info = web_tables_page.click_add_and_fill_form(1)[1]
            web_tables_page.filling_search(person_info)
            table_info = web_tables_page.check_filling_search()
            assert person_info in table_info, 'the person was not found in the search'

        def test_edit_info(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            input_info = web_tables_page.click_add_and_fill_form(1)
            web_tables_page.filling_search(input_info[1])
            edit_info = web_tables_page.check_edit_info()
            info_in_row = web_tables_page.check_filling_search()
            assert edit_info in info_in_row

        def test_delete_info(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            person_info = web_tables_page.click_add_and_fill_form(1)
            web_tables_page.filling_search(person_info[1])
            # web_tables_page.filling_search('Cierra')
            delete_info = web_tables_page.delete_info_and_check()
            print(delete_info)
            assert 'No rows found' in delete_info

        def test_edit_rows(self, driver):  # bug! 25 lines can be selected in full screen.
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            web_tables_page.page_rows_edit()
            time.sleep(5)

    class TestButtons:
        def test_buttons(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double = buttons_page.click_button('double')
            right = buttons_page.click_button('right')
            click = buttons_page.click_button('click')
            assert double == 'You have done a double click', 'double click error'
            assert right == 'You have done a right click', 'right click error'
            assert click == 'You have done a dynamic click', 'click error'

    class TestLinks:
        def test_link_in_window_handles(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_link_in_handles()
            assert href_link == current_url

        def test_dynamic_link_in_window_handles(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_dynamic_link()
            assert href_link == current_url

        def test_created_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response = links_page.check_created_link('https://demoqa.com/created')
            assert response == 201

        def test_no_content_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response = links_page.check_no_content('https://demoqa.com/no-content')
            assert response == 204

        def test_moved_link(self, driver):
            link_page = LinksPage(driver, 'https://demoqa.com/links')
            link_page.open()
            response = link_page.check_moved_link('https://demoqa.com/moved')
            assert response == 301
