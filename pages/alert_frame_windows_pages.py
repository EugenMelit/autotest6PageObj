import random

from locators.alert_frame_windows_locators import BrowserWindowLocators, AlertPageLocators, FramePageLocators, \
    NestedFramePageLocators, ModalDialogPageLocators
from pages.Base_Page import BasePage
import time

class BrowserWindowPage(BasePage):
    locators = BrowserWindowLocators()

    def check_open_new_tab(self):
        self.element_is_visible(self.locators.NEW_BUTTON_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title= self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_open_new_window(self):
        self.element_is_visible(self.locators.NEW_BUTTON_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title


class AlertWindowPage(BasePage):
    locators = AlertPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text


    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_allert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        #accept -  принимает предупреждение, нажимая кнопку «ОК».
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result


    def check_prompt_allert(self):
        text = f'autotest{random.randint(0,999)}'
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text, text_result


class FramePage(BasePage):
    locators = FramePageLocators()

    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame=self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            # осуществляет выход из окна
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]


class NestedFramePage(BasePage):
    locators=NestedFramePageLocators()
    def check_nested_frame(self):
        self.zoom_page()
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text


class ModalDialogPage(BasePage):
    locators=ModalDialogPageLocators()

    def check_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        body_small = self.element_is_present(self.locators.BODY_SMALL_MODAL).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        time.sleep(3)
        title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        body_large = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text
        return [title_small, len(body_small)], [title_large, len(body_large)]



