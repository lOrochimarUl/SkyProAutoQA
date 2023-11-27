import allure
from selenium.webdriver.common.by import By

class MainPage:
    """Класс содержащий методы взаимодействия с главной страницей"""

    def __init__(self, driver) -> None:
        self._driver = driver

    @allure.step("Добавить товар \"{product}\" в корзину")
    def add_prodact_to_cart(self, product: str) -> None:
        """
        Нажимает на кнопку "Добавить в корзину" указанного товара

        :param product: название товара
        """

        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-" + product).click()
        
    @allure.step("Нажать на корзину")
    def click_on_cart(self) -> None:
        """Нажимает на кнопку "Корзина" """

        self._driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    
