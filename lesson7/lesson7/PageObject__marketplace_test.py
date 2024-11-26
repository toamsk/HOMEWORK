# Задание: Автотест на интернет-магазин
# 1.	Откройте сайт магазина: https://www.saucedemo.com/
# 2.	Авторизуйтесь как пользователь standard_user
# 3.	Добавьте в корзину товары: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
# 4.	Перейдите в корзину
# 5.	Нажмите Checkout
# 6.	Заполните форму своими данными: имя, фамилия, почтовый индекс
# 7.	Нажмите кнопку Continue

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.MainPage import MainPage_marketplace
from pages.CartPage import CartPage
from pages.FilForm import FilForm

def test_marketplace():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage_marketplace(browser);
    main_page.authen()
    
    cart_page = CartPage(browser);
    cart_page.add_goods()
    cart_page.go_cart()
    cart_page.click_checkout()

    fil_form = FilForm(browser);
    fil_form.person_data()
    fil_form.click_contin()


