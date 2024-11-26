# Задание: Автотест на калькулятор (запускается через pytest)
# 1. Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
# 2. В поле ввода по локатору #delay введите значение 45
# 3. Нажать на кнопки: 7, +, 8, =

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.MainPage import MainPage_calculator

def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage_calculator(browser)
    main_page.delay(45)
    main_page.click_num()

