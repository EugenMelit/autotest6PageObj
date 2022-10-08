import os

from selenium.webdriver import Keys

from generator.generator import generator_person, generator_file
from locators.form_page_locators import RegistrationFormPageLocators
from pages.Base_Page import BasePage


class RegistrationFormPage(BasePage):
    locators = RegistrationFormPageLocators()

    def fill_field_form(self):
        person = next(generator_person())
        file_name, path = generator_file()
        # self.remove_footer()
        self.zoom_page()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.locators.SUBJECTS).send_keys('Maths')
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADRESS).send_keys(person.current_address)
        self.element_is_visible(self.locators.STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()
        return person
