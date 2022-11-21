import time
from pages.alert_frame_windows_pages import BrowserWindowPage, AlertWindowPage, FramePage, NestedFramePage, \
    ModalDialogPage


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

    class TestFrameWindows:
        def test_frames(self, driver):
            frame_page = FramePage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "The frame doesn't exist"
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "The frame doesn't exist"


    class TestNestedFramePages:
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramePage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame', 'Frame does not exist'
            assert child_text == 'Child Iframe', 'Frame does not exist'


    class TestedModalDialogsPage:
        def test_modal_dialog_page(self, driver):
            modal_dialog_page = ModalDialogPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            small, large = modal_dialog_page.check_modal_dialogs()
            assert small[1] < large[1]
            assert small[0] == 'Small Modal'
            assert large[0] == 'Large Modal'




