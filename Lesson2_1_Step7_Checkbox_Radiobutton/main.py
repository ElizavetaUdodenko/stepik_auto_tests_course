from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/get_attribute.html")

        element = browser.find_element(By.ID, "treasure")
        x = element.get_attribute("valuex")
        y = calc(x)

        answer = browser.find_element(By.ID, "answer")
        answer.send_keys(y)

        checkbox = browser.find_element(By.ID, "robotCheckbox")
        checkbox.click()

        radio = browser.find_element(By.ID, "robotsRule")
        radio.click()

        btn = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
        btn.click()

        time.sleep(5)

    finally:
        browser.quit()
