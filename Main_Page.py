# Набор методов на главной странице
from selenium import webdriver
import time

link = "https://www.drom.ru"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(10)
browser.quit()


# Открыть Продажа авто в России
browser.find_element_by_link_text("Продажа авто в России")[1].click()



# Найти Ларгусы



