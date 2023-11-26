from selenium.webdriver.common.by import By

class MainPage:
    
    def __init__(self, driver) -> None:
        self._driver = driver

    def add_prodact_to_cart(self, product: str):
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-" + product).click()
    
    def click_on_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    
