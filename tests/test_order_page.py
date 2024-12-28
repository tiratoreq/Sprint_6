import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from conftest import driver
from locators.order_page_locators import Locators
from pages.order_page import OrderPage

import allure

from pages.base_page import BasePage

class TestOrderPage:

    @pytest.mark.parametrize(
        'reg_button, name, surname, address, phone, comment',
        [
            [Locators.REG_BUTTON_LOW, Constants.NAME_1, Constants.SURNAME_1, Constants.ADDRESS_1, Constants.PHONE_1, Constants.COMMENT_1],
            [Locators.REG_BUTTON_HIGH, Constants.NAME_2, Constants.SURNAME_2, Constants.ADDRESS_2, Constants.PHONE_2, Constants.COMMENT_2]
        ]
    )
    @allure.title('Проверка создания заказа, Проверка перехода на главную страницу по нажатию на логотип')
    @allure.description('На странице ищем табличку "заказ оформлен"')
    @allure.description('Проверяем переход на главную страницу с самоката после оформления заказа')
    def test_order(self, driver, reg_button, name, surname, address, phone, comment):
        order_page = BasePage(driver)
        make_order = OrderPage()
        order_page.open_page(driver, Constants.URL)
        order_page.cook(driver)
        make_order.order(driver, reg_button, name, surname, address, phone, comment)

        with allure.step('Ищем табличку "Заказ оформлен"'):
            assert driver.find_element(*Locators.ORDERED)
        with allure.step('Нажимаем кнопку "Посмотреть статус"'):
            driver.find_element(*Locators.TO_SEE_STATUS).click()
        with allure.step('Нажимаем на логотип Самоката'):
            driver.find_element(*Locators.LOGO).click()
        with allure.step('Проверяем что перешли на домашнюю страницу Самоката'):
            assert driver.current_url == Constants.SCOOTER_URL
        with allure.step('Нажимаем на логотип Яндекса'):
            driver.find_element(*Locators.LOGO_YA).click()
        with allure.step('Переходим на открывшуюся страницу яндекс Дзен'):
            driver.switch_to.window(driver.window_handles[1])
        with allure.step('Ожидаем загрузки страницы яндекс Дзен'):
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.FIND_BUTTON))
        with allure.step('Проверяем что перешли на страницу Яндекс Дзен'):
            assert driver.current_url == Constants.DZEN_URL
        order_page.quit_driver(driver)