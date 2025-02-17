# Тест на Загрузку файла
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    firstname = browser.find_element(By.NAME, "firstname")
    firstname.send_keys("ivan")

    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("ivanov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("testivan@gmail.com")

# Определение текущей директории
    current_dir = os.path.dirname(__file__) # получаем текущую директорию
    file_path = os.path.join(current_dir, "file.txt") # указываем путь к файлу

# Находим поле для загрузки файла и передаем путь к файлу
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)

    browser.quit()