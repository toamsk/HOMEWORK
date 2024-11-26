# Задание: Автотест на заполнение формы (запускается через pytest)
# 1. Открыть страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html
# 2. Заполнить форму 
# 3. Нажмите кнопку Submit

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


from pages.MainPage import MainPage_fill_form

def test_fill_fields():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage_fill_form(browser);
    main_page.fill()
    main_page.click_button()
   