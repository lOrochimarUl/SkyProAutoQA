from selenium.webdriver.common.by import By

class MainPage:
    """Класс содержащий методы взаимодействия с главной страницей"""

    def __init__(self, driver) -> None:
        self._driver = driver

    def to_main_page(self):
        """"Осуществляет переход на главную страницу"""

        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fullfill_fields(self, fields: list, values: list):
        """
        Заполняет указанные поля значениями из списка. Количество полей и значений должны быть равны. В ином случае 
        бросает Exception

        :param fields: список полей для заполния

        :param values: список значений для полей

        """

        if len(fields) != len(values):
            raise Exception
        
        for x in range(len(fields)):
            self._driver.find_element(By.CSS_SELECTOR, "input[name = '" + fields[x] + "']").send_keys(values[x])

    def click_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()
        


