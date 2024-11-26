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

def test_marketplace():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # 3. Добавьте в корзину товары: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    sleep(1)

    # 4. Перейдите в корзину
    driver.find_element(By.CSS_SELECTOR, "[class= shopping_cart_container]").click()
    sleep(2)

    # 5. Нажмите Checkout
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    sleep(2)

    # 6. Заполните форму своими данными: имя, фамилия, почтовый индекс
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ольга")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Тимошенко")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123")
    sleep(2)

    # 7. Нажмите кнопку Continue
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    sleep(2)

# 8. Прочитайте со страницы итоговую стоимость (Total)
    total = driver.find_element(By.CSS_SELECTOR, "[class=summary_total_label]").text
    print(total)
    sleep(2)

    # 9. Закройте браузер
    driver.quit()

# 10. Проверьте, что итоговая сумма равна $58.29
    assert total == "Total: $58.29"
    print(total)