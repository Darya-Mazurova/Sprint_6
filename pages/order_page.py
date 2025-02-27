import allure
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from locators.main_page_locators import MainPageLocators
from locators.headers_locators import HeadersLocators
from pages.base_page import BasePage
from data import TestData, Urls

class OrderPage(BasePage):
    def open_page(self, url):
        self.driver.get(url)