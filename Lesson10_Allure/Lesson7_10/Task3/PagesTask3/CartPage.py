from selenium.webdriver.common.by import By

class CartPage:
    """Класс содержащий методы взаимодействия со страницей корзины"""

    def __init__(self, driver) -> None:
        self._driver = driver

    def click_checkout(self) -> None:
        """Нажимает на кнопку "Checkout" """

        self._driver.find_element(By.ID, "checkout").click()
