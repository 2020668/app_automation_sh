# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/11/7
E-mail:keen2020@outlook.com
=================================

"""

# a = "2019-11-12 16:29:01"
# b = "2019-11-12 16:39:01"
#
# print(a < b)

from decimal import Decimal

# a = "0.01"
# b = "0.02"
# a = float(a)
# a = Decimal.from_float(a).quantize(Decimal("0.000"))
# print(a)

# a = [{"time": "2019-10-10", "amount": 0.01}]
# b = "2019-10-10"
# for i in a:
#     print(i)
#     print(b in i["time"])

# list_success_amount = "已退款 0.00元"
# list_success_amount = float(list_success_amount[4:-1])
# list_success_amount = Decimal.from_float(list_success_amount).quantize(Decimal("0.00"))
# print(list_success_amount)

# a = {""}

# a = ""
# if a:
#     print(1)
# else:
#     print(2)

# a = "2019-11-27 23:59:00 - 2019-12-27 23:59:59"
# a1 = a[:16]
# a2 = a[22:38]
# print(1)
# print(a1)
# print(a2)

import os

# command = "adb devices"
# # command = "allure serve output/allure"
# a = os.popen(command)
# info = a.readlines()    # 读取命令行输出到list
# for line in info:
#     line = line.strip("\r\n")
#     # print(line)
#     print(line)
# print(type(line1))

# a = os.system("allure serve output/allure")
# aa = 1
# a = os.system("adb devices")
# # print(a)

# 直接打开报告
# os.system("allure serve output/allure")

# 生成报告
# os.system("allure generate output/allure - o output/reports - -clean")
# os.system("allure open -h 192.168.2.222 -p 8080 output/reports")

# from datetime import date, datetime
# import datedelta
#
#
# now = datetime.now()
# delta = datedelta.datedelta(days=5)
# res = now + delta
# print(res)


# datetime = "2019-12-30 15:30"
# year = datetime[:4]
# month = datetime[5:7]
# day = datetime[8:10]
# hour = datetime[11:13]
# minute = datetime[14:16]
#
#
# print(year, month, day, hour, minute)

def relative_position():

    base_start_x = int(input("请输入截图的base_start_x:"))
    base_start_y = int(input("请输入截图的base_start_y:"))

    base_end_x = int(input("请输入截图的base_end_x:"))
    base_end_y = int(input("请输入截图的base_end_y:"))

    start_x = int(input("请输入截图的start_x:"))
    start_y = int(input("请输入截图的start_y:"))

    end_x = int(input("请输入截图的end_x:"))
    end_y = int(input("请输入截图的end_y:"))

    size_x = base_end_x - base_start_x
    size_y = base_end_y - base_start_y

    start_x = size_x - start_x
    start_y = size_y - start_y
    end_x = size_x - end_x
    end_y = size_y - end_y

    x = start_x / size_x
    y = start_y / size_y
    x1 = end_x / size_x
    y1 = end_y / size_y

    print(x, y, x1, y1)
    return x, y, x1, y1


def dem():
    x = "11月"
    x = x[:2]
    print(x)


def a1():
    x = [1, 2, 3]
    y = [4, 5, 6]
    z = x + y
    print(z)


if __name__ == '__main__':
    # relative_position()
    a1()

