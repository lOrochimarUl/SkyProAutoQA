from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self, driver) -> None:
        self._driver = driver

    def to_main_page(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay (self, seconds: int):
        self._driver.find_element(By.ID, "delay").clear()
        self._driver.find_element(By.ID, "delay").send_keys(seconds)

    def click_number_or_dot(self, number: str):
        self._driver.find_element(By.XPATH, "//span[@class = 'btn btn-outline-primary'][text() = " + str(number) + "]").click()

    def click_clear_field(self):
        self._driver.find_element(By.XPATH, "//span[text() = 'C']").click()

    def click_operator(self, operator: str):
        self._driver.find_element(By.XPATH, "//span[@class = 'operator btn btn-outline-success'][text() = '" + str(operator) + "']").click()

    def click_equals(self):
        self._driver.find_element(By.XPATH, "//span[@class = 'btn btn-outline-warning'][text() = '=']").click()

    def get_excepted_screen_value(self, value: str):
        WebDriverWait(self._driver, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), value)
        )