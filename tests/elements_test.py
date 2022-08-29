import time
from pages.elements_page import TextBoxPages, CheckBoxPages, RadioButtonPages


class TestElements:

    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPages(driver, 'https://demoqa.com/text-box')
            text_box_page.open()

            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_current_address, output_permanent_address = text_box_page.check_field_form()
            assert full_name == output_name, "the full_name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_current_address, "the current_address does not match"
            assert permanent_address == output_permanent_address, "the permanent_address does not match"

    class TestCheckbox:
        def test_check_box(self, driver):
            check_box_page =CheckBoxPages(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, 'checkbox have not been selected'

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPages(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('Yes')
            output_result_yes =  radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('No')
            output_result_no = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('Impressive')
            output_result_impressive = radio_button_page.get_output_result()
            assert output_result_yes == 'Yes'
            assert output_result_no == 'No'
            assert output_result_impressive == 'Impressive'