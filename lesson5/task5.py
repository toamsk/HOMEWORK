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

#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def repeat_three_timses():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу Chrome
    driver.get("http://uitestingplayground.com/classattr")
    driver.maximize_window()
    sleep(3)

# Кликните на синюю кнопку
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()
    sleep(3)
    driver.quit()

# Запускаем скрипт три раза
for i in range(3):
    repeat_three_timses()


# Повторение скрипта в Firefox
def repeat_three_timses():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Открыть страницу Firefox
    driver.get("http://uitestingplayground.com/classattr")
    driver.maximize_window()
    sleep(3)

# Кликните на синюю кнопку
    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()
    sleep(3)
    driver.quit()

# Запускаем скрипт три раза
for i in range(3):
    repeat_three_timses()
