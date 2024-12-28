from selenium.common import NoSuchElementException, TimeoutException

from conftest import driver
from locators.main_page_locators import Locators
import allure
from selenium import webdriver


class BasePage:

    def __init__(self, driver):
        self.driver = driver


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
