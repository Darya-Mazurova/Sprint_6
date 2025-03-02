import allure

from pages.order_page import OrderPage
from data import TestData
from urls import Urls

@allure.feature("Order Page")
class TestOrderPage:
    @allure.title("Make order one")
    def test_make_order_one(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.BASE_URL)
        order_page.click_order_button_up()
        order_page.fill_order_one_1(TestData.NAME,TestData.LAST_NAME,TestData.ADDRESS,TestData.PHONE)
        order_page.select_metro_station_1()
        order_page.input_date(TestData.DATE)
        order_page.select_time_1()
        order_page.select_scooter_color_1()
        order_page.input_comment(TestData.COMMENT)
        order_page.click_submit_button()
        order_page.click_yes_button()
        order_page.is_order_confirmed()

        assert "Заказ оформлен" in driver.page_source

    @allure.title("Make order two")
    def test_make_order_two(self, driver):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.BASE_URL)
        order_page.click_order_button_up()
        order_page.fill_order_one_1(TestData.NAME_1, TestData.LAST_NAME_1, TestData.ADDRESS_1, TestData.PHONE_1)
        order_page.select_metro_station_2()
        order_page.input_date(TestData.DATE_1)
        order_page.select_time_2()
        order_page.select_scooter_color_2()
        order_page.input_comment(TestData.COMMENT_1)
        order_page.click_submit_button()
        order_page.click_yes_button()
        order_page.is_order_confirmed()

        assert "Заказ оформлен" in driver.page_source




