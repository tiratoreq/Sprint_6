from selenium.webdriver.common.by import By


class Locators:
    # Локаторы часто задаваемых вопросов
    HOW_MUCH = (By.XPATH, "//div[@aria-controls ='accordion__panel-0']")
    FEW_SCOOTERS = (By.XPATH, "//div[@aria-controls ='accordion__panel-1']")
    RENT_TIME = (By.XPATH, "//div[@aria-controls ='accordion__panel-2']")
    ORDER_TODAY = (By.XPATH, "//div[@aria-controls ='accordion__panel-3']")
    ORDER_LONGER = (By.XPATH, "//div[@aria-controls ='accordion__panel-4']")
    CHARGE = (By.XPATH, "//div[@aria-controls ='accordion__panel-5']")
    ORDER_CANCEL = (By.XPATH, "//div[@aria-controls ='accordion__panel-6']")
    ABROAD_CITY = (By.XPATH, "//div[@aria-controls ='accordion__panel-7']")

    # Локаторы ответов
    HOW_MUCH_ANSWER = (By.ID, "accordion__panel-0")
    FEW_SCOOTERS_ANSWER = (By.ID, "accordion__panel-1")
    RENT_TIME_ANSWER = (By.ID, "accordion__panel-2")
    ORDER_TODAY_ANSWER = (By.ID, "accordion__panel-3")
    ORDER_LONGER_ANSWER = (By.ID, "accordion__panel-4")
    CHARGE_ANSWER = (By.ID, "accordion__panel-5")
    ORDER_CANCEL_ANSWER = (By.ID, "accordion__panel-6")
    ABROAD_CITY_ANSWER = (By.ID, "accordion__panel-7")

    # Кнопка куков
    COOKIES = (By.XPATH, "//button[@class ='App_CookieButton__3cvqF']")

