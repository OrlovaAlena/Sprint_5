from src.config import Config
from src.elements import Elements


class TestSectionSwitch:
    def test_sauces_tab(self, driver):
        driver.get(Config.URL)
        driver.find_element(*Elements.SAUCES_TAB).click()
        assert Elements.SAUCES_SELECTED

    def test_fillings_tab(self, driver):
        driver.get(Config.URL)
        driver.find_element(*Elements.FILLINGS_TAB).click()
        assert Elements.FILLINGS_SELECTED

    def test_buns_tab(self, driver):
        driver.get(Config.URL)
        driver.find_element(*Elements.SAUCES_TAB).click()
        driver.find_element(*Elements.BUNS_TAB)
        assert Elements.BUNS_SELECTED
