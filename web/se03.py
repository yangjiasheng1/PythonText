from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://www.baidu.com/')

driver.find_element_by_id('s-top-loginbtn').click()
driver.find_element_by_id('TANGRAM__PSP_11__regLink').click()
a = driver.window_handles
time.sleep(2)
driver.switch_to.window(a[0])
# print(1)
# b = driver.current_window_handle
# print(b)