from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import by
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element(by.By.CSS_SELECTOR, 'button.btn-primary')

try:
    blue_button.click()
    print("Blue button was clicked")
except TypeError:
    print("Exception!!!")