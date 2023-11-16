from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.common import by
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

driver = webdriver.Firefox(service = FireFoxService(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/entry_ad")

#Добавил sleep, чтобы модальное окно успело загрузиться до клика
sleep(5) 

close_button = driver.find_element(by.By.CSS_SELECTOR, "div.modal-footer p")

try:
    close_button.click()
    print("Close button was clicked")
except TypeError:
    print("Exception!!!")