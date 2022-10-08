import random
import time
from pages.elements_page import TextBoxPages, CheckBoxPages, RadioButtonPages, WebTablePages, ButtonsPages, LinksPages, \
    UploadAndDownloadPage, DynamicPropertyPage, RegistrationFormPage


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

    class TestButtons:
        def test_different_click_on_the_button(self, driver):
            button_page = ButtonsPages(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            print(double)
            print(right)
            print(click)
            assert double == 'You have done a double click', 'The double click button was not present'
            assert right == 'You have done a right click''The right click button was not present'
            assert click == 'You have done a dynamic click','The  dynamic button was not present'

    class TestLinks:

        def test_check_link(self,driver):
            link_page = LinksPages(driver, 'https://demoqa.com/links')
            link_page.open()
            link_href, current_url = link_page.check_new_tab_simple_links()
            assert link_href == current_url


        def test_check_broken_link(self,driver):
            link_page = LinksPages(driver, 'https://demoqa.com/links')
            link_page.open()
            response_code = link_page.check_broken_links('https://demoqa.com/bad-request')
            assert response_code == 400

    class TestUploadAndDownLoad:
        def test_upload_file(self, driver):
            upload_page = UploadAndDownloadPage(driver,'https://demoqa.com/upload-download')
            upload_page.open()
            file_name, result = upload_page.upload_file()
            assert file_name == result, 'The file has not been uploaded'



        def test_dowlad_file(self, driver):
            upload_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            check = upload_page.download_file()
            assert check is True, 'The file has not been downloaded'

    class TestDynamicPropertyPage:

        def test_dynamic_propertys(self, driver):
            dynamic_propertys_page = DynamicPropertyPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_propertys_page.open()
            color_before, color_after = dynamic_propertys_page.check_change_of_colors()
            assert color_before != color_after, 'The color has not been changed'

        def test_check_button_appear(self,driver):
            dynamic_propertys_page = DynamicPropertyPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_propertys_page.open()
            appear = dynamic_propertys_page.check_button_appear()
            assert appear is True, 'The button has not been appear'

        def test_enable_button(self, driver):
            dynamic_propertys_page = DynamicPropertyPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_propertys_page.open()
            enable = dynamic_propertys_page.check_enable_after()
            assert enable is True, "The button has not been enable"


