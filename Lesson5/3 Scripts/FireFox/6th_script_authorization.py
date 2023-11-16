from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.common import by
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

driver = webdriver.Firefox(service=FireFoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

login = driver.find_element(by.By.CSS_SELECTOR, "div input#username")
login.send_keys("tomsmith")

password = driver.find_element(by.By.CSS_SELECTOR, "div input#password")
password.send_keys("SuperSecretPassword!")

button = driver.find_element(by.By.CSS_SELECTOR, "button.radius")
button.click()
sleep(7)