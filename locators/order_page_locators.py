from selenium.webdriver.common.by import By

class Locators:
    # Локаторы кнопок регистрации заказа
    REG_BUTTON_HIGH = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    REG_BUTTON_LOW = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

    # Заполнение формы регистрации
    NAME = (By.XPATH, "//input[@placeholder= '* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder= '* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder= '* Адрес: куда привезти заказ']")
    METRO = (By.XPATH, "//input[@placeholder= '* Станция метро']")
    BULVAR = (By.XPATH, "// *[text() = 'Бульвар Рокоссовского']")
    PHONE = (By.XPATH, "//input[@placeholder= '* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[@class= 'Button_Button__ra12g Button_Middle__1CSJM']")
    CALENDAR = (By.XPATH, "//input[@placeholder= '* Когда привезти самокат']")
    DAY = (By.XPATH, "//div[@aria-label = 'Choose вторник, 26-е ноября 2024 г.']")
    HOW_LONG_FIELD = (By.XPATH, "//div[@class = 'Dropdown-placeholder']")
    HOW_LONG = (By.XPATH, "// *[text() = 'двое суток']")
    COLOR = (By.XPATH, "// *[text() = 'чёрный жемчуг']")
    COURIER_COMMENT = (By.XPATH, "//input[@placeholder= 'Комментарий для курьера']")
    # Подтверждение заказа
    ORDER_BUTTON = (By.XPATH, "//button[@class= 'Button_Button__ra12g Button_Middle__1CSJM']")
    ORDER_BUTTON_YES = (By.XPATH, "// *[text() = 'Да']")

    # Локаторы для проверок ассертов
    ORDERED = (By.XPATH, "// *[text() = 'Заказ оформлен']")
    TO_SEE_STATUS = (By.XPATH, "// *[text() = 'Посмотреть статус']")
    LOGO = (By.XPATH, "//a[@class = 'Header_LogoScooter__3lsAR']")
    LOGO_YA = (By.XPATH, "//img[@src = '/assets/ya.svg']")
    FIND_BUTTON = (By.XPATH, "// *[text() = 'Найти']")
