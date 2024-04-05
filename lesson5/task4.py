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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу Chrome
driver.get("http://uitestingplayground.com/dynamicid")
driver.maximize_window()
sleep(2)

# Кликнуть на синюю кнопку
blue_element = driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]')

for i in range(3):
    blue_element.click()
    sleep(1)
    # проверка нажатия трех раз на кнопку
    #blue_element.send_keys(Keys.TAB)

# Повторение скрипта в Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Открыть страницу Firefox
driver.get("http://uitestingplayground.com/dynamicid")
driver.maximize_window()
sleep(2)

# Кликнуть на синюю кнопку
blue_element = driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]')

for i in range(3):
    blue_element.click()
    sleep(1)
    # проверка нажатия трех раз на кнопку
    #blue_element.send_keys(Keys.TAB)

driver.quit()