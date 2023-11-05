from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.common import by
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

driver = webdriver.Firefox(service=FireFoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
input = driver.find_element(by.By.CSS_SELECTOR, "div input")

input.send_keys("1000")
sleep(2)

input.clear()
sleep(2)

input.send_keys(999)
sleep(2)