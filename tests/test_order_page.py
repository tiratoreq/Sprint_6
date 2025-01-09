import pytest

from constants import Constants
from conftest import driver
from locators.order_page_locators import Locators
from pages.order_page import OrderPage

import allure

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

def test_order(driver, reg_button, name, surname, address, phone, comment):
    make_order = OrderPage(driver)
    make_order.order(driver, reg_button, name, surname, address, phone, comment)
    assert make_order.find_element(locator = Locators.ORDERED)
    make_order.click_element(locator = Locators.TO_SEE_STATUS)
    make_order.click_element(locator = Locators.LOGO)
    assert make_order.current_url(driver) == Constants.SCOOTER_URL
    make_order.click_element(locator = Locators.LOGO_YA)
    make_order.switch_to_window(driver)
    assert make_order.current_url(driver) == Constants.DZEN_URL
