from datetime import time

from pages.interaction_page import SortablePage, SelectablePage, ResizablePage


class TestInteractions:

    class TestSortablePage:
        def test_check_sortable(self, driver):

            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after , "The changes does not perform"
            assert grid_before != grid_after, "The changes does not perform"

    class TestSelectablePage:
        def test_check_selectable(self, driver):

            selectable_page =SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active_list = selectable_page.select_list_item()

            active_grid = selectable_page.select_grid_item()
            assert len(active_list) > 0 , "Any position was not selected"
            assert len(active_grid) > 0 , "Any item was not selected"

    class TestResizablePage:
        def test_check_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            # resizable_page.zoom_page()

            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resiza, min_resiza = resizable_page.change_size_resizable()
            assert ('500px', '300px') == max_box
            assert ('150px', '150px') == min_box
            assert max_resiza != min_resiza