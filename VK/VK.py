from selenium import webdriver
import time
import pytest

link = "https://vk.com"
link2 = "https://vk.com/id32419013"
browser = webdriver.Chrome()
browser.get(link)

# Залогинивание
try:
    input1 = browser.find_element_by_id("index_email")
    input1.send_keys("+79609300308")
    input2 = browser.find_element_by_id("index_pass")
    input2.send_keys("1Вутсршл1")
    userpage = browser.current_url
    print(userpage)
    button = browser.find_element_by_id("index_login_button").click()
    #a = browser.find_element_by_xpath("//a[@href='/id32419013' and @class='left_row']").click()


# находим элемент, содержащий текст
    userpage = browser.current_url
    print(userpage)
    assert userpage == link2

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


# Разлогинивание
# time.sleep(5)
# button1 = browser.find_element_by_xpath('//div[@class="top_profile_arrow"]')
# button1.click()
#
# button2 = browser.find_element_by_id("top_logout_link")
# button2.click()
#
# userpage = browser.current_url
# print(userpage)
# assert userpage == link, "Урл неверный"
#
# time.sleep(5)
# browser.quit()
