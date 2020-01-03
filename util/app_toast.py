# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/2

E-mail:keen2020@outlook.com

=================================


"""

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


"""
只能通过XPATH定位
注意事项：
1、desired_caps["automationName"] = "UiAutomator2"
2、要求安装JDK1.8 64位以上，并配置环境变量JAVA_HOME和PATH
3、Android5.0以上
4、appium server 1.6.3以上

XPATH表达式
xpath = '//*[contains(@text,"部分文本内容")]'
driverWait方法中，请用presence_of_element_located


"""

desired_caps = {}

desired_caps["platformName"] = "Android"  # 平台名称
desired_caps["platformVersion"] = "9"  # 平台版本,雷电模拟器的安卓版本是5.1,真机以实际版本为准
desired_caps["deviceName"] = "mi8_lite"  # 设备名称，可以随便写
desired_caps["appPackage"] = 'com.cashier.jiutongshanghu'  # 应用包名 com.cashier.jiutongshanghu
desired_caps["appActivity"] = 'com.cashier.jiutongshanghu.home.home_main.activity.StartActivity'  # 应用入口页面
desired_caps["noReset"] = True  # 不重置应用的状态

# desired_caps["chromedriverExecutable"] = 'D:\\ChromeDrivers\\chrome39-42\\chromedriver.exe'

# 2、连接appium desktop，向appium发送请求。在哪个设备打开哪个app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ed_login_phone"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("13072721092")

driver.find_element_by_android_uiautomator(
    'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/ed_login_password")').send_keys("123455")

driver.find_element_by_android_uiautomator(
    'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/but_login")').click()

# 等待toast存在，获取toast文本
loc = MobileBy.XPATH, '//*[contains(@text, "密码错误")]'
try:
    WebDriverWait(driver, 10, 0.01).until(ec.presence_of_element_located(loc))      # 元素存在
    text = driver.find_element(*loc).text
    print("toast元素找到了", text)
except:
    print("toast元素没找到！")

