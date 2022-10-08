import random

from selenium.webdriver.common.by import By

class RegistrationFormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    GENDER = (By.CSS_SELECTOR,  f'div[class*="custom-control"] label[for="gender-radio-{random.randint(1,3)}"]')

    MOBILE = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    SUBJECTS = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    HOBBIES = (By.CSS_SELECTOR, f'div[class*="custom-control"] label[for="hobbies-checkbox-{random.randint(1,3)}"]')
    FILE_INPUT = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')

    # result table

    RESULT_TABLE = (By.CSS_SELECTOR, '')