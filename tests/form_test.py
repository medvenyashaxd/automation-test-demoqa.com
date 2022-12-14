import allure

from pages.form_page import PracticeFormPage


@allure.suite('Test practice form')
class TestPracticeForm:

    @allure.feature('Test student registration form')
    class TestStudentRegistrationForm:

        @allure.title('Check practice form')
        def test_practice_form(self, driver):
            practice_form_page = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
            practice_form_page.open()

            input_info = practice_form_page.fill_fields()
            output_info = practice_form_page.check_submitting_form()

            assert [input_info.first_name + ' ' + input_info.last_name, input_info.email] == [output_info[0],
                   output_info[1]], 'table form is filled incorrectly'
