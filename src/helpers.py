import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.config import Config
from src.data import Data
from src.elements import Elements


class GenerateUser:

    @staticmethod
    def generate_email():
        add = random.randint(100, 999)
        domain = random.choice(['@mail.ru', '@gmail.com', '@yandex.ru'])
        email = 'orlovaalena13' + str(add) + domain
        return email

    @staticmethod
    def generate_password():
        add = random.randint(10, 99)
        password = 'pass' + str(add)
        return password


class SignIn:
    @staticmethod
    def sign_in(driver):
        driver.find_element(*Elements.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains('/login'))
        driver.find_element(*Elements.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(*Elements.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(*Elements.CONFIRM_LOGIN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_to_be(Config.URL))
