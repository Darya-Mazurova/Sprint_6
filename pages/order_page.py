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
        self.driver.get(self.PAGE_URL)

    def click_order_button_headers(self):
        order_button_headers = self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_HEADERS)
        order_button_headers.click()

    def click_order_button_footer(self):
        order_button_footer = self.driver.find_element(*OrderPageLocators.ORDER_BUTTON_FOOTER)
        order_button_footer.click()

    def input_name(self, name):
        name = self.driver.find_element(*MainPageLocators.NAME_INPUT)
        name.send_keys(name)

    def input_last_name(self, last_name):
        last_name = self.driver.find_element(*MainPageLocators.LAST_NAME_INPUT)
        last_name.send_keys(last_name)

    def input_address(self, address):
        address = self.driver.find_element(*MainPageLocators.ADDRESS_INPUT)
        address.send_keys(address)

    def input_phone(self, phone):
        phone = self.driver.find_element(*MainPageLocators.PHONE_INPUT)
        phone.send_keys(phone)




