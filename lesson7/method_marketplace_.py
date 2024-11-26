# Задание: Автотест на интернет-магазин
# 1.	Откройте сайт магазина: https://www.saucedemo.com/
# 2.	Авторизуйтесь как пользователь standard_user
# 3.	Добавьте в корзину товары: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
# 4.	Перейдите в корзину
# 5.	Нажмите Checkout
# 6.	Заполните форму своими данными: имя, фамилия, почтовый индекс
# 7.	Нажмите кнопку Continue
# 8.	Прочитайте со страницы итоговую стоимость (Total)
# 9.	Закройте браузер
# 10.	Проверьте, что итоговая сумма равна $58.29

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = None

# 1. Откройте сайт магазина: https://www.saucedemo.com/
def open_page():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

# 2. Авторизуйтесь как пользователь standard_user
def authen():
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    sleep(2)

# 3. Добавьте в корзину товары: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
def add_goods():
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    
# 4. Перейдите в корзину
def go_cart():
    driver.find_element(By.CSS_SELECTOR, "[class= shopping_cart_container]").click()
    sleep(2)

# 5. Нажмите Checkout
def click_checkout():
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    sleep(2)

# 6. Заполните форму своими данными: имя, фамилия, почтовый индекс
def person_data():
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ольга")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Тимошенко")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123")
    sleep(2)

# 7. Нажмите кнопку Continue
def click_contin():
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    sleep(2)

# 8. Прочитайте со страницы итоговую стоимость (Total)
def read_total():
    total = driver.find_element(By.CSS_SELECTOR, "[class=summary_total_label]").text
    assert total == "Total: $58.29"
    print(total)
    sleep(2)
    
# 9. Закройте браузер
def close_page():
    driver.quit()

def test_marketplace():
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    open_page()
    authen()
    add_goods()
    go_cart()
    click_checkout()
    person_data()
    click_contin()
    read_total()
    close_page()
    