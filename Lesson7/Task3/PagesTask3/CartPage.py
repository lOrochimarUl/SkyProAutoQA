from selenium.webdriver.common.by import By

class CartPage:
    
    def __init__(self, driver) -> None:
        self._driver = driver

    def click_checkout(self):
        self._driver.find_element(By.ID, "checkout").click()
