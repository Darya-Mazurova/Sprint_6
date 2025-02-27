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

    @allure.step("Нажать кнопку Заказать в хэдере страницы" )
    def click_order_button_headers(self):
        order_button_headers = self.driver.find_element(*OrderPageLocators.ORDER_BUTTON)
        order_button_headers.click()

    @allure.step("Нажать кнопку Заказать внизу страницы")
    def click_order_button_bottom(self):
        order_button_bottom = self.driver.find_element(*MainPageLocators.BUTTON_ORDER_DOWN)
        order_button_bottom.click()

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

    @allure.step("Выбрать станцию метро")
    def select_metro_station_1(self):
        self.driver.find_element(*OrderPageLocators.SELECT_METRO).click()
        self.driver.find_element(*OrderPageLocators.SELECT_METRO_STATION_1).click()

    @allure.step("Выбрать станцию метро")
    def select_metro_station_2(self):
        self.driver.find_element(*OrderPageLocators.SELECT_METRO).click()
        self.driver.find_element(*OrderPageLocators.SELECT_METRO_STATION_2).click()

    @allure.step("Ввести номер телефона")
    def input_phone(self, phone):
        phone = self.driver.find_element(*MainPageLocators.PHONE_INPUT)
        phone.send_keys(phone)

    @allure.step("Нажать кнопку Далее")
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

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


