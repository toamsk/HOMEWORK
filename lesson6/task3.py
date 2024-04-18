# Задание 3. Написать скрипт "Дождаться картинки"
# 1. Перейдите на сайт: https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
# 2. Дождитесь загрузки всех картинок
# 3. Получите значение атрибута src у 3-й картинки
# 4. Выведите значение в консоль

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
waiter = WebDriverWait(driver, 40)

# Открыть страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.maximize_window()

waiter.until(
    EC.all_of(EC.visibility_of_element_located((By.CSS_SELECTOR, "#compass")), EC.visibility_of_element_located((By.CSS_SELECTOR, "#calendar")),
              EC.visibility_of_element_located((By.CSS_SELECTOR, "#award")), EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape")))
)   

print(driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src"))
driver.quit()