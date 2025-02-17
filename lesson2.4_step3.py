# Тест - Нажать на кнопку и Проверить, что появилась надпись. Кнопка появляется с задержкой
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

try:
    link = "http://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    time.sleep(1) # если кнопка появляется с задержкой мы добавляем паузу до начала поиска элемента
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    time.sleep(10)

    browser.quit()