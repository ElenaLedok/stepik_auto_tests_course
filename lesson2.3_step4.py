# Тест принимаем Alert
from selenium import webdriver
from selenium.webdriver.common.by import By


import time
import math

# Функция для вычисления результата из числа
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

# Принять alert (confirm) и нажимаем кнопку OK
    alert = browser.switch_to.alert
    alert.accept()

# На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)

# Ввести ответ в поле и отправить форму
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(10)

    browser.quit()