import allure
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from locators.headers_locators import HeadersLocators
from pages.base_page import BasePage
from data import TestData
from urls import Urls

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators ()
    @allure.step('Открываем странцу Яндекс Самокат')
    def open_page(self,url):
        self.driver.get(url)
        self.open(Urls.BASE_URL)

    @allure.step('Нажимаем кнопку Заказать в хэдере страницы')
    def click_order_button_up(self):
        self.driver.find_element(*HeadersLocators.BUTTON_ORDER_UP).click()

    @allure.step('Заполняем поля формы Для кого самокат')
    def fill_order_one_1 (self, name, last_name, address, phon):
        self.fill_input(self.locators.INPUT_NAME, name)
        self.fill_input(self.locators.INPUT_LAST_NAME,last_name)
        self.fill_input(self.locators.INPUT_ADDRESS, address)
        self.fill_input(self.locators.INPUT_PHONE,phon)

    @allure.step('Выбираем станцию метро Бульвар Рокоссовского')
    def select_metro_station_1(self):
        self.driver.find_element(*OrderPageLocators.SELECT_METRO).click()
        self.driver.find_element(*OrderPageLocators.SELECT_METRO_STATION_1).click()

        self.click_on_element(self.locators.BUTTON_NEXT)

    @allure.step('Выбираем станцию метро Черкизовская')
    def select_metro_station_2(self):
        self.driver.find_element(*OrderPageLocators.SELECT_METRO).click()
        self.driver.find_element(*OrderPageLocators.SELECT_METRO_STATION_2).click()

        self.click_on_element(self.locators.BUTTON_NEXT)

    @allure.step('Вводим дату')
    def input_date(self, date):
        date_input = self.driver.find_element(*OrderPageLocators.INPUT_DATE)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    @allure.step('Выбираем срок аренды 1 сутки')
    def select_time_1(self):
        self.driver.find_element(*OrderPageLocators.SELECT_TIME).click()
        self.driver.find_element(*OrderPageLocators.SELECT_TIME_DAY_1).click()

    @allure.step('Выбираем срок аренды 2 суток')
    def select_time_2(self):
        self.driver.find_element(*OrderPageLocators.SELECT_TIME).click()
        self.driver.find_element(*OrderPageLocators.SELECT_TIME_DAY_2).click()

    @allure.step('Выбираем цвет самоката "черный жемчуг"')
    def select_scooter_color_1(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_COLOR_1).click()

    @allure.step('Выбираем цвет самоката "серая безысходность"')
    def select_scooter_color_2(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_COLOR_2).click()

    @allure.step('Вводим комментарий к заказу')
    def input_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys(comment)

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_submit_button(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_SUBMIT).click()

    @allure.step('Нажимаем кнопку "Да"')
    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_YES).click()

    def is_order_confirmed(self):
      WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(OrderPageLocators.TEXT_ORDER_CONFIRMED))

    @allure.step('Нажимаем на логотип "Яндекс"')
    def click_yandex_button(self):
        main_window_handle = self.driver.current_window_handle
        yandex_logo = self.driver.find_element(*HeadersLocators.YANDEX_LOGO)
        yandex_logo.click()

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        for window_handle in self.driver.window_handles:
            if window_handle != main_window_handle:
                self.driver.switch_to.window(window_handle)
                break

        WebDriverWait(self.driver, 10).until(EC.title_contains(TestData.DZEN_LOGO))

        WebDriverWait(self.driver, 10).until(EC.url_contains(Urls.DZEN_URL_REDIRECT))

    @allure.step('Нажимаем на логотип "Самокат"')
    def click_samocat_button(self):
        self.driver.find_element(*HeadersLocators.SAMOKAT_LOGO).click()
