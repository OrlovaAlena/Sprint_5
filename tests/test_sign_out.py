from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.config import Config
from src.elements import Elements
from src.helpers import SignIn


class TestSignOut:

    def test_sign_out(self, driver):
        driver.get(Config.URL)
        SignIn().sign_in(driver)
        driver.find_element(*Elements.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, Config.TIMEOUT).until(expected_conditions.url_contains('/account/profile'))
        driver.find_element(*Elements.EXIT_BUTTON).click()
        WebDriverWait(driver, Config.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(Elements.CONFIRM_LOGIN_BUTTON)
        )
        assert 'login' in driver.current_url
