from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Calculator:
    def calculate(first_number: int, second_number: int):

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        waiter = WebDriverWait(driver, 46)

        driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")
        
        driver.find_element(By.XPATH, "//span[contains(text()," + str(first_number) +")]").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
        driver.find_element(By.XPATH, "//span[contains(text()," + str(second_number) +")]").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click()

        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), str(first_number + second_number)))
        return driver.find_element(By.CSS_SELECTOR, "div.screen").text
        
        



