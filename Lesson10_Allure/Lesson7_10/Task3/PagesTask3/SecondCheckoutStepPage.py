from selenium.webdriver.common.by import By

class SecondCheckoutPage:
    
    def __init__(self, driver) -> None:
        self._driver = driver

    def get_total_cost(self):
        return self._driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text.partition(" ")[2]