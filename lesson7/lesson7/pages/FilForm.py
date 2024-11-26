from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FilForm:
    def __init__(self, browser2):
        self.driver = browser2

# 6. Заполните форму своими данными: имя, фамилия, почтовый индекс
    def person_data(self):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Ольга")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Тимошенко")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123")
        sleep(2)

# 7. Нажмите кнопку Continue
    def click_contin(self):
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()
        sleep(2)