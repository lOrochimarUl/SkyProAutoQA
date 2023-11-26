from selenium.webdriver.common.by import By

class LoginPage:
    """Класс содержащий методы взаимодействия со страницей авторизации"""

    def __init__(self, driver) -> None:
        self._driver = driver

    def to_login_page(self) -> None:
        """Осуществляет перехо на страницу авторизации"""

        self._driver.get("https://www.saucedemo.com/")

    def auth_stand_user(self) -> None:
        """Вводит в поля "login" и "password" соответствующие данные стандартного пользователя и нажимает кнопку "Log in" """

        self._driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self._driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self._driver.find_element(By.ID, "login-button").click()