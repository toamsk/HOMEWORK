# Задание: Автотест на калькулятор (запускается через pytest)
# 1. Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
# 2. В поле ввода по локатору #delay введите значение 45
# 3. Нажать на кнопки: 7, +, 8, =
# 4. Проверить (assert), что в окне отобразится результат 15 через 45 секунд

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # 1. Открыть страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()
        
    # 2. В поле ввода по локатору #delay очистить и затем ввести значение 45
    driver.find_element(By.CSS_SELECTOR, "[id=delay]").clear()
    driver.find_element(By.CSS_SELECTOR, "[id=delay]").send_keys(45)

    # 3. Нажать на кнопки: 7, +, 8, =
    driver.find_element(By.XPATH, ('//span[text()="7"]')).click()
    driver.find_element(By.XPATH, ('//span[text()="+"]')).click()
    driver.find_element(By.XPATH, ('//span[text()="8"]')).click()
    driver.find_element(By.XPATH, ('//span[text()="="]')).click()

    # 4. Проверить (assert), что в окне отобразится результат 15 через 45 секунд
    result = WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element ((By.CLASS_NAME, "screen"), "15"))
    assert result == "15"
    print(result)

    driver.quit()