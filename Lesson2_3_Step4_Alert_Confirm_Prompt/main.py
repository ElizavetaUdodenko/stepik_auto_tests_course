from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, os

def calc(x):
    return math.log(abs(12 * math.sin(x)))


if __name__ == '__main__':

    try:
        link = "http://suninjuly.github.io/alert_accept.html"
        browser = webdriver.Chrome()
        browser.get(link)

        btn = browser.find_element(By.CLASS_NAME, "btn-primary")
        btn.click()

        confirm = browser.switch_to.alert
        confirm.accept()

        x = browser.find_element(By.ID, "input_value").text
        y = calc(int(x))

        answer = browser.find_element(By.ID, "answer")
        answer.send_keys(y)

        submit = browser.find_element(By.CLASS_NAME, "btn-primary")
        submit.click()

        time.sleep(1)

        alert = browser.switch_to.alert
        data = alert.text.split()[-1]
        print(data)
        os.system("echo '%s' | pbcopy" % data)

    finally:
        browser.quit()
