from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import by
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid")

button_without_ID = driver.find_element(by.By.CLASS_NAME, 'btn.btn-primary')

try:
    button_without_ID.click()
    print("Button was clicked")
except TypeError:
    print("Exception!!!")

