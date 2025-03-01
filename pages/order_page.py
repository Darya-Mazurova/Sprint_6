import allure
from Locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from Locators.main_page_locators import MainPageLocators
from Locators.headers_locators import HeadersLocators
from pages.base_page import BasePage
from data import TestData
from urls import Urls

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()


    def open_page(self):
        self.get(Urls.PAGE_URL)

    @allure.step("Нажать кнопку Заказать в хэдере страницы" )
    def click_order_button_headers(self):
        order_button_headers = self.driver.find_element(*OrderPageLocators.ORDER_BUTTON)
        order_button_headers.click()

    @allure.step("Нажать кнопку Заказать внизу страницы")
    def click_order_button_bottom(self):
        order_button_bottom = self.driver.find_element(*MainPageLocators.BUTTON_ORDER_DOWN)
        order_button_bottom.click()

    def place_an_order_1(self,name,last_name,address,phone):
        self.fill_input(self.locators.INPUT_NAME, name)
        self.fill_input(self.locators.INPUT_LAST_NAME, last_name)
        self.fill_input(self.locators.INPUT_ADDRESS, address)
        self.fill_input(self.locators.INPUT_PHONE, phone)


        self.click_on_element(self.locators.BUTTON_NEXT)














    @allure.step("Ввести имя")
    def input_name(self, name):
        name = self.driver.find_element(*MainPageLocators.INPUT_NAME)
        name.send_keys(name)

    @allure.step("Ввести фамилию")
    def input_last_name(self, last_name):
        last_name = self.driver.find_element(*MainPageLocators.INPUT_LAST_NAME)
        last_name.send_keys(last_name)

    @allure.step("Ввести адрес")
    def input_address(self, address):
        address = self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS)
        address.send_keys(address)

    @allure.step("Выбрать станцию метро 1")
    def select_metro_station_1(self):
        metro_station = self.driver.find_element(*OrderPageLocators.SELECT_METRO)
        metro_station.click()
        metro_station_1 = self.driver.find_element(*OrderPageLocators.METRO_STATION_1)
        metro_station_1.click()

    @allure.step("Выбрать станцию метро 2")
    def select_metro_station_2(self):
        metro_station = self.driver.find_element(*OrderPageLocators.SELECT_METRO)
        metro_station.click()
        metro_station_1 = self.driver.find_element(*OrderPageLocators.METRO_STATION_2)
        metro_station_1.click()

    @allure.step("Ввести номер телефона")
    def input_phone(self, phone):
        phone = self.driver.find_element(*OrderPageLocators.INPUT_PHONE)
        phone.send_keys(phone)

    @allure.step("Нажать кнопку Далее")
    def click_next_button(self):
        next_button = self.driver.find_element(*OrderPageLocators.BUTTON_NEXT)
        next_button.click()


    @allure.step("Выбрать дату")
    def input_date(self, date):
        date_input = self.driver.find_element(*OrderPageLocators.INPUT_DATE)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    @allure.step("Выбрать срок аренды")
    def select_time_1(self):
        self.driver.find_element(*OrderPageLocators.SELECT_TIME).click()
        self.driver.find_element(*OrderPageLocators.SELECT_TIME_DAY_1).click()

    @allure.step("Выбрать срок аренды")
    def select_time_2(self):
        self.driver.find_element(*OrderPageLocators.SELECT_TIME).click()
        self.driver.find_element(*OrderPageLocators.SELECT_TIME_DAY_2).click()

    @allure.step("Выбрать цвет самоката")
    def select_scooter_color_1(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_COLOR_1).click()

    @allure.step("Выбрать цвет самоката")
    def select_scooter_color_2(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_COLOR_2).click()

    @allure.step("Ввести комментарий")
    def input_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys(comment)

    @allure.step("Нажать кнопку Заказать ")
    def click_submit_button(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_SUBMIT).click()

    @allure.step("Нажать кнопку Да")
    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_YES).click()

    @allure.step("Сообщение об успешно заказе")
    def is_order_confirmed (self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.TEXT_ORDER_CONFIRMED))

    @allure.step("Click Yandex logo")
    def click_yandex_button(self):
        # Сохраняем текущее окно
        main_window_handle = self.driver.current_window_handle

        yandex_logo = self.driver.find_element(*HeadersLocators.YANDEX_LOGO)
        yandex_logo.click()

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        for window_handle in self.driver.window_handles:
            if window_handle != main_window_handle:
                self.driver.switch_to.window(window_handle)
                break

        WebDriverWait(self.driver, 10).until(EC.title_contains(TestData.DZEN_LOGO))

        WebDriverWait(self.driver, 10).until(EC.url_contains(TestData.DZEN_URL_REDIRECT))

    @allure.step("Click Samokat logo")
    def click_samocat_button(self):
        self.driver.find_element(*HeadersLocators.SAMOKAT_LOGO).click()

