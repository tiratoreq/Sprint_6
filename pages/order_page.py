import allure
from selenium.webdriver.support.wait import WebDriverWait

from constants import Constants
from locators.order_page_locators import Locators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнить форму заказа")
    def order(self, driver, reg_button, name, surname, address, phone, comment):
        order_page = BasePage(driver)
        order_page.open_page(driver, Constants.URL)
        order_page.cook(driver)
        self.click_element(locator = reg_button)
        self.send_keys(locator = Locators.NAME, text = name)
        self.send_keys(locator = Locators.SURNAME, text = surname)
        self.send_keys(locator = Locators.ADDRESS, text = address)
        self.click_element(locator = Locators.METRO)
        self.click_element(locator = Locators.BULVAR)
        self.send_keys(locator = Locators.PHONE, text = phone)
        self.click_element(locator = Locators.NEXT_BUTTON)
        self.click_element(locator = Locators.CALENDAR)
        self.click_element(locator = Locators.DAY)
        self.click_element(locator = Locators.HOW_LONG_FIELD)
        self.click_element(locator = Locators.HOW_LONG)
        self.click_element(locator = Locators.COLOR)
        self.send_keys(locator = Locators.COURIER_COMMENT, text = comment)
        self.click_element(locator = Locators.ORDER_BUTTON)
        self.click_element(locator = Locators.ORDER_BUTTON_YES)

    @allure.step('Перейти на новое окно')
    def switch_to_window(self, driver):
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.FIND_BUTTON))

    @allure.step('Получаем текущий адрес страницы')
    def current_url(self, driver):
        url = driver.current_url
        return url

