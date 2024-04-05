# Поле ввода
# 1. Открыть страницу http://the-internet.herokuapp.com/inputs
# 2. Ввести в поле текст 1000
# 3. Очистить это поле (метод clear)
# 4. Ввести в это же поле текст 999

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу Chrome
driver.get("http://the-internet.herokuapp.com/inputs")
driver.maximize_window()
sleep(2)

# Ввести в поле текст 1000
search_number = driver.find_element(By.TAG_NAME, "input")
search_number.send_keys(1000)
sleep(2)

#Очистить это поле (метод clear)
search_number.clear()
sleep(2)

# Ввести в это же поле текст 999
search_number.send_keys(999)
sleep(2)


# Повторение скрипта в Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Открыть страницу Firefox
driver.get("http://the-internet.herokuapp.com/inputs")
driver.maximize_window()
sleep(2)

# Ввести в поле текст 1000
search_number = driver.find_element(By.TAG_NAME, "input")
search_number.send_keys(1000)
sleep(2)

#Очистить это поле (метод clear)
search_number.clear()
sleep(2)

# Ввести в это же поле текст 999
search_number.send_keys(999)
sleep(2)

driver.quit()