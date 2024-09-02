from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.config import Config
from src.elements import Elements


class TestSignIn:

    def test_open_page(self, driver):
        driver.get(Config.URL)
        assert driver.current_url == Config.URL

    def test_sign_in_from_personal_account(self, driver):
        driver.get(Config.URL)
        driver.find_element(*Elements.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(Elements.CONFIRM_LOGIN_BUTTON)
        )
        assert 'login' in driver.current_url

    def test_sign_in_from_sign_up_page(self, driver):
        driver.get(Config.URL)
        driver.find_element(*Elements.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains('/login'))
        driver.find_element(*Elements.CREATE_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains('/register'))
        driver.find_element(*Elements.LOG_IN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(Elements.CONFIRM_LOGIN_BUTTON)
        )
        assert 'login' in driver.current_url

    def test_sign_in_from_restore_password_page(self, driver):
        driver.get(Config.URL)
        driver.find_element(*Elements.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains('/login'))
        driver.find_element(*Elements.PASSWORD_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains('/forgot-password'))
        driver.find_element(*Elements.LOG_IN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(Elements.CONFIRM_LOGIN_BUTTON)
        )
        assert 'login' in driver.current_url

    def test_sign_in_from_main_page(self, driver):
        driver.get(Config.URL)
        driver.find_element(*Elements.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(Elements.CONFIRM_LOGIN_BUTTON)
        )
        assert 'login' in driver.current_url
