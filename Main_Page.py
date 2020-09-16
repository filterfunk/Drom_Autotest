# Набор методов на главной странице
import self as self
from selenium import webdriver
import time

link = "https://www.drom.ru"
browser = webdriver.Chrome()
browser.get(link)

# Открыть Продажа авто в России
browser.find_element_by_xpath("//h2[@class='css-1cmbqcv e18vbajn0']").click()

# Радиус поиска +1000км
browser.find_element_by_xpath("//a[@class='css-ifsycf e1wvjnck0'][2]").click()

# Прокручиваем вниз, чтобы было видно списки моделей
element = browser.find_element_by_xpath("//button[contains(text(), 'Марка')]")
browser.execute_script("return arguments[0].scrollIntoView(true);", element)

# Найти Ларгусы
Brand = browser.find_element_by_xpath("//button[contains(text(), 'Марка')]").click()
Brand1 = browser.find_element_by_xpath("//div[contains(text(), 'Лада')][2]").click()
Model = browser.find_element_by_xpath("//button[contains(text(), 'Модель')][1]").click()
Model1 = browser.find_element_by_xpath("//div[contains(text(), 'Ларгус')][1]").click()
Year = browser.find_element_by_xpath("//button[contains(text(), 'Год от')]").click()
Year1 = browser.find_element_by_xpath("//div[contains(text(), '2015')][1]").click()


# Прокручиваем вниз до кнопки Отправить и нажимаем её
submit = browser.find_element_by_xpath("//button[@type='submit']")
browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
submit = browser.find_element_by_xpath("//button[@type='submit']").click()
userpage = browser.current_url
print(userpage)
assert userpage == "https://novosibirsk.drom.ru/lada/largus/?minyear=2015&distance=1000"


time.sleep(5)
browser.quit()
