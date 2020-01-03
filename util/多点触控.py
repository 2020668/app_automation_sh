# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/2

E-mail:keen2020@outlook.com

=================================


"""

from appium.webdriver.common.multi_action import MultiAction
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time



desired_caps = {}

desired_caps["platformName"] = "Android"  # 平台名称
desired_caps["platformVersion"] = "9"  # 平台版本,雷电模拟器的安卓版本是5.1,真机以实际版本为准
desired_caps["deviceName"] = "mi8_lite"  # 设备名称，可以随便写
desired_caps["appPackage"] = 'com.autonavi.minimap'  # 应用包名 com.cashier.jiutongshanghu
desired_caps["appActivity"] = 'com.autonavi.map.activity.SplashActivity'  # 应用入口页面
desired_caps["noReset"] = True  # 不重置应用的状态

# 2、连接appium desktop，向appium发送请求。在哪个设备打开哪个app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)

# 获取屏幕尺寸
size = driver.get_window_size()

t1 = TouchAction(driver)
t2 = TouchAction(driver)
t1.press(x=size['width']*0.6, y=size['height']*0.6).wait(200).move_to(x=size['width']*0.9, y=size['height']*0.3).wait(200).release()
t2.press(x=size['width']*0.5, y=size['height']*0.7).wait(200).move_to(x=size['width']*0.2, y=size['height']*0.9).wait(200).release()

ma = MultiAction(driver)
ma.add(t1, t2)
ma.perform()
