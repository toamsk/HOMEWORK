from selenium.webdriver.common.by import By
from time import sleep

class CartPage:
    def __init__(self, browser):
        self.driver = browser

# 3. Добавьте в корзину товары: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
    def add_goods(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        
# 4. Перейдите в корзину
    def go_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "[class= shopping_cart_container]").click()
        sleep(2)

# 5. Нажмите Checkout
    def click_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        sleep(2)
        