import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math, os


def calc(x):
    return math.log(abs(12*math.sin(x)))


if __name__ == '__main__':
    try:
        link = "http://suninjuly.github.io/explicit_wait2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

        btn = browser.find_element(By.ID, "book")
        btn.click()

        submit = browser.find_element(By.ID, "solve")
        browser.execute_script("return arguments[0].scrollIntoView(true);", submit)

        x = browser.find_element(By.ID, "input_value").text
        y = calc(int(x))

        answer = browser.find_element(By.ID, "answer")
        answer.send_keys(y)

        submit.click()

        alert = browser.switch_to.alert
        data = alert.text.split()[-1]
        print(data)
        os.system("echo '%s' | pbcopy" % data)

    finally:
        browser.quit()
