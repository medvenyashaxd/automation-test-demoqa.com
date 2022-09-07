import time
import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage, \
    BrokenLinksImagesPage, UpLoadAndDownLoadPage, DynamicPropertiesPage


@allure.suite('Elements')
class TestElements:

    @allure.feature('Test text box')
    class TestTextBox:

        @allure.title('Check text box')
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email = text_box_page.fill_form_fields()
            output_full_name, output_email = text_box_page.check_filled_form()

            assert full_name == output_full_name, 'name is not correct'
            assert email == output_email, 'email is not correct'

    @allure.feature('Test check box')
    class TestCheckBox:

        @allure.title('Check box page')  # Invalid file name to check output
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            time.sleep(2)
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            check = check_box_page.check_checked_box()
            check_output = check_box_page.get_check_checked_box()

            print(check)
            print(check_output)

    @allure.feature('Test radio button')
    class TestRadioButton:

        @allure.title('Check radio button')
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            time.sleep(2)
            radio_button_page.click_radio_button('yes')
            output_yes = radio_button_page.get_output_text_button()
            radio_button_page.click_radio_button('impressive')
            output_impressive = radio_button_page.get_output_text_button()
            test_click_no = radio_button_page.click_radio_button('no')

            assert output_yes == 'Yes', 'button is not clicked'
            assert output_impressive == 'Impressive', 'button is not clicked'
            assert test_click_no is False, 'button is clicked'

    @allure.feature('Test web tables')
    class TestWebTables:

        @allure.title('Check web tables')
        def test_web_tables(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            time.sleep(2)
            input_table = web_tables_page.click_add_and_fill_form(1)
            output_table = web_tables_page.check_web_table()

            assert input_table in output_table, 'person was not found in the table'

        @allure.title('Check search table')
        def test_search_table(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            time.sleep(2)
            person_info = web_tables_page.click_add_and_fill_form(1)[1]
            web_tables_page.filling_search(person_info)
            table_info = web_tables_page.check_filling_search()

            assert person_info in table_info, 'person was not found in the search'

        @allure.title('Check edit information')
        def test_edit_info(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            time.sleep(2)
            input_info = web_tables_page.click_add_and_fill_form(1)
            web_tables_page.filling_search(input_info[1])
            edit_info = web_tables_page.check_edit_info()
            info_in_row = web_tables_page.check_filling_search()

            assert edit_info in info_in_row, 'text does not match'

        @allure.title('Check delete information')
        def test_delete_info(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            time.sleep(2)
            person_info = web_tables_page.click_add_and_fill_form(1)
            web_tables_page.filling_search(person_info[1])
            delete_info = web_tables_page.delete_info_and_check()

            assert 'No rows found' in delete_info, 'text does not match'

        @allure.title('Check edit rows')
        def test_edit_rows(self, driver):  # bug! only 25 lines can be selected
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            web_tables_page.page_rows_edit()

    @allure.feature('Test buttons')
    class TestButtons:

        @allure.title('Check buttons ')
        def test_buttons(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            time.sleep(2)
            double = buttons_page.click_button('double')
            right = buttons_page.click_button('right')
            click = buttons_page.click_button('click')

            assert double == 'You have done a double click', 'double click error'
            assert right == 'You have done a right click', 'right click error'
            assert click == 'You have done a dynamic click', 'click error'

    @allure.feature('Test link')
    class TestLinks:

        @allure.title('Check link in window handles')
        def test_link_in_window_handles(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            url, status = links_page.check_link_opened_in_new_tab('home')
            url_random_id, status_random_id = links_page.check_link_opened_in_new_tab('home_random_id')

            status_code_created_link = links_page.check_link('https://demoqa.com/created', 'created')
            status_code_no_content_link = links_page.check_link('https://demoqa.com/no-content', 'no_content')
            status_code_moved_link = links_page.check_link('https://demoqa.com/moved', 'moved')
            status_code_not_found_link = links_page.check_link('https://demoqa.com/invalid-url', 'not_found')

            assert url, status == ['https://demoqa.com/ 200']
            assert url_random_id, status_random_id == ['https://demoqa.com/ 200']

            assert status_code_created_link == 201, 'link is work'
            assert status_code_no_content_link == 204, 'link is work'
            assert status_code_moved_link == 301, 'link is work'
            assert status_code_not_found_link == 404, 'link is work'

    @allure.feature('Test broken link')
    class TestBrokenLinksImage:

        @allure.title('Check valid broken link')
        def test_valid_broken_link(self, driver):
            broken_page = BrokenLinksImagesPage(driver, 'https://demoqa.com/broken')
            broken_page.open()
            request_status_code_valid_link = broken_page.check_link('http://demoqa.com/', 'valid_link')
            broken_page.open()
            request_status_code_broken_link = broken_page.check_link(
                'http://the-internet.herokuapp.com/status_codes/500', 'broken_link')

            assert request_status_code_valid_link == 200, 'link not work'
            assert request_status_code_broken_link == 500, 'link is work'

    @allure.feature('Test upload and download file')
    class TestUpLoadAndDownload:

        @allure.title('Check download')
        def test_download(self, driver):
            download_file_page = UpLoadAndDownLoadPage(driver, 'https://demoqa.com/upload-download')
            download_file_page.open()
            check = download_file_page.download_file()

            assert check is True, 'file has not been download'

        @allure.title('Check lpload')
        def test_upload(self, driver):
            upload_file_page = UpLoadAndDownLoadPage(driver, 'https://demoqa.com/upload-download')
            upload_file_page.open()
            check_file, path = upload_file_page.upload_file()

            assert check_file == path, 'file is not true'

    @allure.feature('Test dynamic properties')
    class TestDynamicProperties:

        @allure.title('Check dynamic properties')
        def test_dynamic_properties(self, driver):
            dynamic_properties = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties.open()
            text = dynamic_properties.check_text_with_random_id()
            enable_button = dynamic_properties.check_enable_button_after_5_second()
            color_button = dynamic_properties.check_change_color()
            visible_button = dynamic_properties.check_visible_button_after_5_second()

            assert enable_button is True, 'element is not clickable'
            assert text == 'This text has random Id', 'text does not match'
            assert color_button != 'rgba(255, 255, 255, 1)'
            assert visible_button is True, 'element is not visible'
