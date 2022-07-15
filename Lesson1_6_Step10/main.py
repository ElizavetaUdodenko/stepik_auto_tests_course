import time
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':

    try:
        browser = webdriver.Chrome()
        time.sleep(5)

        browser.get("http://suninjuly.github.io/registration1.html")

        elements = browser.find_elements(By.CSS_SELECTOR, "div.first_block > div > input")
        for e in elements:
            e.send_keys("Test")

        time.sleep(5)

        button = browser.find_element(By.TAG_NAME, "button" )
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

        time.sleep(10)

    finally:
        browser.quit()
