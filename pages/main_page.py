import allure

from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Выбор вопроса')
    def question_selection(self, element):
        self.click_element(locator=element)