
import time
from pages.Base_Page import BasePage


def test(driver):
    page= BasePage(driver, 'https://demoqa.com/text-box')
    page.open()
    time.sleep(3)