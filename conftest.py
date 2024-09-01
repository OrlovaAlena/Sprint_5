import pytest
from selenium import webdriver
from src.config import Config


@pytest.fixture(scope='function')
def driver():
    chrome = webdriver.Chrome()
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()
