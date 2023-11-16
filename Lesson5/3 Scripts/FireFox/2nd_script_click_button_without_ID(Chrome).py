from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.common import by
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service = FireFoxService(GeckoDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid")

button_without_ID = driver.find_element(by.By.CLASS_NAME, 'btn.btn-primary')

try:
    button_without_ID.click()
    print("Button was clicked")
except TypeError:
    print("Exception!!!")