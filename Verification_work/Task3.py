from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Sauce:
    def want_sauce():
        driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.saucedemo.com/")


        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys("Alexandr")
        driver.find_element(By.ID, "last-name").send_keys("Byk")
        driver.find_element(By.ID, "postal-code").send_keys("000000")

        driver.find_element(By.ID, "continue").click()
        cost = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label").text.partition(":")[2]

        driver.close()
        return cost
        
        
        
        
        