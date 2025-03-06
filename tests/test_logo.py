import allure

from data import TestData
from pages.order_page import OrderPage
from urls import Urls

class TestLogo:


    def test_click_logo_redirect_to_dzen(self, driver):
        order_page = OrderPage(driver)
        order_page.open(Urls.BASE_URL)

        with allure.step("Click Yandex logo"):
            order_page.click_yandex_button()

    # Добавим ожидание перенаправления
        allure.attach(driver.current_url, name="Current URL")
        assert TestData.URL_DZEN in driver.current_url

    def test_click_logo_redirect_to_samokat(self, driver):
        order_page = OrderPage(driver)
        order_page.open(Urls.BASE_URL)
        order_page.click_samocat_button()


        assert Urls.BASE_URL == driver.current_url