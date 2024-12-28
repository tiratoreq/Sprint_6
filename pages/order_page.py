import allure
from locators.order_page_locators import Locators


class OrderPage:

    @staticmethod
    def order(driver, reg_button, name, surname, address, phone, comment):
        with allure.step('Выбираем кнопку для регистрации заказа и нажимаем ее'):
            driver.find_element(*reg_button).click()
        with allure.step(f"Вводим имя: {name}"):
            driver.find_element(*Locators.NAME).send_keys(name)
        with allure.step(f"Вводим фамилию: {surname}"):
            driver.find_element(*Locators.SURNAME).send_keys(surname)
        with allure.step(f"Указываем адрес: {address}"):
            driver.find_element(*Locators.ADDRESS).send_keys(address)
        with allure.step('выбираем станцию метро'):
            driver.find_element(*Locators.METRO).click()
            driver.find_element(*Locators.BULVAR).click()
        with allure.step(f"Указываем номер телефона: {phone}"):
            driver.find_element(*Locators.PHONE).send_keys(phone)
            driver.find_element(*Locators.NEXT_BUTTON).click()
        with allure.step('Указываем дату для доставки'):
            driver.find_element(*Locators.CALENDAR).click()
            driver.find_element(*Locators.DAY).click()
        with allure.step('Выбираем срок'):
            driver.find_element(*Locators.HOW_LONG_FIELD).click()
            driver.find_element(*Locators.HOW_LONG).click()
        with allure.step('Выбираем цвет'):
            driver.find_element(*Locators.COLOR).click()
        with allure.step(f"Пишем комментарий: {comment}"):
            driver.find_element(*Locators.COURIER_COMMENT).send_keys(comment)
        with allure.step('Подтверждаем заказ'):
            driver.find_element(*Locators.ORDER_BUTTON).click()
            driver.find_element(*Locators.ORDER_BUTTON_YES).click()
