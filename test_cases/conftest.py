# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/10/05
E-mail:keen2020@outlook.com
=================================

"""

import pytest
import yaml
import os
from appium import webdriver
from common import logger
import logging

from common.dir_config import CAPS_DIR
from common import adb_oper as adb
from page_ojbects.login_page import LoginPage
from page_ojbects.index_page import IndexPage
from data import common_data as cd


# 专为登录用例准备 - noReset的值为False
@pytest.fixture()
def init_app():
    # 启动参数
    driver = _base_driver(noReset=False)
    yield driver
    driver.close_app()


# @pytest.fixture()
# def start_app():
#     # 启动参数
#     driver = _base_driver()
#     # 登陆状态处理
#     # _deal_logined(driver)
#     yield driver
#     driver.close_app()


@pytest.fixture()
def run_app():
    # 启动参数
    driver = _base_driver()
    # 登陆状态处理
    # _deal_logined(driver)
    yield driver
    driver.quit()
    # driver.close_app()

# def _deal_logined(driver):
#     """
#         判断用户是否已登陆。若未登陆,则进行登陆操作。最终，都会切换回应用主页面。
#         :param driver:
#         :return: None
#         """
#     ip, lp = IndexPage(driver), LoginPage(driver)
#     # 若没有登陆，则调用 登陆页面的  登陆方法。
#     login_status = ip.get_login_status()
#     if login_status is False:
#         lp.login_action(cd.c_username, cd.c_pwd)


# 定制服务器启动参数，并启动一个与appium server的会话。
def _base_driver(server_port=4723, **kwargs):
    # 读取公共的默认配置
    fs = open(os.path.join(CAPS_DIR, "desired_caps.yaml"))
    desired_caps = yaml.safe_load(fs)
    # 通过adb命令动态获取设备的平台版本号。更新到默认配置中。
    devices = adb.get_device_uuid()
    if len(devices) == 1:  # 检测到1台设备，更新配置参数。
        desired_caps["platformVersion"] = adb.get_device_plat_version(devices[0])
    elif len(devices) > 1:  # 检测到多台，暂不支持多台，所以只将第1台的配置数据更新进来
        logging.warning("目前识别到至少2台设备，无法确认使用哪个设备，默认使用第1台设备的平台版本号！")
        desired_caps["platformVersion"] = adb.get_device_plat_version(devices[0])
    else:  # 没有设备连接的时候，直接报错。
        logging.error("目前没有识别到可用设备，请确保至少1台设备可用！！")
        raise

    # 看一下是否有定制化的配置项。
    if kwargs:
        for key, value in kwargs.items():
            desired_caps[key] = value

    # 启动一个server会话。
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(server_port), desired_caps)
    driver.get_window_size()
    return driver
