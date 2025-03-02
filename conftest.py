import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from urls import Urls


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.headless = False
    driver = webdriver.Firefox(options=options)
    driver.get(Urls.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()




