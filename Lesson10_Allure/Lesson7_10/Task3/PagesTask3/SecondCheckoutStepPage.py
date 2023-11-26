from selenium.webdriver.common.by import By

class SecondCheckoutPage:
    """Класс содержащий методы взаимодействия со второй страницы проверки"""

    def __init__(self, driver) -> None:
        self._driver = driver

    def get_total_cost(self) -> str:
        """Возвращает цену из значения "Total cost" """

        return self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text.partition(" ")[2]