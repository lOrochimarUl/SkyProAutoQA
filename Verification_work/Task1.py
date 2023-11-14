from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Form:
    def filling_form_uncompletely(green_color: str, red_color: str):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        list_of_fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
        list_of_values = ["Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro"]


        for x in range(len(list_of_fields)):
            driver.find_element(By.CSS_SELECTOR, "input[name = '" + list_of_fields[x] + "']").send_keys(list_of_values[x])
        driver.find_element(By.CSS_SELECTOR, "button[type = 'submit']").click()
        is_red = red_color == driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")

        is_green = True
        count = -1
        while is_green == True and count < len(list_of_fields):
            is_green = driver.find_element(By.CSS_SELECTOR, "#"+ list_of_fields[count]).value_of_css_property("background-color") == green_color
            count = count + 1
        
        return [is_red, is_green]
        


