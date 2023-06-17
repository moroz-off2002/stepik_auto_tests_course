from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем слагаемые
    num1 = browser.find_element(By.ID, "num1")
    x = num1.text
    num2 = browser.find_element(By.ID, "num2")
    y = num2.text
    z = int(x) + int(y)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(z))  # ищем элемент с ответом
         
    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
