# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/9/1

E-mail:keen2020@outlook.com

=================================


"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

# desired_caps["automationName"] = "UiAutomator2"

desired_caps = {}
desired_caps["platformName"] = "Android"  # 平台名称
desired_caps["platformVersion"] = "5.1"  # 平台版本,雷电模拟器的安卓版本是5.1
desired_caps["deviceName"] = "mi8_lite"  # 设备名称，可以随便写
desired_caps["appPackage"] = 'com.cashier.jiutongshanghu'  # 应用包名 com.cashier.jiutongshanghu
desired_caps["appActivity"] = 'com.cashier.jiutongshanghu.home.home_main.activity.StartActivity'  # 应用入口页面
desired_caps["noReset"] = True  # 不重置应用的状态

# desired_caps["chromedriverExecutable"] = 'D:\\ChromeDrivers\\chrome39-42\\chromedriver.exe'

# 2、连接appium desktop，向appium发送请求。在哪个设备打开哪个app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

WebDriverWait(driver, 20).until(
    ec.visibility_of_element_located((MobileBy.ID, 'com.cashier.jiutongshanghu:id/ed_login_phone')))
time.sleep(2)

# 获取设备的屏幕大小
size = driver.get_window_size()

# 多机兼容, 从屏幕的(90%,50%)开始滑动到(30%,50%), 多次划屏的话，要等待
driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.5, 200)
