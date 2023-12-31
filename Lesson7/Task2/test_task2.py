import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from PagesTask2.MainPage import MainPage

@pytest.mark.l7
def test_summ():
    chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(chrome)

    main_page.to_main_page()
    main_page.set_delay(45)
    main_page.click_number_or_dot(7)
    main_page.click_operator('+')
    main_page.click_number_or_dot(8)
    main_page.click_equals()

    main_page.get_excepted_screen_value("15")