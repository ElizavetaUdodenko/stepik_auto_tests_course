from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/math.html")

        element_x = browser.find_element(By.CSS_SELECTOR, "#input_value")
        x = element_x.text
        y = calc(x)

        element_y = browser.find_element(By.CSS_SELECTOR, "#answer")
        element_y.send_keys(y)

        checkbox = browser.find_element(By.ID, "robotCheckbox")
        checkbox.click()

        radio_btn = browser.find_element(By.ID, "robotsRule")
        radio_btn.click()

        submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
        submit.click()

        time.sleep(5)

        radio_btn_checked = radio_btn.get_attribute("name")
        print(radio_btn_checked)

        people = browser.find_element(By.ID, "peopleRule")
        people_checked = people.get_attribute("checked")
        print(people_checked)
        assert people_checked is not None, "People radio is not selected by default"

        people_href = people.get_attribute("href")
        print(people_href)

    finally:
        browser.quit()

