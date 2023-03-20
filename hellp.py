from selenium import webdriver
import time
import json
import os
from selenium.webdriver.chrome.options import Options


# 虚拟出Chrome界面
chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# action  linux服务器驱动地址
# driver = webdriver.Chrome(executable_path='/home/runner/work/Neworld_SignIn/Neworld_SignIn/driver/chromedriver',chrome_options=chrome_options)    # Chrome浏览器  
# driver = webdriver.Chrome(executable_path='/home/runner/work/Neworld_SignIn/Neworld_SignIn/driver/chromedriver')    # Chrome浏览器  

# windows 系统驱动路径
driver = webdriver.Chrome(executable_path='D:\Downloads\chromedriver_win32\chromedriver.exe')    # Chrome浏览器


# 环境变量中读取数据，包含账号密码，和登陆页面测试
u = os.environ["USERNAME"]
p = os.environ["PASSWORD"]

print('u',u)
print('p',p)
driver.get("https://neworld.tv/auth/login") 
#  获取cookies 
time.sleep(5)
# 账号密码登录版本
driver.find_element_by_id('email').clear()
driver.find_element_by_id("email").send_keys(u)

driver.find_element_by_id('passwd').clear()
driver.find_element_by_id("passwd").send_keys(p)

time.sleep(1)
driver.find_element_by_id("login").click()

driver.refresh()#刷新页面 


driver.refresh()#刷新页面 

# time.sleep(5)

# buttons = driver.find_element_by_xpath("//button[@id='checkin']")
# print('buttons',buttons)

driver.find_element_by_id("checkin").click() # 点击元素
