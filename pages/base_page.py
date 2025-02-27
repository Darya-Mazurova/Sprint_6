from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


class BasePage:


    def __init__(self, driver):
        self.driver: WebDriver= driver

    @allur.step("Открыть страницу")
    def open(self):
        self.driver.get(self.PAGE_URL) # Открыть страницу

    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)) # найти элемент

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.scroll_into_view(element)
            element.click() # кликнуть на элемент

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text # получить текст из элемента

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text) # установить текст в элемент

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element) #скролл страницы
