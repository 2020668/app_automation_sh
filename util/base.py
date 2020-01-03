# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/8/29

E-mail:keen2020@outlook.com

=================================


"""

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import logging

from common.tools import uninstall_uiautomator2, uninstall_appium_settings

# desired_caps["automationName"] = "UiAutomator2"

desired_caps = {}

desired_caps["platformName"] = "Android"  # 平台名称
desired_caps["automationName"] = "UiAutomator2"
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
    'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/ed_login_password")').send_keys("123456")

driver.find_element_by_android_uiautomator(
    'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/but_login")').click()

# loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("账单")'
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
#
# # 所有页面
# loc = (MobileBy.ID, 'com.cashier.jiutongshanghu:id/tv_status')
# WebDriverWait(driver, 20).until(ec.visibility_of_all_elements_located(loc))
# time.sleep(1)
#
# size = driver.get_window_size()
# # 滑动之前的页面
# old = ""
# # 当前的页面
# new = driver.page_source
#
# while old != new:
#     try:
#         driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("15:40:48")')
#         print("找到 指定订单 元素了")
#     except:
#         old = new  # 滑动之前,将当前的页面赋值给old
#         driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.5, 200)
#         loc = MobileBy.ID, 'com.cashier.jiutongshanghu:id/tv_status'
#         WebDriverWait(driver, 20).until(ec.visibility_of_all_elements_located(loc))
#         time.sleep(1)
#         # 重新获取当前页面
#         new = driver.page_source
#     else:
#         print("找到 指定订单 元素了")
#         break

# 点击 我的
loc = (MobileBy.ID, 'com.cashier.jiutongshanghu:id/iv_tab_icon')
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_elements(*loc)[2].click()

# 点击设置
loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/tv_setting")')
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击 退出登录
loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/ll_loginout")'
WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 点击确定   取消-->   com.cashier.jiutongshanghu:id/dialog_normal_leftbtn
loc = MobileBy.ANDROID_UIAUTOMATOR, \
      'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/dialog_normal_rightbtn")'
WebDriverWait(driver, 20).until(ec.visibility_of_all_elements_located(loc))
driver.find_element(*loc).click()

# 卸载配置应用
uninstall_uiautomator2()
uninstall_appium_settings()

# # 等待webview元素出现
# loc = (MobileBy.CLASS_NAME, 'android.webkit.WebView')
# WebDriverWait(driver, 20).until(ec.visibility_of_all_elements_located(loc))
# time.sleep(2)

# # 获取当前所有的contexts
# cons = driver.contexts
# print(cons)

# # 切换到 webview --- 切换到html页面
# driver.switch_to.context(cons[1])
# time.sleep(2)
# print("当前的context: ", driver.current_context)

# print("=======================进入web自动化======================")
# 怎么得到html页面，并进行元素定位？？
# 1、 工具 - uc devtools
# 2、 chrome://inspect
# 3、 driver.page_source得到html页面。保存在一个文件中用chrome访问。
# 4、 直接找开发获取内嵌的html

# 注意chromedriver的版本 要与  安卓 系统的webview版本匹配
# 可以通过desired_caps["chromedriverExecutable"] 来指定 chromedriver的路径 。

# //button[text()="立即购买"]
# loc = (MobileBy.XPATH, '//button[text()="立即购买"]')
# WebDriverWait(driver, 20).until(ec.visibility_of_element_located(loc))
# driver.find_element(*loc).click()

# 步骤： 识别、开启调试模式、得到所有上下文、切换到webview、定位元素并操作(chromedriver的版本匹配)

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_ele_visible(self, locator, timeout=30, poll_frequency=0.5, model_name="model"):
        logging.info("等待元素可见：{}".format(locator))
        try:
            # 获取开始等待的时间
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 获取结束等待的时间
            # 获取等待的总时长 - 以秒为单位
            logging.info("元素已可见。等待元素可见总时长：开始等待的时间，等待结束的时间：")
        except:
            # 写进日志
            logging.exception("等待元素可见超时。")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 查找元素
    def get_element(self, locator, model_name="model"):
        logging.info("查找模块：{}下的元素：{}".format(model_name, locator))
        try:
            ele = self.driver.find_element(*locator)
            logging.info("查元素成功。")
            return ele
        except:
            # 写进日志
            logging.exception("查找元素失败。")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 查找元素
    def get_elements(self, locator, model_name="model"):
        logging.info("查找模块：{}下的元素：{}".format(model_name, locator))
        try:
            ele = self.driver.find_elements(*locator)
            logging.info("查元素成功。")
            return ele
        except:
            # 写进日志
            logging.exception("查找元素失败。")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 点击元素
    def click_element(self, locator, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("点击操作：模块 {} 下的元素 {}".format(model_name, locator))
        try:
            ele.click()
        except:
            # 写进日志
            logging.exception("点击元素操作失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 输入内容
    def input_text(self, locator, value, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("输入操作：模块 {} 下的元素 {}输入文本 {}".format(model_name, locator, value))
        try:
            ele.send_keys(value)
        except:
            # 写进日志
            logging.exception("元素输入操作失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 获取元素的属性
    def get_element_attribute(self, locator, attr, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("获取元素属性：模块 {} 下的元素 {} 的属性 {}".format(model_name, locator, attr))
        try:
            return ele.get_attribute(attr)
        except:
            # 写进日志
            logging.exception("获取元素属性失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 获取元素的文本内容
    def get_element_text(self, locator, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logging.info("获取元素文本值：模块 {} 下的元素 {}".format(model_name, locator))
        try:
            return ele.text
        except:
            # 写进日志
            logging.exception("获取元素文本值失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    def save_webImg(self, model_name):
        # 文件名称=模块名称_当前时间.png
        filePath = screenshot_dir + "/{0}_{1}.png".format(model_name,
                                                          time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logging.info("截图成功，文件路径为：{}".format(filePath))
        except:
            logging.exception("截图失败！！")

    # toast获取
    def get_toastMsg(self, part_str, model_name="model"):
        xpath = '//*[contains(@text,"{}")]'.format(part_str)
        logging.info("获取toast信息，toast表达式为：{}".format(xpath))
        try:
            WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located((MobileBy.XPATH, xpath)))
            return self.driver.find_element(MobileBy.XPATH, xpath)
        except:
            logging.exception("获取toast信息失败！！")
            raise

    # 获取设备的大小
    def get_device_size(self):
        try:
            size = self.driver.get_window_size()
            logging.info("当前设备的大小为：{}".format(size))
            return size
        except:
            logging.exception("获取设备大小失败。")
            raise

    # 左右滑
    def swipe_left_right(self, start_percent=0.9, end_percent=0.1):
        size = self.get_device_size()
        try:
            logging.info("页面左右滑动，页面从坐标：{} 滑动到坐标：{}".format(size["width"] * start_percent, size["width"] * end_percent))
            self.driver.swipe(size["width"] * start_percent, size["height"] * 0.5, size["width"] * end_percent,
                              size["height"] * 0.5, 200)
            time.sleep(1)
        except:
            logging.exception("页面左右滑动失败！！")
            self.save_webImg("页面左右滑动失败")
            raise

    # 上下滑
    def swipe_up_down(self, start_percent=0.9, end_percent=0.1):
        size = self.get_device_size()
        try:
            self.driver.swipe(size["width"] * 0.5, size["height"] * start_percent, size["width"] * 0.5,
                              size["height"] * end_percent, 200)
            logging.info(
                "页面上下滑动，页面从坐标：{} 滑动到坐标：{}".format(size["height"] * start_percent, size["height"] * end_percent))
            time.sleep(1)
        except:
            logging.exception("页面上下滑动失败！！")
            self.save_webImg("页面上下滑动失败")
            raise

    # 获取当前页面源码
    def get_page_source(self):
        logging.info("获取当前页面源码。")
        try:
            return self.driver.page_source
        except:
            logging.exception("获取页面源码失败！")
            self.save_webImg("获取页面源码失败")
            raise
