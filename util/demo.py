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

from datetime import date, datetime
import datedelta


now = datetime.now()
delta = datedelta.datedelta(days=5)
res = now + delta
print(res)





