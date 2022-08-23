import time

from pages.form_page import PracticeFormPage


class TestPracticeForm:
    class TestStudentRegistrationForm:

        def test_practice_form(self, driver):
            practice_form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
            practice_form_page.open()
            time.sleep(2)
            input_info = practice_form_page.fill_fields()
            output_info = practice_form_page.check_submitting_form()
            assert [input_info.first_name + ' ' + input_info.last_name, input_info.email] == [output_info[0],
                    output_info[1]], 'table form is filled incorrectly'
