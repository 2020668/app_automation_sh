# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/7

E-mail:keen2020@outlook.com

=================================


"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import logging

from common.tools import uninstall_uiautomator2, uninstall_appium_settings

desired_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "platformVersion": "8.1",
    "deviceName": "mi_6x",
    "appPackage": 'com.cashier.jiutongfuwu',
    "appActivity": 'com.cashier.jiutongfuwu.activity.StartActivity',
    "noReset": True
}

# 数据参数
phone = "18627787716"
pwd = "123456"
msg_code = "123456"


# desired_caps["chromedriverExecutable"] = 'D:\\ChromeDrivers\\chrome39-42\\chromedriver.exe'

# 2、连接appium desktop，向appium发送请求。在哪个设备打开哪个app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 手机号输入框
loc = MobileBy.ID, 'com.cashier.jiutongfuwu:id/et_phone'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("18627787716")

# 密码输入框
loc = MobileBy.ID, 'com.cashier.jiutongfuwu:id/et_password'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("123456")

# 登录按钮
loc = MobileBy.ID, 'com.cashier.jiutongfuwu:id/btn_login'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 开户进件按钮
loc = MobileBy.ID, 'com.cashier.jiutongfuwu:id/tv_open_account'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 手机号码输入框
loc = MobileBy.ID, 'com.cashier.jiutongfuwu:id/et_open_account'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("13022223333")

# 获取验证码按钮
loc = MobileBy.ID, 'com.cashier.jiutongfuwu:id/cv_get_countdown'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 验证码输入框
loc = MobileBy.ID, 'com.cashier.jiutongfuwu:id/et_open_code'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("123456")

# 点击下一步
loc = MobileBy.ID, 'com.cashier.jiutongfuwu:id/next_btn'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击小微商户
loc = MobileBy.ID, 'com.cashier.jiutongfuwu:id/iv_xiaowei'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击门头照
loc = MobileBy.ID, 'com.cashier.jiutongfuwu:id/iv_store_head'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击从相册选择
loc = MobileBy.ID, 'com.cashier.jiutongfuwu:id/but_zhaopian_xiangce'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 选择图片
loc = MobileBy.ID, 'com.miui.gallery:id/pick_num_indicator'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_elements(*loc)[4].click()


# 卸载配置应用
uninstall_uiautomator2()
uninstall_appium_settings()
