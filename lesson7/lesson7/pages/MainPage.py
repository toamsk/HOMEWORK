from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage_fill_form:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()

# Заполнить форму
    def fill(self):
        self.driver.find_element(By.CSS_SELECTOR, ("[name=first-name]")).send_keys("Иван")
        self.driver.find_element(By.CSS_SELECTOR, ("[name=last-name]")).send_keys("Петров")
        self.driver.find_element(By.CSS_SELECTOR, ("[name=address]")).send_keys("Ленина, 55-3")
        self.driver.find_element(By.CSS_SELECTOR, ("[name=zip-code]")).send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, ("[name=city]")).send_keys("Москва")
        self.driver.find_element(By.CSS_SELECTOR, ("[name=country]")).send_keys("Россия")
        self.driver.find_element(By.CSS_SELECTOR, ("[name=e-mail]")).send_keys("test@skypro.com")
        self.driver.find_element(By.CSS_SELECTOR, ("[name=phone]")).send_keys("+7985899998787")
        self.driver.find_element(By.CSS_SELECTOR, ("[name=job-position]")).send_keys("QA")
        self.driver.find_element(By.CSS_SELECTOR, ("[name=company]")).send_keys("SkyPro")
    
# Нажать кнопку Submit
    def click_button(self):
        self.driver.find_element(By.CSS_SELECTOR, ("[type=submit]")).click()
        sleep(3)


class MainPage_calculator:
    def __init__(self, driver2):
        self.driver = driver2
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.maximize_window()
           
# В поле ввода по локатору #delay очистить и затем ввести значение 45
    def delay(self, number):
        self.driver.find_element(By.CSS_SELECTOR, "[id=delay]").clear()
        self.driver.find_element(By.CSS_SELECTOR, "[id=delay]").send_keys(number)

# Нажать на кнопки: 7, +, 8, =
    def click_num(self):
        self.driver.find_element(By.XPATH, ('//span[text()="7"]')).click()
        self.driver.find_element(By.XPATH, ('//span[text()="+"]')).click()
        self.driver.find_element(By.XPATH, ('//span[text()="8"]')).click()
        self.driver.find_element(By.XPATH, ('//span[text()="="]')).click()


class MainPage_marketplace:
    def __init__(self, driver3):
        self.driver = driver3
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
    
# Авторизуйтесь как пользователь standard_user
    def authen(self):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    