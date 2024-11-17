# Задание 2. Написать скрипт "Переименовать кнопку"
# 1. Перейдите на сайт: http://uitestingplayground.com/textinput
# 2. Укажите в поле ввода текст SkyPro
# 3. Нажмите на синюю кнопку
# 4. Получите текст кнопки и выведите в консоль "SkyPro"

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# Открыть страницу
driver.get("http://uitestingplayground.com/textinput")
driver.maximize_window()

# В поле ввода написать текст
driver.find_element(By.CSS_SELECTOR, value = "#newButtonName").send_keys("Skypro")
#sleep(3)

# Нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
#sleep(3)

# Найти элемент плашки
content = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

# Напечатать текст на экран
print(content)

driver.quit()