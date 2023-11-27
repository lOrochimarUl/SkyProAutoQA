import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from PagesTask3.LoginPage import LoginPage
from PagesTask3.MainPage import MainPage
from PagesTask3.CartPage  import CartPage
from PagesTask3.FirstCheckoutStepPage import FirstCheckoutPage
from PagesTask3.SecondCheckoutStepPage import SecondCheckoutPage

product_list = ["backpack", "bolt-t-shirt", "onesie"]
checkout_values_list = ["Alexandr", "Byk", "000000"]

@allure.title("Получение общей цены товаров")
@allure.description("Соответствие суммы чисел товаров в корзине фактическому результату")
@allure.feature("Something")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.l7_10
def test_summ():
    
    chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    login_page = LoginPage(chrome)
    main_page = MainPage(chrome)
    cart_page = CartPage(chrome)
    first_checkout_page = FirstCheckoutPage(chrome)
    second_checkout_page = SecondCheckoutPage(chrome)

    login_page.to_login_page()
    login_page.auth_stand_user()

    for x in range(len(product_list)):
        main_page.add_prodact_to_cart(product_list[x])
    main_page.click_on_cart()

    cart_page.click_checkout()

    first_checkout_page.fullfill_fields(product_list[0], product_list[1], product_list[2])
    first_checkout_page.click_continue()

    assert second_checkout_page.get_total_cost() == "$58.29"

    

