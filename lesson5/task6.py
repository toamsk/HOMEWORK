# Модальное окно
# 1. Откройте страницу http://the-internet.herokuapp.com/entry_ad
# 2. В модальном окне нажмите на кнопку Сlose.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу Chrome
driver.get("http://the-internet.herokuapp.com/entry_ad")
driver.maximize_window()
sleep(2)

# В модальном окне нажмите на кнопку Сlose
modal_windowe = driver.find_element(By.CSS_SELECTOR, ".modal-footer p")
modal_windowe.click()
sleep(2)
driver.quit()


# Повторение скрипта в Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Открыть страницу Firefox
driver.get("http://the-internet.herokuapp.com/entry_ad")
driver.maximize_window()
sleep(2)

# В модальном окне нажмите на кнопку Сlose
modal_windowe = driver.find_element(By.CSS_SELECTOR, ".modal-footer p")
modal_windowe.click()
sleep(2)
driver.quit()