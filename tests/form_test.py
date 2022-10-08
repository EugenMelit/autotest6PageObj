import time

from pages.form_page import RegistrationFormPage


class TestForm:
    class TestRegistrationForm:
        def test_registration_form(self, driver):
            registration_form_page = RegistrationFormPage(driver, 'https://demoqa.com/automation-practice-form')
            registration_form_page.open()
            registration_form_page.fill_field_form()
            time.sleep(5)


