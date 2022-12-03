from datetime import time
import time
from pages.widget_page import WidgetAccordianPage, AutoCompletePage, DataPickerPage, SliderPage, ProgressBarPage, \
    TabsPage, ToolTipsPage, MenuPage, SelectMenuPage


class TestWidget:

    class TestWidgetAccordian:
        def test_widget_accordian(self, driver):
            widget_accordian_page = WidgetAccordianPage(driver, 'https://demoqa.com/accordian')
            widget_accordian_page.open()
            first_content, first_title = widget_accordian_page.check_widget_accordian('first')
            # time.sleep(3)
            second_content, second_title = widget_accordian_page.check_widget_accordian('second')
            # time.sleep(3)
            third_content, third_title = widget_accordian_page.check_widget_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0

    class TestAutoComplete:
        def test_auto_complete_page(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multiply()
            colors_result = auto_complete_page.check_color_in_multi()
            assert colors ==colors_result

        def test_remove_value_from_autocomplete_page(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multiply()
            time.sleep(2)
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multiply()
            assert count_value_before != count_value_after


        def test_single_auto_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_input_single()
            color_result = auto_complete_page.check_color_in_single()
            assert color == color_result

    class TestDataPicker:
        def test_change_select_data(self, driver):
            data_picker_page = DataPickerPage(driver, 'https://demoqa.com/date-picker')
            data_picker_page.open()
            date_before, date_after = data_picker_page.check_select_data()
            assert date_before != date_after


        def test_change_data_and_time(self, driver):
            data_picker_page = DataPickerPage(driver, 'https://demoqa.com/date-picker')
            data_picker_page.open()


    class TestSlider:
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_value_slider()
            assert before != after, "the value slide has not been changes"

    class TestProgressBar:
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            befor, after = progress_bar.change_progress_bar_value()
            assert befor != after, "the value prores bar has not been changes"

    class TestTabs:
        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_button, what_content = tabs.check_tabs('what')
            time.sleep(3)
            origin_button, origin_content = tabs.check_tabs('origin')
            time.sleep(3)
            use_button, use_content = tabs.check_tabs('use')
            more_button, more_content = tabs.check_tabs('more')
            assert what_button == "what" and what_content !=0 , "The tab_what was not present or the text is missing"
            assert origin_button == "origin" and what_content !=0, "The tab_origin was not present or the text is missing"
            assert use_button == "use" and use_content !=0, "The tab_use was not present or the text is missing"
            assert more_button == "more" and more_content !=0, "The tab_more was not present or the text is missing"

    class TestToolTips:
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text, field_text, contrary_text, link_text = tool_tips_page.check_text_tips()
            assert button_text == 'You hovered over the Button' , 'The hover_button does not exist'
            assert field_text == 'You hovered over the text field', 'The hover_field does not exist'
            assert contrary_text == 'You hovered over the Contrary', 'The hover_contrary does not exist'
            assert link_text == 'You hovered over the 1.10.32', 'The hover_link does not exist'


    class TestMenu:
        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu#')
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »',
                            'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3'], "The menu does not exist or work incorrect"

    class SelectMenu:
        def test_select_menu(self, driver):
            select_menu_page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
            select_menu_page.open()





