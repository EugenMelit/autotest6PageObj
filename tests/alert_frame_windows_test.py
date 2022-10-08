import time
from pages.alert_frame_windows_pages import BrowserWindowPage, AlertWindowPage


class TestAlertFrameWindows:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            text_result = new_tab_page.check_open_new_tab()
            assert text_result == 'This is a sample page', "Page not open"

        def test_new_window(self, driver):
            browser_window_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            text_result = browser_window_page.check_open_new_window()
            assert text_result == 'This is a sample page', "Page not open"

    class TestAlertWindows:
        def test_see_alert(self, driver):
            alert_page = AlertWindowPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            time.sleep(2)
            assert alert_text == "You clicked a button", "Alert did not show up"


        def  test_appear_alert(self, driver):
            alert_page = AlertWindowPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds", "Alert did not show up"

        def test_confirm_alert(self, driver):
            alert_page = AlertWindowPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_allert()
            assert alert_text == 'You selected Ok', "Alert did not show up"


        def test_prompt_alert(self, driver):
            alert_page = AlertWindowPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, text_result = alert_page.check_prompt_allert()
            assert text in text_result, "Alert did not show up"

