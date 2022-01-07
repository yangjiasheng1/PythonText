from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time 
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com/')

# driver.find_element_by_id('s-top-loginbtn').click()
# a = driver.current_window_handle
# driver.find_element_by_id('TANGRAM__PSP_11__regLink').click()
# b = driver.window_handles
# for i in b:
#     if i == a:
#         driver.switch_to_window(i)


xuanting = driver.find_element_by_id('s-usersetting-top')
ActionChains(driver).move_to_element(xuanting).perform()
driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/div/a[1]').click()
driver.find_element_by_xpath('//*[@id="se-setting-7"]/a[2]').click()
time.sleep(2)
#接收弹窗3
driver.switch_to.alert.accept()