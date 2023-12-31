from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver) -> None:
        self._driver = driver

    def to_main_page(self):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fullfill_fields(self, fields: list, values: list):
        for x in range(len(fields)):
            self._driver.find_element(By.CSS_SELECTOR, "input[name = '" + fields[x] + "']").send_keys(values[x])

    def click_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()
        


