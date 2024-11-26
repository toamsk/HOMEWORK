# Задание: Автотест на заполнение формы (запускается через pytest)
# 1. Открыть страницу: https://bonigarcia.dev/selenium-webdriver-java/data-types.html
# 2. Заполнить форму 
# 3. Нажмите кнопку Submit
# 4. Проверьте (assert), что поле Zip code подсвечено красным.
# 5. Проверьте (assert), что остальные поля подсвечены зеленым.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_fill_fields():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    browser.maximize_window()

    # Заполнить форму
    browser.find_element(By.CSS_SELECTOR, ("[name=first-name]")).send_keys("Иван")
    browser.find_element(By.CSS_SELECTOR, ("[name=last-name]")).send_keys("Петров")
    browser.find_element(By.CSS_SELECTOR, ("[name=address]")).send_keys("Ленина, 55-3")
    browser.find_element(By.CSS_SELECTOR, ("[name=zip-code]")).send_keys("")
    browser.find_element(By.CSS_SELECTOR, ("[name=city]")).send_keys("Москва")
    browser.find_element(By.CSS_SELECTOR, ("[name=country]")).send_keys("Россия")
    browser.find_element(By.CSS_SELECTOR, ("[name=e-mail]")).send_keys("test@skypro.com")
    browser.find_element(By.CSS_SELECTOR, ("[name=phone]")).send_keys("+7985899998787")
    browser.find_element(By.CSS_SELECTOR, ("[name=job-position]")).send_keys("QA")
    browser.find_element(By.CSS_SELECTOR, ("[name=company]")).send_keys("SkyPro")

    # Нажать кнопку Submit
    browser.find_element(By.CSS_SELECTOR, ("[type=submit]")).click()
    sleep(3)

    # Проверка (assert), что поле Zip code подсвечено красным
    color_form = browser.find_element(By.CSS_SELECTOR, "[id=zip-code]").value_of_css_property("color")

    print(color_form)
    assert color_form == "rgba(132, 32, 41, 1)"

    elements = ["first-name", "last-name", "address", "city", "country", "e-mail", "phone", "job-position", "company"]
    for i in elements:
        other_elements = browser.find_element(By.CSS_SELECTOR, "[id=%s]" %i).value_of_css_property("color")
        assert other_elements == "rgba(15, 81, 50, 1)"
        