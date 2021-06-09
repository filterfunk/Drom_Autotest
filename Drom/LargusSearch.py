import pytest
from selenium import webdriver
import time
import allure
from allure_commons.types import AttachmentType

link = "https://www.drom.ru"


# Мы создадим фикстуру browser, которая будет создавать объект WebDriver.
@pytest.fixture(scope="class")
def browser():
    print("\nЗапускаем браузер для тестов..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nЗакрываем браузер после тестов..")
    browser.quit()


# Запуск тестов - pytest --alluredir results .\LargusSearch.py
# Создание отчёта Allure - allure serve results

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    @pytest.mark.smoke
    def test_we_can_find_largus(self, browser):
        print("test_we_can_find_largus")
        browser.get(link)
        # Открыть Продажа авто в России
        browser.find_element_by_xpath("//h2[@class='css-1cmbqcv e18vbajn0']").click()
        # Радиус поиска +1000км
        browser.find_element_by_xpath("//a[@class='css-ifsycf e1wvjnck0'][2]").click()
        # Прокручиваем вниз, чтобы было видно списки моделей
        element = browser.find_element_by_xpath("//button[contains(text(), 'Марка')]")
        browser.execute_script('return arguments[0].scrollIntoView(true)', element)
        brand = browser.find_element_by_xpath("//button[contains(text(), 'Марка')]").click()
        brand1 = browser.find_element_by_xpath("//div[contains(text(), 'Лада')][2]").click()
        model = browser.find_element_by_xpath("//button[contains(text(), 'Модель')][1]").click()
        model1 = browser.find_element_by_xpath("//div[contains(text(), 'Ларгус')][1]").click()
        year = browser.find_element_by_xpath("//button[contains(text(), 'Год от')]").click()
        year1 = browser.find_element_by_xpath("//div[contains(text(), '2015')][1]").click()
        # Прокручиваем вниз до кнопки Отправить и нажимаем её
        submit = browser.find_element_by_xpath("//button[@type='submit']")
        browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
        submit = browser.find_element_by_xpath("//button[@type='submit']").click()
        userpage = browser.current_url
        print("URL страницы: " + userpage)
        print("Title страницы: " + browser.title)
        with allure.step('Сделать скриншот'):
            allure.attach(browser.get_screenshot_as_png(),
                          name='Поиск Ларгуса', attachment_type=AttachmentType.PNG)
        assert userpage == "https://novosibirsk.drom.ru/lada/largus/?minyear=2015&distance=1000"
        time.sleep(5)
        browser.quit()
