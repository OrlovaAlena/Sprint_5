from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.config import Config
from src.data import Data
from src.elements import Elements


class TestLogOut:

    def test_sign_out(self, driver):
        driver.get(Config.URL)
        driver.find_element(*Elements.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains('/login'))

        driver.find_element(*Elements.EMAIL_INPUT).send_keys(Data.EMAIL)
        driver.find_element(*Elements.PASSWORD_INPUT).send_keys(Data.PASSWORD)
        driver.find_element(*Elements.COMPLETE_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_to_be(Config.URL))

        driver.find_element(*Elements.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains('/account/profile'))

        driver.find_element(*Elements.EXIT_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains('/login'))
        assert Elements.ENTER_SIGN
