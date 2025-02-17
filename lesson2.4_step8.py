# Тест - Бронирование дома по строго заданной цене (100$) ждем пока цена упадет.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()

# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

# Нажимаем кнопку "Book"
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

# Находим значение X (математическая формула выше)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)

# Вводим ответ в поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

# Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    time.sleep(10)

    browser.quit()