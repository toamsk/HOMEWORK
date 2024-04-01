# Клик по кнопке без ID
# 1. Откройте страницу http://uitestingplayground.com/dynamicid
# 2. Кликните на синюю кнопку.
# 3. Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def click_button():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу Chrome
    driver.get("http://uitestingplayground.com/dynamicid")
    driver.maximize_window()
    sleep(2)

# Кликнуть на синюю кнопку
    blue_element = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    blue_element.click()
    sleep(2)
    driver.quit()

# Запускаем функцию три раза
for i in range(3):
    click_button()

# Повторение скрипта в Firefox
def click_button():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()

# Открыть страницу Firefox
    driver.get("http://uitestingplayground.com/dynamicid")
    driver.maximize_window()
    sleep(1)

# Кликнуть на синюю кнопку
    blue_element = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    blue_element.click()
    sleep(1)
    driver.quit()

# Запускаем функцию три раза
for i in range(3):
    click_button()