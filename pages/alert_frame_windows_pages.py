import random

from locators.alert_frame_windows_locators import BrowserWindowLocators, AlertPageLocators
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
