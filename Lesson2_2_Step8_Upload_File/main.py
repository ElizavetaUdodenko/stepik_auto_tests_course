from selenium import webdriver
from selenium.webdriver.common.by import By

import time, math, os

if __name__ == '__main__':

    try:
        link = "http://suninjuly.github.io/file_input.html"
        browser = webdriver.Chrome()
        browser.get(link)

        for element in browser.find_elements(By.CSS_SELECTOR, "input.form-control"):
            element.send_keys("Test")

        time.sleep(1)

        # file = "/test.txt"

        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'test.txt')
        print(current_dir)

        upload_file = browser.find_element(By.ID, "file")
        upload_file.send_keys(file_path)

        btn = browser.find_element(By.CLASS_NAME, "btn-primary")
        btn.click()

        time.sleep(5)

    finally:
        browser.quit()
