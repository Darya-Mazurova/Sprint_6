import allure
from data import TestData
from pages.order_page import OrderPage
from urls import Urls


def test_order_page(driver):
    order_page = OrderPage(driver, Urls.PAGE_URL)
    order_page.open()
    order_page.click_order_button_headers.click()



