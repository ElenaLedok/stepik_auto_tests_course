from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Функция для вычисления ответа
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Получение значения x из элемента с id="input_value"
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # Вычисляем значение y
    y = calc(x)

    # Вводим результат в текстовое поле с id="answer"
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Отмечаем чекбокс "I'm the robot" с id="robotCheckbox"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбираем радиокнопку "Robots rule!" с id="robotsRule"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Даём время на выполнение и закрываем браузер
    time.sleep(10)

    browser.quit()