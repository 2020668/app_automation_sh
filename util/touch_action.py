# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/9/1

E-mail:keen2020@outlook.com

=================================


"""

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

# actionchains      把所有的鼠标操作放在一个链表里面,通过perform去执行

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

# 九宫格   获取元素的起点坐标
start_loc = driver.find_element("", "").location

# 获取元素的大小
size = driver.find_element("", "").size

# 步长
step = size["width"]/6

# 第一个点
TouchAction(driver).press(x=start_loc["x"]+step, y=start_loc["y"]+step).wait(200).\
    move_to(x=start_loc["x"]+3*step, y=start_loc["y"]+step).wait(200).\
    move_to(x=start_loc["x"]+5*step, y=start_loc["y"]+step).wait(200).\
    move_to(x=start_loc["x"]+5*step, y=start_loc["y"]+3*step).wait(200).\
    move_to(x=start_loc["x"]+3*step, y=start_loc["y"]+3*step).wait(200).\
    move_to(x=start_loc["x"]+step, y=start_loc["y"]+3*step).\
    release().perform()



