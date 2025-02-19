# Тест регистрация на сайте в стиле unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest
import time

    class TestRegistration1(unittest.TestCase):

        def setUp(self):
            """Настройка перед тестами: открываем браузер"""
            self.browser = webdriver.Chrome()

        def tearDown(self):
            """Закрытие браузера после тестов"""
            self.browser.quit()

        def test_registration(self):
            """Тест регистрации на сайте, заполнив только обязательные поля"""
            link = "http://suninjuly.github.io/registration1.html"
            self.browser.get(link)

            # Код, который заполняет обязательные поля
            first_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            first_name.send_keys("Ivan")

            last_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            last_name.send_keys("Petrov")

            email = self.browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            email.send_keys("test@example.com")

            # Отправляем заполненную форму
            button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться. ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


    if __name__ == "__main__":
        unittest.main()

