from selenium.webdriver.common.by import By

class HeadersLocators:

    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")  # логотип Yandex
    SAMOKAT_LOGO = (By.XPATH, "//img[@alt='Scooter']")  # логотип Самокат
    ORDER_BUTTON = (By.XPATH, "//button[text() = 'Заказать']") # Кнопка "Заказать" в хедере