from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver =  webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('https://www.baidu.com/')

# driver.find_element_by_id('kw').send_keys('杨佳晟')
#鼠标右键
right_click = driver.find_element_by_id('lg')
ActionChains(driver).context_click(right_click).perform()
#鼠标悬停
xuanting = driver.find_element_by_id('s-usersetting-top')
ActionChains(driver).move_to_element(xuanting).perform()
#鼠标双击
# shuangji = driver.find_element_by_id('head_wrapper')
# ActionChains(driver).double_click(shuangji).perform()
#鼠标拖放
# yuanweizhi  = driver.find_element_by_class_name('title-content-title')
# xinweizhi = driver.find_element_by_id('kw')
# ActionChains(driver).drag_and_drop(yuanweizhi, xinweizhi).perform()
#获取文本
# a = driver.find_element_by_class_name('title-content-title').text
# print(a)
#打印当前页面
b = driver.title
print(b)
#打印当前页面url
c = driver.current_url
print(c)