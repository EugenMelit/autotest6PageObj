import random
import time

from locators.interactions_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators
from pages.Base_Page import BasePage


class SortablePage(BasePage):

    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_by_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)

        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.GRID).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_by_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)

        return order_before, order_after

class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_random(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_random(self.locators.LIST_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.GRID_TAB).click()
        self.click_random(self.locators.GRID_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text

class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_value_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_and_min_size(self, element):
        size = self.element_is_visible(element)
        # ?????????? ???????????????? ???????????? ?? ???????????? ????????????????
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        # ???????????????? ?????????????? ???????? ???? ???????????????? ??????????????????????
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), 450, 280)
        max_size = self.get_value_from_width_height(self.get_max_and_min_size(self.locators.RESIZABLE_BOX))

        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -450, -280)
        min_size = self.get_value_from_width_height(self.get_max_and_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resizable(self):
        # ???????????????? ?????????????? ???????? ???? ???????????????? ?????????????????????? ?????????????????? ??????????????,?? ???????????????? ???????? ????????????????
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(1, 300), random.randint(1, 300))
        max_size = self.get_value_from_width_height(self.get_max_and_min_size(self.locators.RESIZABLE))
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(-200, -1), random.randint(-200, -1))
        min_size = self.get_value_from_width_height(self.get_max_and_min_size(self.locators.RESIZABLE))

        return max_size, min_size






