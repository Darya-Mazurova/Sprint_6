from selenium.webdriver.common.by import By


class Urls:
    PAGE_URL = "https://qa-scooter.praktikum-services.ru/" # url главной страницы
    ORDER_BUTTON = (By.XPATH, "//button[text() = 'Заказать']")
