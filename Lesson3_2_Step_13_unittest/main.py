import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

welcome_text = "Congratulations! You have successfully registered!"
link1 = "https://suninjuly.github.io/registration1.html"
link2 = "https://suninjuly.github.io/registration2.html"
implicity_wait_timer = 5


def open_link(link):
    browser = webdriver.Chrome()
    browser.get(link)
    return browser


class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        browser = open_link(link1)

        browser.implicitly_wait(implicity_wait_timer)

        input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first:required")
        input1.send_keys("test")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second:required")
        input2.send_keys("test")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third:required")
        input3.send_keys("test")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text_actual = welcome_text_elt.text

        browser.quit()

        self.assertEqual(welcome_text_actual, welcome_text,
                         f"Welcome text is wrong. \nExpected: {welcome_text}. \nGot: {welcome_text_actual}")

    def test_registration2(self):
        browser = open_link(link2)

        browser.implicitly_wait(implicity_wait_timer)

        input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first:required")
        input1.send_keys("test")
        input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second:required")
        input2.send_keys("test")
        input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third:required")
        input3.send_keys("test")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text_actual = welcome_text_elt.text

        browser.quit()

        self.assertEqual(welcome_text_actual, welcome_text,
                         f"Welcome text is wrong. \nExpected: {welcome_text}. \nGot: {welcome_text_actual}")


if __name__ == '__main__':
    unittest.main()
