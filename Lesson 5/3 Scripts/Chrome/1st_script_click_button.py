from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import by
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

add_button = driver.find_element(by.By.CSS_SELECTOR, '[onclick = "addElement()"]')

for x in range (5):
    add_button.click()
    print("Button was clicked " + str(x + 1) + " times")

print("Added elements on the page: " + str(len(driver.find_elements(by.By.CLASS_NAME, 'added-manually'))))