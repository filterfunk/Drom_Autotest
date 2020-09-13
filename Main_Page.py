# Набор методов на главной странице
from selenium import webdriver
import time

link = "https://www.drom.ru"
browser = webdriver.Chrome()
browser.get(link)

time.sleep(10)
browser.quit()

# Найти Ларгусы



