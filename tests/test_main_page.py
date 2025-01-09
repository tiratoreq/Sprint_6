import pytest

from conftest import driver
from locators.main_page_locators import Locators
from constants import Constants

import allure

from pages.main_page import MainPage


@pytest.mark.parametrize(
    'element, answer, text_in',
    [
        [Locators.HOW_MUCH, Locators.HOW_MUCH_ANSWER, Constants.QNA_TEXT_PRICE],
        [Locators.FEW_SCOOTERS, Locators.FEW_SCOOTERS_ANSWER, Constants.QNA_FEW_SCOOTERS],
        [Locators.RENT_TIME, Locators.RENT_TIME_ANSWER, Constants.QNA_RENT_TIME],
        [Locators.ORDER_TODAY, Locators.ORDER_TODAY_ANSWER, Constants.QNA_ORDER_TODAY],
        [Locators.ORDER_LONGER, Locators.ORDER_LONGER_ANSWER, Constants.QNA_ORDER_LONGER],
        [Locators.CHARGE, Locators.CHARGE_ANSWER, Constants.QNA_CHARGE],
        [Locators.ORDER_CANCEL, Locators.ORDER_CANCEL_ANSWER, Constants.QNA_ORDER_CANCEL],
        [Locators.ABROAD_CITY, Locators.ABROAD_CITY_ANSWER, Constants.QNA_ABROAD_CITY]
    ]
)
@allure.title('Проверка нажатия на вопрос из раздела "вопросы о важном"')
@allure.description("На странице ищем элемент с текстом ответа")

def test_check_qna(driver, element, answer, text_in):
    main_page = MainPage(driver)
    main_page.open_page(driver, Constants.URL)
    main_page.cook(driver)
    main_page.question_selection(element)
    answer = main_page.find_element(locator = answer)
    with allure.step("На странице ищем элемент с текстом ответа"):
        allure.attach(
            f"На странице ищем элемент с текстом ответа {text_in} он соответствует '{answer.text}'",
            name="Проверка открытия ответа",
            attachment_type=allure.attachment_type.TEXT
        )
        assert answer.text == text_in, "Условие не выполнено"
