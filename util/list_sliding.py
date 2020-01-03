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
desired_caps["platformVersion"] = "9"  # 平台版本,雷电模拟器的安卓版本是5.1,真机以实际版本为准
desired_caps["deviceName"] = "mi8_lite"  # 设备名称，可以随便写
desired_caps["appPackage"] = 'com.cashier.jiutongshanghu'  # 应用包名 com.cashier.jiutongshanghu
desired_caps["appActivity"] = 'com.cashier.jiutongshanghu.home.home_main.activity.StartActivity'  # 应用入口页面
desired_caps["noReset"] = True  # 不重置应用的状态

# desired_caps["chromedriverExecutable"] = 'D:\\ChromeDrivers\\chrome39-42\\chromedriver.exe'

# 2、连接appium desktop，向appium发送请求。在哪个设备打开哪个app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element_by_android_uiautomator(
    'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/ed_login_phone")').send_keys("13072721092")

driver.find_element_by_android_uiautomator(
    'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/ed_login_password")').send_keys("123456")

# driver.find_element_by_android_uiautomator(
#     'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/iv_login_jizhu")').click()

driver.find_element_by_android_uiautomator(
    'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/but_login")').click()

loc = MobileBy.ANDROID_UIAUTOMATOR, 'new new UiSelector().text("账单")'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 所有页面
loc = MobileBy.ID, 'com.cashier.jiutongshanghu:id/tv_status'
WebDriverWait(driver, 20).until(ec.visibility_of_all_elements_located(loc))
time.sleep(1)

size = driver.get_window_size()
# 滑动之前的页面
old = ""
# 当前的页面
new = driver.page_source

while old != new:
    try:
        driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new new UiSelector().text("15:40:48")')
        print("找到指定订单 元素了")
    except:
        old = new       # 滑动之前,将当前的页面赋值给old
        driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.5, 200)
        loc = MobileBy.ID, 'com.cashier.jiutongshanghu:id/tv_status'
        WebDriverWait(driver, 20).until(ec.visibility_of_all_elements_located(loc))
        time.sleep(1)
        # 重新获取当前页面
        new = driver.page_source
    else:
        print("找到 指定订单 元素了")
        break
