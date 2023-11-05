from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.common import by
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service = FireFoxService(GeckoDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element(by.By.CSS_SELECTOR, 'button.btn-primary')

try:
    blue_button.click()
    print("Blue button was clicked")
except TypeError:
    print("Exception!!!")