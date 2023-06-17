from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем на кнопку
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'magical')]")
    button.click()

    # Переключаемся на модальное окно и принимаем
    confirm = browser.switch_to.alert
    confirm.accept()

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print("value x: ", x)
    y = calc(x)
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)
         
    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
