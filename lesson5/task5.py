# Клик по кнопке с CSS-классом
# 1. Откройте страницу http://uitestingplayground.com/classattr.
# 2. Кликните на синюю кнопку.
# 3. Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу Chrome
driver.get("http://uitestingplayground.com/classattr")
driver.maximize_window()
sleep(1)

# Запускаем скрипт три раза
for i in range(3):
    blue_button = driver.find_element(By.CLASS_NAME, value= "btn-primary").click()
    sleep(2)
    alert = Alert(driver)
    alert.accept()
    sleep(2)

# Повторение скрипта в Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Открыть страницу Firefox
driver.get("http://uitestingplayground.com/classattr")
driver.maximize_window()
sleep(1)

#Запускаем скрипт три раза
for i in range(3):
    blue_button = driver.find_element(By.CLASS_NAME, value= "btn-primary").click()
    sleep(2)
    alert = Alert(driver)
    alert.accept()
    sleep(2)

driver.quit()