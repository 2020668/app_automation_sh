# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/27

E-mail:keen2020@outlook.com

=================================


"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import datetime
import logging
from common import logger

from common.tools import uninstall_uiautomator2, uninstall_appium_settings


# 能否完成付款完成后返回H5页,再次付款。取决于实际操作能否在H5页重复付款

desired_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "platformVersion": "9",
    "deviceName": "mi8_lite",
    "appPackage": 'com.tencent.mm',
    "appActivity": 'com.tencent.mm.ui.LauncherUI',
    # "recreateChromeDriverSessions": True,
    'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'},
    "noReset": True
}

# desired_caps["chromedriverExecutable"] = 'D:\\ChromeDrivers\\chrome39-42\\chromedriver.exe'

# 2、连接appium desktop，向appium发送请求。在哪个设备打开哪个app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 密码输入框
# loc = MobileBy.ID, "com.tencent.mm:id/m6"
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).send_keys("pwd")
#
# # 登录按钮
# loc = MobileBy.ID, "com.tencent.mm:id/d0q"
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
#
# time.sleep(3)

# 点击 + 号
loc = (MobileBy.ID, 'com.tencent.mm:id/ra')
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
logging.info("等待 + 按钮可见成功")
driver.find_element(*loc).click()
logging.info("点击 + 按钮成功")

# 点击 扫一扫按钮
# loc = (MobileBy.ID, 'com.tencent.mm:id/dc")')
loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("扫一扫")'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
logging.info("等待 扫一扫 按钮可见成功")
driver.find_element(*loc).click()
logging.info("点击 扫一扫 按钮成功")

# # 点击屏幕右上方的更多按钮         class android.widget.ImageButton
# loc = MobileBy.ID, "com.tencent.mm:id/ln"
# # loc = MobileBy.CLASS_NAME, "android.widget.ImageButton"
# WebDriverWait(driver, 20).until(ec.presence_of_element_located(loc))
# driver.find_element(*loc).click()
#
# # 从相册选择二维码
# loc = MobileBy.ID, "com.tencent.mm:id/dc"
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
#
# # 选取第一张图片
# loc = MobileBy.ID, "com.tencent.mm:id/cem"
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()

# 等待webview出现
loc = MobileBy.CLASS_NAME, "com.tencent.tbs.core.webkit.WebView"
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
logging.info("等待 webview 元素可见成功")

# 获取当前页面所有的contexts
# cons = driver.contexts
# print(cons)
num = 0
while num < 3:

    cons = driver.contexts
    print(cons)

    start = datetime.datetime.now()

    # 切换到webview
    driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
    handles = driver.window_handles
    print(handles)
    for i in handles:
        driver.switch_to.window(i)
        if "向商户付款" in driver.page_source:
            break

    # 确认支付按钮
    time.sleep(1)
    loc = MobileBy.XPATH, "//button[@class='tijiao']"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    logging.info("等待 使用密码 按钮可见成功")
    driver.find_element(*loc).click()
    logging.info("点击 使用密码 按钮成功")

    # 确定按钮
    # loc = MobileBy.XPATH, '//input[@type="button"]'
    # WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    # driver.find_element(*loc).click()

    # 返回app
    driver.switch_to.context("NATIVE_APP")

    # 使用密码按钮
    loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("使用密码")'
    WebDriverWait(driver, 20).until(ec.presence_of_element_located(loc))
    logging.info("等待 使用密码 按钮可见成功")
    driver.find_element(*loc).click()
    logging.info("点击 使用密码 按钮成功")

    # 支付密码输入框 采用坐标定位 不同手机的密码和坐标都不同
    loc = MobileBy.CLASS_NAME, "android.widget.RelativeLayout"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    # driver.find_element(*loc).click()
    # driver.find_element(*loc).send_keys("112025")
    driver.tap([(180, 1580), (180, 1580)], 500)
    time.sleep(0.1)
    driver.tap([(180, 1580), (180, 1580)], 500)
    time.sleep(0.1)
    driver.tap([(540, 1580), (540, 1580)], 500)
    time.sleep(0.1)
    driver.tap([(540, 2060), (540, 2060)], 500)
    time.sleep(0.1)
    driver.tap([(540, 1580), (540, 1580)], 500)
    time.sleep(0.1)
    driver.tap([(540, 1740), (540, 1740)], 500)

    # 手机原生的返回按钮 采用坐标定位 不同手机的密码和坐标都不同

    # 付款完成后的完成按钮
    loc = MobileBy.CLASS_NAME, "android.widget.ImageView"

    time.sleep(2)
    driver.tap([(771, 2210), (771, 2210)], 500)
    time.sleep(1)
    driver.tap([(771, 2210), (771, 2210)], 500)
    # time.sleep(1)
    # driver.tap([(771, 2210), (771, 2210)], 500)
    # time.sleep(3)

    logging.info("输入支付密码成功")

    # # 完成按钮
    # loc = MobileBy.CLASS_NAME, "android.widget.ImageView"
    # WebDriverWait(driver, 20).until(ec.presence_of_element_located(loc))
    # time.sleep(8)
    # driver.find_element(*loc).click()
    #
    # # 点击页面左上角 X
    # loc = MobileBy.ID, "com.tencent.mm:id/m0"
    # WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    # driver.find_element(*loc).click()

    end = datetime.datetime.now()
    num += 1
    logging.info("完成第{}次支付,耗时{}".format(num, end - start))

# # 点击 我 按钮
# loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.mm:id/djv").text("我")'
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
#
# # 点击 设置 按钮
# loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/title").text("设置")'
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
#
# # 退出按钮
# loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.mm:id/d8").text("退出")'
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
#
# # 退出登录
# loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.mm:id/dc").text("退出登录")'
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
#
# # 确认退出按钮
# loc = MobileBy.ID, "com.tencent.mm:id/b47"
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
#
# time.sleep(8)

driver.quit()

# 卸载配置应用
uninstall_uiautomator2()
uninstall_appium_settings()
