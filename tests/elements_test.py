import random
import time
from pages.elements_page import TextBoxPages, CheckBoxPages, RadioButtonPages, WebTablePages


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

    class TestWebTable:
        def test_webtable_add_person(self, driver):
            web_table_page = WebTablePages(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_add_new_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePages(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            print(key_word)
            print(table_result)
            assert key_word in table_result

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePages(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(last_name)
            time.sleep(3)
            age = web_table_page.update_person_info()
            time.sleep(3)
            row = web_table_page.check_search_person()
            print(age)
            print(row)
            assert age in row, "The person card has not been changed"

        def test_web_table_delete_person_info(self, driver):
            web_table_page = WebTablePages(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person_info()
            text = web_table_page.check_deleted()
            assert text == 'No rows found'

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePages(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 25, 50, 100], "The number of rows has not been change"

