import pytest
from selenium import webdriver




@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Firefox()
    request.cls.driver = driver
    yield
    driver.quit()