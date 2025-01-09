from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import NoSuchElementException, TimeoutException


from conftest import driver
from locators.main_page_locators import Locators
import allure
from selenium import webdriver

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    @allure.step('Открыть страницу: {url}')
    def open_url(self, url: str):
        self.driver.get(url)


    @allure.step("Найти элемент {locator}")
    def find_element(self, locator: tuple, timeout: int = None):
        try:
            if timeout:
                wait = WebDriverWait(self.driver, timeout)
            else:
                wait = self.wait
            element = wait.until(EC.presence_of_element_located(locator))
            return element
        except TimeoutException:
            raise TimeoutException(
                f"Элемент {locator} не найден после {timeout if timeout else 10} секунд")


    @allure.step("Нажать на элемент {locator}")
    def click_element(self, locator: tuple):
        element = self.find_element(locator)
        element.click()

    @allure.step("Ввести текст {text} в элемент {locator}")
    def send_keys(self, locator: tuple, text: str):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step('Открываем браузер Firefox')
    def init_driver(self):
        return webdriver.Firefox()

    @allure.step('Открываем страницу {page}')
    def open_page(self, driver, page):
        driver.get(page)

    @allure.step('Закрываем браузер')
    def quit_driver(self, driver):
        driver.quit()

    @allure.step('Проверяем кнопку куков и если есть нажимаем на неё')
    def cook(self, driver):
        try:
            driver.find_element(*Locators.COOKIES).click()
        except(NoSuchElementException, TimeoutException):
            pass

    @allure.step('Проверить, что текст в элементе {locator} соответствует {expected_text}')
    def assert_text(self, locator: tuple, expected_text: str, timeout: int = None):

        element = self.find_element(locator, timeout)
        actual_text = element.text
        assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}' for {locator}"


