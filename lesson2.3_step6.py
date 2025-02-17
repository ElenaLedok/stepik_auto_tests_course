# Тест Переход на новую вкладку
from selenium import webdriver
from selenium.webdriver.common.by import By


import time
import math

# Функция для вычисления математического выражения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

# Нажимаем на кнопку, которая откроет новую вкладку
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

# Переключаемся на новую вкладку
    new_window = browser.window_handles[1]  # Получаем вторую вкладку (новая)
    browser.switch_to.window(new_window)  # Переключаемся на нее

# Считываем значение x и решаем уравнение
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)

# Вводим ответ в поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

# Нажимаем на кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    time.sleep(10)

    browser.quit()