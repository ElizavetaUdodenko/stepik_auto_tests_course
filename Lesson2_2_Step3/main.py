from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

if __name__ == '__main__':
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/selects1.html")

        el1 = browser.find_element(By.ID, "num1").text
        x = int(el1)
        el2 = browser.find_element(By.ID, "num2").text
        y = int(el2)

        select = Select(browser.find_element(By.TAG_NAME, "select"))
        select.select_by_visible_text(str(x+y))

        btn = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
        btn.click()
        time.sleep(5)

    finally:
        browser.quit()
