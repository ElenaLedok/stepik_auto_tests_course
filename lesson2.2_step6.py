from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Посчитать математическую функцию от x
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

# Считать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)

# Проскроллить страницу вниз.
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)

# Ввести ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

# Выбрать checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

# Прокручиваем страницу до радиокнопки и переключаем на "Robots rule!"
    radio_button = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("arguments[0].scrollIntoView();", radio_button)

    radio_button.click()

# Нажать на кнопку "Submit"
    submit_button.click()

finally:
    time.sleep(10)

    browser.quit()