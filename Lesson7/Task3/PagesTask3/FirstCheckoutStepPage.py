from selenium.webdriver.common.by import By

class FirstCheckoutPage:
    
    def __init__(self, driver) -> None:
        self._driver = driver

    def fullfill_fields(self, first_name: str, last_name: str, zip_code: str):
        self._driver.find_element(By.ID, "first-name").send_keys(first_name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(zip_code)
    
    def click_continue(self):
        self._driver.find_element(By.ID, "continue").click()

