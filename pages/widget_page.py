import time
import random


from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generator_color, generator_data
from locators.widget_locators import WidgetAccordianPageLocators, AutoCompletePageLocators, DataPickerPageLocators, \
    SliderPageLocators, ProgresBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators, \
    SelectMenuPageLocators
from pages.Base_Page import BasePage


class WidgetAccordianPage(BasePage):
    locators = WidgetAccordianPageLocators()

    def check_widget_accordian(self, accordian_num):
        # self.zoom_page()
        accordian = {'first':
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_SECOND_CONTENT},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_THIRD_CONTENT},
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()

            section_content = self.element_is_present(accordian[accordian_num]['content']).text

        return [len(section_content), section_title.text]

class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multiply(self):
        colors = random.sample(next(generator_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            # sample - берет одно значение из массива,k - колич.эл-ов
            input_multi = self.elements_is_clicable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors


    def remove_value_from_multiply(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after


    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors


    def fill_input_single(self):
        color = random.sample(next(generator_color()).color_name, k=1)
        input_single = self.elements_is_clicable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text

class DataPickerPage(BasePage):
    locators = DataPickerPageLocators()

    def check_select_data(self):
        date = next(generator_data())
        input_date = self.element_is_visible(self.locators.DATA_INPUT)
        value_date_before = input_date.get_attribute("value")
        input_date.click()
        self.select_date_by_text(self.locators.DATA_MONTH, date.month)
        self.select_date_by_text(self.locators.DATA_YEAR, date.year)
        self.select_item_from_list(self.locators.DATA_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute("value")
        return value_date_before, value_date_after

    def select_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        # Select-полезные методы с раскрывающимеся списками
        select.select_by_visible_text(value)

    def select_item_from_list(self, elements, value):
        item_list = self.elements_are_visible(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break



class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_value_slider(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)

        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')

        return value_before, value_after






class ProgressBarPage(BasePage):
    locators = ProgresBarPageLocators()
    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRES_BAR_VALUE).text
        progres_bar_button = self.elements_is_clicable(self.locators.PROGRES_BAR_BUTTON)
        progres_bar_button.click()
        time.sleep(random.randint(1, 5))
        progres_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRES_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):

    locators = TabsPageLocators()
    def check_tabs(self,name_tab):
        tabs = {'what':
                 {'title': self.locators.TAB_WHAT,
                  'content': self.locators.TAB_WHAT_CONTENT},
               'origin':
                 {'title': self.locators.TAB_ORIGIN,
                  'content': self.locators.TAB_ORIGIN_CONTENT},
               'use':
                 {'title': self.locators.TAB_USE,
                  'content': self.locators.TAB_USE_CONTENT},
               'more':
                 {'title': self.locators.TAB_MORE,
                  'content': self.locators.TAB_MORE_CONTENT},
             }

        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        what_content = self.element_is_visible(tabs[name_tab]['content']).text
        return button.text, len(what_content)


        # what_button = self.element_is_visible(self.locators.TAB_WHAT)
        # origin_button = self.element_is_visible(self.locators.TAB_ORIGIN)
        # use_button = self.element_is_visible(self.locators.TAB_USE)
        # more_button = self.element_is_visible(self.locators.TAB_MORE)
        # what_button.click()
        # what_button_content = self.element_is_visible(self.locators.TAB_WHAT_CONTENT).text
        # origin_button.click()
        # origin_button_content = self.element_is_visible(self.locators.TAB_ORIGIN_CONTENT).text
        # use_button.click()
        # use_button_content = self.element_is_visible(self.locators.TAB_USE_CONTENT).text
        # more_button.click()
        # more_button_content = self.element_is_visible(self.locators.TAB_MORE_CONTENT).text
        # return [what_button.text, len(what_button_content)], [origin_button.text, len(origin_button_content)],\
        #        [use_button.text, len(use_button_content)], [more_button.text, len(more_button_content)]

class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tool_tips(self, hower_elem, wait_elem):

        element = self.element_is_present(hower_elem)
        self.action_move_to_element(element)
        self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    def check_text_tips(self):
        tool_tips_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON_HOVER)
        time.sleep(3)
        tool_tips_text_field = self.get_text_from_tool_tips(self.locators.INPUT_FIELD, self.locators.FIELD_LINK_HOVER)
        time.sleep(3)
        tool_tips_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK, self.locators.CONTRARY_LINK_HOVER)
        time.sleep(3)
        tool_tips_text_link = self.get_text_from_tool_tips(self.locators.SECTION_LINK, self.locators.SECTION_LINK_HOVER)
        time.sleep(3)
        return tool_tips_text_button, tool_tips_text_field, tool_tips_text_contrary, tool_tips_text_link


class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            time.sleep(3)
            self.action_move_to_element(item)
            # self.element_is_visible(item)
            data.append(item.text)
        return data

class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()








