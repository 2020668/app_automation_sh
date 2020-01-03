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
from common.basepage import BasePage
from page_locators.wechat_locator import WechatLocator as Loc


class WechatPay(BasePage):

    def wechat_pay(self):

        desired_caps = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "platformVersion": "9",
            "deviceName": "mi8_lite",
            "appPackage": 'com.tencent.mm',
            "appActivity": 'com.tencent.mm.ui.LauncherUI',
            "recreateChromeDriverSessions": True,
            'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'},
            "noReset": True
        }

        # desired_caps["chromedriverExecutable"] = 'D:\\ChromeDrivers\\chrome39-42\\chromedriver.exe'

        # 连接appium desktop，向appium发送请求。在哪个设备打开哪个app
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        # 密码输入框
        self.wait_ele_visible(loc=Loc.pwd_input_loc, img_desc="登录密码输入框")
        self.input_text(loc=Loc.pwd_input_loc, value="fendou19881128", img_desc="登录密码输入框")

        # 登录按钮
        self.wait_ele_visible(loc=Loc.login_button_loc, img_desc="登录按钮")
        self.click_element(loc=Loc.login_button_loc, img_desc="登录按钮")

        time.sleep(3)

        # 点击 + 号
        self.wait_ele_visible(loc=Loc.add_button_loc, img_desc="+按钮")
        self.click_element(loc=Loc.add_button_loc, img_desc="+按钮")

        # 点击 扫一扫按钮
        self.wait_ele_visible(loc=Loc.scan_loc, img_desc="扫一扫按钮")
        self.click_element(loc=Loc.scan_loc, img_desc="扫一扫按钮")

        # 等待webview出现
        self.wait_ele_visible(loc=Loc.webview_loc, img_desc="webview对象")
        # loc = MobileBy.CLASS_NAME, "com.tencent.tbs.core.webkit.WebView"
        # WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))

        time.sleep(2)

        # 获取当前页面所有的contexts
        cons = driver.contexts
        print(cons)

        # 切换到webview
        driver.switch_to.context('WEBVIEW_com.tencent.mm')
        handles = driver.window_handles
        # print(handles)
        # time.sleep(3)

        for i in handles:
            driver.switch_to.window(i)
            if "向商户付款" in driver.page_source:
                break

        # 确认支付按钮
        self.wait_ele_visible(loc=Loc.pay_sure_loc, img_desc="确认支付按钮")
        self.click_element(loc=Loc.pay_sure_loc, img_desc="确认支付按钮")

        # 确定按钮
        # self.wait_ele_visible(loc=Loc.pay_sure_loc, img_desc="确认")
        # loc = MobileBy.XPATH, '//input[@type="button"]'
        # WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
        # driver.find_element(*loc).click()

        # 返回app
        driver.switch_to.context("NATIVE_APP")

        # 使用密码按钮
        self.wait_ele_visible(loc=Loc.use_pwd_loc, img_desc="使用密码按钮")
        self.click_element(loc=Loc.use_pwd_loc, img_desc="使用密码按钮")
        # loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("使用密码")'
        # WebDriverWait(driver, 20).until(ec.presence_of_element_located(loc))
        # driver.find_element(*loc).click()

        # 支付密码输入框
        self.wait_ele_visible(loc=Loc.pay_pwd_input_loc, img_desc="支付密码输入框")
        self.click_element(loc=Loc.pay_pwd_input_loc, img_desc="支付密码输入框")

        # 输入密码
        self.driver.tap([(180, 1580), (180, 1580)], 500)
        time.sleep(0.5)

        self.driver.tap([(180, 1580), (180, 1580)], 500)
        time.sleep(0.5)

        self.driver.tap([(540, 1580), (540, 1580)], 500)
        time.sleep(0.5)

        self.driver.tap([(540, 2060), (540, 2060)], 500)
        time.sleep(0.5)

        self.driver.tap([(540, 1580), (540, 1580)], 500)
        time.sleep(0.5)

        self.driver.tap([(540, 1740), (540, 1740)], 500)

        # 完成按钮
        self.wait_ele_visible(loc=Loc.finish_loc, img_desc="完成按钮")
        time.sleep(6)
        self.click_element(loc=Loc.finish_loc, img_desc="完成按钮")
        # loc = MobileBy.CLASS_NAME, "android.widget.ImageView"
        # WebDriverWait(driver, 20).until(ec.presence_of_element_located(loc))
        # time.sleep(8)
        # driver.find_element(*loc).click()

        # 点击页面左上角 X
        self.wait_ele_visible(loc=Loc.close_loc, img_desc="页面右上角 X 按钮")
        self.click_element(loc=Loc.close_loc, img_desc="页面右上角 X 按钮")
        # loc = MobileBy.ID, "com.tencent.mm:id/m0"
        # WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
        # driver.find_element(*loc).click()

        # 点击 我 按钮
        self.wait_ele_visible(loc=Loc.me_loc, img_desc="按钮 我")
        self.click_element(loc=Loc.me_loc, img_desc="按钮 我")
        # loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.mm:id/djv").text("我")'
        # WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
        # driver.find_element(*loc).click()

        # 点击 设置 按钮
        self.wait_ele_visible(loc=Loc.setting_loc, img_desc="设置 按钮")
        self.click_element(loc=Loc.setting_loc, img_desc="设置 按钮")
        # loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/title").text("设置")'
        # WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
        # driver.find_element(*loc).click()

        # 退出按钮
        self.wait_ele_visible(loc=Loc.out_button_loc, img_desc="退出 按钮")
        self.click_element(loc=Loc.out_button_loc, img_desc="退出 按钮")
        # loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.mm:id/d8").text("退出")'
        # WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
        # driver.find_element(*loc).click()

        # 退出登录
        loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.mm:id/dc").text("退出登录")'
        WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
        driver.find_element(*loc).click()

        # 退出按钮
        self.wait_ele_visible(loc=Loc.logout_sure_loc, img_desc="确定退出按钮")
        self.click_element(loc=Loc.logout_sure_loc, img_desc="确定退出按钮")
        # loc = MobileBy.ID, "com.tencent.mm:id/b47"
        # WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
        # driver.find_element(*loc).click()

        time.sleep(8)

        # loc = MobileBy.ID, "com.tencent.mm:id/m0"
        # WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
        # driver.find_element(*loc).click()


if __name__ == '__main__':
    we = WechatPay(BasePage)
    we.wechat_pay()

