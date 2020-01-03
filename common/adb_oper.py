# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

import subprocess
import chardet

"""
本模块 是为了 动态获取当前连接的安卓设备数。，并获取设备对应的安卓 版本号。

一共提供了3个函数
函数1：get_device_uuid： 通过adb devices命令，获取所有的状态为device的在线安卓设备。
                         返回一个列表，列表当中，为设备的uuid.

函数2：get_device_platVersion: 根据设备的uuid，获取设备的平台版本号。比如8.1.
                         参数为：设备的uuid.

函数3：_run_command_and_get_stout： 执行命令并得到命令执行后的输出内容。
"""


# 获取设备的uuid
def get_device_uuid():
    device_uuid = []
    # 终端命令行命令。
    command = "adb devices"
    result = _run_command_and_get_stout(command)
    # ['List of devices attached', '08e7c5997d2a\tdevice', 'emulator-5554\tdevice', '', '']
    device_list = result.split("\r\n")
    for item in device_list:  # 遍历adb devices 输出的内容
        if item.find("\t") != -1:  # 获取设备信息
            temp = item.split("\t")
            if temp[1] == "device":  # 设备为可识别状态。有些可能是offline、unauthorized等。
                device_uuid.append(temp[0])
    return device_uuid


# 得到设备的平台版本号。
def get_device_plat_version(device_uuid):
    command = 'adb -P 5037 -s {} shell getprop ro.build.version.release'.format(device_uuid)
    result = _run_command_and_get_stout(command)
    return result


# 执行命令行并获取返回值。 比如adb命令，aapt命令。
def _run_command_and_get_stout(command):
    # 执行command的，并获取命令执行之后的输出数据。
    stdout, stderror = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        shell=True).communicate()
    # 编码处理
    # print(stdout)
    encoding = chardet.detect(stdout)["encoding"]
    result = stdout.decode(encoding)

    result = result.strip("\r\n")  # 去掉首尾的换行回车
    # print(result)
    return result
