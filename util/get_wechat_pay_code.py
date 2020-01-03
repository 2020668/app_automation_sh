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


def get_wechat_pay_code():
    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "platformVersion": "9",
        "deviceName": "mi8_lite",
        "appPackage": 'com.tencent.mm',
        "appActivity": 'com.tencent.mm.ui.LauncherUI',
        "noReset": True,
        'chromeOptions': {'androidProcess': 'WEBVIEW_com.tencent.mm'}
    }

    # desired_caps["chromedriverExecutable"] = 'D:\\ChromeDrivers\\chrome39-42\\chromedriver.exe'

    # 2、连接appium desktop，向appium发送请求。在哪个设备打开哪个app
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    # 点击 我
    loc = (MobileBy.ID, 'com.tencent.mm:id/ta')
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()

    # 点击 支付按钮
    loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("支付")'
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()

    time.sleep(5)

    # 点击首付款按钮
    loc = MobileBy.ID, "com.tencent.mm:id/dde"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()

    # time.sleep(2)

    # 获取当前页面所有的contexts
    cons = driver.contexts
    print(cons)

    # 切换到webview
    # driver.switch_to.context(cons[1])
    driver.switch_to.context('WEBVIEW_com.tencent.mm')

    # 金额输入框
    loc = MobileBy.XPATH, '//span[@id="amount"]'
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).send_keys("0.01")

    # 确定按钮
    loc = MobileBy.XPATH, '//input[@type="button"]'
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()

    # # 返回app
    # driver.switch_to.context("NATIVE_APP")
    # 使用密码按钮
    loc = MobileBy.ID, "com.tencent.mm:id/g4f"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).click()

    # 支付密码输入框
    loc = MobileBy.ID, "android.widget.RelativeLayout"
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
    driver.find_element(*loc).send_keys("112025")

    # 卸载配置应用
    uninstall_uiautomator2()
    uninstall_appium_settings()
