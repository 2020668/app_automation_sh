# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/9/14

E-mail:keen2020@outlook.com

=================================


"""

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

# desired_caps["automationName"] = "UiAutomator2"

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

driver.start_activity('包名', '入口名')

