# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

import os
import time
import logging

from common import logger
from API.http_request import HTTPRequest


def uninstall_uiautomator2():
    os.system("adb uninstall io.appium.uiautomator2.server")
    print("uninstall uiautomator2.server successfully")

    os.system("adb uninstall io.appium.uiautomator2.server.test")
    print("uninstall uiautomator2.server.test successfully")


def uninstall_appium_settings():
    os.system("adb uninstall io.appium.settings")
    print("uninstall appium.settings successfully")


def get_line_token(phone, pwd, imei, voip_imei=None):
    request = HTTPRequest()
    url = "https://api.hczypay.com/api/merchant/login"
    if voip_imei:
        request_data = {"phone": phone, "password": pwd, "imei": imei, "type": "phone", "voip_imei": voip_imei}
    else:
        request_data = {"phone": phone, "password": pwd, "imei": imei, "type": "jg"}
    response = request.request(
        method="post", url=url, data=request_data)
    token = response.json()["token"]
    request.close()
    logging.info("===================================")
    logging.info("登录请求地址--> {}".format(url))
    logging.info("登录请求参数--> {}".format(request_data))
    logging.info("登录结果--> {}".format(response.json()))
    # 退出登录
    logout(phone=phone, token=token)
    time.sleep(1)
    return token


def logout(phone, token):
    request = HTTPRequest()
    request_data = {'phone': phone,
                    'imei': '919dc52afd82279be4f9ff04288be30a9de665ff8fd68b437dbe93953b8e07c9', 'token': token}
    url = "https://api.hczypay.com/api/merchant/logout"
    response = request.request(method="post", url=url, data=request_data)
    res = response.json()
    logging.info("退出登录结果--> {}".format(res))


def get_cmd_result(command):
    a = os.popen(command)
    info = a.readlines()  # 读取命令行输出到list
    for line in info:
        line = line.strip("\r\n")
        print(line)
        print(type(line))


if __name__ == '__main__':
    uninstall_uiautomator2()
    uninstall_appium_settings()

    # get_cmd_result("allure serve output/allure")
    # get_cmd_result("adb devices")

