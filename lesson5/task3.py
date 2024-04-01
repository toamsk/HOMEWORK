# Клик по кнопке
# 1. Открыть страницу http://the-internet.herokuapp.com/add_remove_elements/.
# 2. Пять раз кликнуть на кнопку Add Element.
# 3. Собрать со страницы список кнопок Delete.
# 4. Вывести на экран размер списка.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу Chrome
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
driver.maximize_window()
sleep(1)

# Пять раз кликнуть на кнопку Add Element
add_element = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
for i in range(5):
    add_element.click()
sleep(1)

# Собираем список кнопок "Delete"
delete_buttons = driver.find_elements(By.XPATH, '//button[text()="Delete"]')

# Выводим размер списка на экран
print(f'Количество кнопок Delete на странице Chrome: {len(delete_buttons)}')
driver.quit()

# Повторение скрипта в Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# Открыть страницу Firefox
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
driver.maximize_window()
sleep(1)

# Пять раз кликнуть на кнопку Add Element
add_element = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
for i in range(5):
    add_element.click()
sleep(1)

# Собираем список кнопок "Delete"
delete_buttons = driver.find_elements(By.XPATH, '//button[text()="Delete"]')

# Выводим размер списка на экран
print(f'Количество кнопок Delete на странице Firefox: {len(delete_buttons)}')

driver.quit()