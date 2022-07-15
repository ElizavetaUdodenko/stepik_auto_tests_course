from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        browser.execute_script("document.title='Script executing';alert('Robots at work');")
        time.sleep(5)

        link = "https://SunInJuly.github.io/execute_script.html"
        browser.get(link)

        x = browser.find_element(By.ID, "input_value").text
        y = calc(x)

        button = browser.find_element(By.TAG_NAME, "button")
        # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        browser.execute_script("window.scrollBy(0, 100);")

        answer = browser.find_element(By.ID, "answer")
        answer.send_keys(y)

        checkbox = browser.find_element(By.ID, "robotCheckbox")
        checkbox.click()

        radio = browser.find_element(By.ID, "robotsRule")
        radio.click()

        button.click()

        time.sleep(5)

    finally:
        browser.quit()
