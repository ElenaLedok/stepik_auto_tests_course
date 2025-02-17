from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elem1 = browser.find_element(By.CSS_SELECTOR, "#num1")

    elem2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    num1 = int(elem1.text)
    num2 = int(elem2.text)
    total = num1 + num2

    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    # select.click()

    select.select_by_value(str(total))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)

    browser.quit()