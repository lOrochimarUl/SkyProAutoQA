import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    """Класс содержащий методы взаимодействия с главной страницей"""

    def __init__(self, driver) -> None:
        self._driver = driver

    @allure.step("Перейти на главную страницу")
    def to_main_page(self) -> None:
        """Осуществляет переход на главную страницу"""

        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить задержку {seconds} секунд")
    def set_delay (self, seconds: int) -> None:
        """
        Очищает поле "Delay" и устанавливает в него указанное значение

        :param seconds:  значение устанавливаемое в поле
        """

        self._driver.find_element(By.ID, "delay").clear()
        self._driver.find_element(By.ID, "delay").send_keys(seconds)

    @allure.step("Нажать кнопку {number}")
    def click_number_or_dot(self, number: str) -> None:
        """
        Нажимает на указанный номер или точку
        
        :param number: цифра или точка на калькуляторе
        """

        self._driver.find_element(By.XPATH, "//span[@class = 'btn btn-outline-primary'][text() = " + str(number) + "]").click()

    @allure.step("Очистить поле ввода")
    def click_clear_field(self) -> None:
        """Очищает поле ввода"""

        self._driver.find_element(By.XPATH, "//span[text() = 'C']").click()

    @allure.step("Нажать на кнопку {operator}")
    def click_operator(self, operator: str) -> None:
        """
        Нажимает на указанный оператор
        
        :param number: умножение(*), деление (\), сложение (+), вычитание(-)
        """

        self._driver.find_element(By.XPATH, "//span[@class = 'operator btn btn-outline-success'][text() = '" + str(operator) + "']").click()

    @allure.step("Нажать на кнпоку Равно")
    def click_equals(self) -> None:
        """Нажимает на указанный равно"""

        self._driver.find_element(By.XPATH, "//span[@class = 'btn btn-outline-warning'][text() = '=']").click()

    @allure.step("Пытаться получить из поля ввода значение {value}, в течение {delay} секунд")
    def get_excepted_screen_value(self, value: str, delay: int) -> None:
        """
        Ожидает появления в поле значения в пределах установленного времени. Если значение не появилось, бросает Exception
        
        :param value: ожидаемое значение

        :param delay: секунды, в течение которых ожидать появление value
        """

        WebDriverWait(self._driver, delay).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), value)
        )