from selenium import webdriver
from selenium.webdriver.common.by import By
import time

if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/find_xpath_form")
        time.sleep(1)
        elements = browser.find_elements(By.TAG_NAME, "input")
        for el in elements:
            el.send_keys("Test")
        btn = browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
        btn.click()
        time.sleep(10)

    finally:
        browser.quit()
