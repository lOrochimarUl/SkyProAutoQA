import allure
from selenium.webdriver.common.by import By

class ResultPage:
    """Класс содержащий методы взаимодействия со страницей результатов"""

    def __init__(self, driver) -> None:
        self._driver = driver
    
    @allure.step("Получить цвет фона объекта")
    def check_field_color(self, id: str) -> str:
        """
        Возвращает цвет фона элемента

        :param id: id веб-элемента
        """

        return self._driver.find_element(By.ID, id).value_of_css_property("background-color")
    

    
