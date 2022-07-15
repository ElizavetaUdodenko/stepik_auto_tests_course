# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    try:
    # print_hi('PyCharm')

    # Инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
        driver = webdriver.Chrome()

    # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
        time.sleep(5)

    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
        driver.get("https://stepik.org/lesson/25969/step/12")
        time.sleep(15)

    # Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему.
    # Способы поиска элементов мы обсудим позже
    # Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
    # Ищем поле для ввода текста
        textarea = driver.find_element(By.CSS_SELECTOR, ".ember-text-area")

    # Напишем текст ответа в найденное поле
        textarea.send_keys("get()")
        time.sleep(5)

    # Найдем кнопку, которая отправляет введенное решение
        submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

    # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
        submit_button.click()
        time.sleep(5)

    # После выполнения всех действий мы должны не забыть закрыть окно браузера

    finally:
        driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
