from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.config import Config
from src.data import Data
from src.elements import Elements
from src.helpers import GenerateUser


class TestCreateAnAccount:

    def test_create_new_account(self, driver):
        driver.find_element(*Elements.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains('/login'))
        driver.find_element(*Elements.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains('/register'))
        driver.find_element(*Elements.USERNAME_INPUT).send_keys(Data.USER_NAME)
        driver.find_element(*Elements.EMAIL_INPUT).send_keys(GenerateUser.generate_email())
        driver.find_element(*Elements.PASSWORD_INPUT).send_keys(GenerateUser.generate_password())
        driver.find_element(*Elements.COMPLETE_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.presence_of_element_located(Elements.ENTER_SIGN))
        assert driver.current_url == Config.URL + 'login'

    def test_should_not_create_with_five_symbol_password(self, driver):
        driver.get(Config.URL)
        driver.find_element(*Elements.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains('/login'))
        driver.find_element(*Elements.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains('/register'))
        driver.find_element(*Elements.USERNAME_INPUT).send_keys(Data.USER_NAME)
        driver.find_element(*Elements.EMAIL_INPUT).send_keys(GenerateUser.generate_email())
        driver.find_element(*Elements.PASSWORD_INPUT).send_keys('12345')
        driver.find_element(*Elements.COMPLETE_BUTTON).click()
        assert driver.find_element(*Elements.INPUT_ERROR_MASSAGE).text == 'Некорректный пароль'
