import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from PagesTask1.MainPage import MainPage
from PagesTask1.ResultPage import ResultPage

red_color = 'rgba(248, 215, 218, 1)'
green_color = 'rgba(209, 231, 221, 1)'
list_of_fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
list_of_values = ["Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro"]


@allure.title("Подсветка красным уветом незаполненных полей")
@allure.description("Незаполненное поле zip-code подсвечивается красным")
@allure.feature("Something")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.l7_10
def test_red_color_field():

    chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_page = MainPage(chrome)
    result_page = ResultPage(chrome) 

    main_page.to_main_page()
    main_page.fullfill_fields(list_of_fields, list_of_values)
    main_page.click_submit()

    assert result_page.check_field_color("zip-code") == red_color


@allure.title("Подсветка зелёным цветом заполненных полей")
@allure.description("Заполненные поля подсвечивается зелёным")
@allure.feature("Something")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.l7_10
def test_green_color_fields():
 
        chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        main_page = MainPage(chrome)
        result_page = ResultPage(chrome) 

        main_page.to_main_page()
        main_page.fullfill_fields(list_of_fields, list_of_values)
        main_page.click_submit()

        for x in range(len(list_of_fields)):
            assert result_page.check_field_color(list_of_fields[x]) == green_color








