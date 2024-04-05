# Форма авторизации
# 1. Откройте страницу http://the-internet.herokuapp.com/login
# 2. В поле username введите значение tomsmith
# 3. В поле password введите значение SuperSecretPassword!
# 4. Нажмите кнопку Login

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу Chrome
driver.get("http://the-internet.herokuapp.com/login")
driver.maximize_window()
sleep(2)

# В поле username введите значение tomsmith
search_username = driver.find_element(By.ID, value="username").send_keys("tomsmith")
sleep(2)

# Найти поле ввода для пароля и ввести значение
password_field = driver.find_element(By.ID, value="password").send_keys("SuperSecretPassword!")
sleep(2)

# Найти кнопку Login и нажать на неё
login_button = driver.find_element(By.XPATH, value="//button[@type='submit']").click()
sleep(2)


# Повторение скрипта в Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Открыть страницу Firefox
driver.get("http://the-internet.herokuapp.com/login")
driver.maximize_window()
sleep(2)

# В поле username введите значение tomsmith
search_username = driver.find_element(By.ID, value="username").send_keys("tomsmith")
sleep(2)

# Найти поле ввода для пароля и ввести значение
password_field = driver.find_element(By.ID, value="password").send_keys("SuperSecretPassword!")
sleep(2)

# Найти кнопку Login и нажать на неё
login_button = driver.find_element(By.XPATH, value="//button[@type='submit']").click()
sleep(2)

driver.quit()