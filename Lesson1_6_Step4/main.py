from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':

    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/simple_form_find_task.html")
        input1 = browser.find_element(By.NAME, "first_name")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(30)

    finally:
        browser.quit()

