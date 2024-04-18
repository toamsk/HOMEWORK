# Задание 1. Написать скрипт "Нажатие на кнопку"
# 1. Перейдите на страницу http://uitestingplayground.com/ajax
# 2. Нажмите на синюю кнопку
# 3. Получите текст из зеленой плашки
# 4. Выведите его в консоль *("Data loaded with AJAX get request.")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)

# Открыть страницу
driver.get("http://uitestingplayground.com/ajax")
driver.maximize_window()

# Найти и нажимам на синиюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, ("[id=ajaxButton]")).click()

# Найти элемент плашки
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

# Напечатать текст на эксран
print(txt)

driver.quit()