# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/12/18
E-mail:keen2020@outlook.com
=================================

"""

import logging
from common import logger

"""

全部门店 不传store_id   storeName 全部门店
指定门店 storeName 固定为->指定门店  传对应门店的store_id
全部终端 terminalName 全部终端
指定终端 terminalName 指定终端  terminal 设备前缀:终端id  前缀如下
扫码王/扫码盒子 sl51:终端id
收款码 qr_pay:终端id
POS机 n910:终端id
倾蜻蜓刷脸设备 qt-f4:终端id
微收银插件 qwx:终端id
易锐插件 inspiry:终端id
支付方式 全部 "" weixin alipay pos auth other
支付状态 全部 status ""  支付成功1 已退款3

账单筛选测试数据总和 936

"""

success_data = [
    {"login_phone": "18971335925",
     "login_pwd": "335925",
     "amount": "0.01",
     "pwd": "123456",
     "shop_name": "火锅一店",
     "note_pay_success": "自动测试支付成功备注",
     "note_refund_all": "自动测试全额退款备注",
     "note_refund_part": "自动测试部分退款备注"}
]


# 主门店 筛选条件组合 子门店的数据加上主门店的数据一起 list相加
def order_main_screen_data():

    # 主门店筛选 全部门店 * 全部终端 72
    # time_list = ["本月", "近7天", "近24小时", {"time_start": "2019-12-10 08:03", "time_end": "2020-01-07 06:00"}]
    # store_list = ["全部门店"]
    # terminal_list = ["全部终端"]
    # payment_list = ["全部", "微信", "支付宝", "刷卡", "预授权", "其他"]
    # status_list = ["全部订单", "支付成功", "退款成功"]

    # 主门店筛选 全部门店 2个具体终端 144
    # time_list = ["本月", "近7天", "近24小时", {"time_start": "2019-12-10 08:03", "time_end": "2020-01-07 06:00"}]
    # store_list = ["全部门店"]
    # terminal_list = [{"name": "收款一号机", "terminal_id": "qr_pay:NO_2018122515457307981444"},
    # {"name": "收款1号机", "terminal_id": "qr_pay:NO_2018122515457307773472"} ]
    # payment_list = ["全部", "微信", "支付宝", "刷卡", "预授权", "其他"]
    # status_list = ["全部订单", "支付成功", "退款成功"]

    # 主门店筛选主门店  144
    # time_list = ["本月", "近7天", "近24小时", {"time_start": "2019-12-10 08:03", "time_end": "2020-01-07 06:00"}]
    # store_list = [{"name": "吉野家日式料理店", "id": "2019121716261782222"}]
    # terminal_list = ["全部终端", {"name": "收款一号机", "terminal_id": "qr_pay:NO_2018122515457307981444"}]
    # payment_list = ["全部", "微信", "支付宝", "刷卡", "预授权", "其他"]
    # status_list = ["全部订单", "支付成功", "退款成功"]

    # 主门店筛选子门店 144
    # time_list = ["本月", "近7天", "近24小时", {"time_start": "2019-12-10 08:03", "time_end": "2020-01-07 06:00"}]
    # store_list = [{"name": "吉野家一分店", "id": "2019122413571152189"}]
    # terminal_list = ["全部终端", {"name": "收款1号机", "terminal_id": "qr_pay:NO_2018122515457307773472"}]
    # payment_list = ["全部", "微信", "支付宝", "刷卡", "预授权", "其他"]
    # status_list = ["全部订单", "支付成功", "退款成功"]

    # 调试数据
    time_list = ["本月", "近7天", "近24小时"]
    store_list = [{"name": "吉野家日式料理店", "id": "2019121716261782222"}]
    terminal_list = ["全部终端"]
    payment_list = ["全部", "微信", "支付宝", "刷卡", "预授权", "其他"]
    status_list = ["全部订单", "支付成功", "退款成功"]

    return composite_data(login_phone='18971335925', login_pwd='335925', time_list=time_list,
                          terminal_list=terminal_list, payment_list=payment_list, status_list=status_list)


# 子门店 筛选条件组合 子门店的数据加上主门店的数据一起 list相加
def order_child_screen_data():

    # 子门店筛选 没有门店可选  144
    # time_list = ["本月", "近7天", "近24小时", {"time_start": "2019-12-10 08:03", "time_end": "2020-01-07 06:00"}]
    # terminal_list = ["全部终端", {"name": "收款1号机", "terminal_id": "qr_pay:NO_2018122515457307773472"}]
    # payment_list = ["全部", "微信", "支付宝", "刷卡", "预授权", "其他"]
    # status_list = ["全部订单", "支付成功", "退款成功"]

    # 调试数据
    time_list = ["本月", "近7天", "近24小时"]
    terminal_list = ["全部终端", {"name": "收款1号机", "terminal_id": "qr_pay:NO_2018122515457307773472"}]
    payment_list = ["全部", "微信", "支付宝", "刷卡", "预授权", "其他"]
    status_list = ["全部订单", "支付成功", "退款成功"]

    return composite_data(login_phone='18971330001', login_pwd='123456', time_list=time_list,
                          terminal_list=terminal_list, payment_list=payment_list, status_list=status_list)


# 主门店收银员 筛选条件组合 子门店的数据加上主门店的数据一起 list相加
def order_main_cashier_screen_data():

    # 主门店收银员 筛选 没有门店可选  144
    time_list = ["本月", "近7天", "近24小时", {"time_start": "2019-12-10 08:03", "time_end": "2020-01-07 06:00"}]
    terminal_list = ["全部终端", {"name": "收款一号机", "terminal_id": "qr_pay:NO_2018122515457307981444"}]
    payment_list = ["全部", "微信", "支付宝", "刷卡", "预授权", "其他"]
    status_list = ["全部订单", "支付成功", "退款成功"]

    # 调试数据
    # time_list = ["本月", "近7天", "近24小时"]
    # terminal_list = ["全部终端", {"name": "收款一号机", "terminal_id": "qr_pay:NO_2018122515457307981444"}]
    # payment_list = ["全部", "微信"]
    # status_list = ["全部订单"]

    return composite_data(login_phone='18971335952', login_pwd='123456', time_list=time_list,
                          terminal_list=terminal_list, payment_list=payment_list, status_list=status_list)


# 子门店收银员 筛选条件组合 子门店的数据加上主门店的数据一起 list相加
def order_child_cashier_screen_data():

    # 子门店收银员 筛选 没有门店可选  144
    # time_list = ["本月", "近7天", "近24小时", {"time_start": "2019-12-10 08:03", "time_end": "2020-01-07 06:00"}]
    # terminal_list = ["全部终端", {"name": "收款1号机", "terminal_id": "qr_pay:NO_2018122515457307773472"}]
    # payment_list = ["全部", "微信", "支付宝", "刷卡", "预授权", "其他"]
    # status_list = ["全部订单", "支付成功", "退款成功"]

    # 调试数据
    time_list = ["本月", "近7天", "近24小时"]
    terminal_list = ["全部终端", {"name": "收款1号机", "terminal_id": "qr_pay:NO_2018122515457307773472"}]
    payment_list = ["全部", "微信", "支付宝", "刷卡", "预授权", "其他"]
    status_list = ["全部订单", "支付成功", "退款成功"]

    return composite_data(login_phone='18971330010', login_pwd='123456', time_list=time_list,
                          terminal_list=terminal_list, payment_list=payment_list, status_list=status_list)


def composite_data(login_phone, login_pwd, time_list, terminal_list, payment_list, status_list):
    data = list()
    for time in time_list:
        for terminal in terminal_list:
            for payment in payment_list:
                for status in status_list:
                    res = {"login_phone": login_phone,
                           "login_pwd": login_pwd,
                           "main_store_name": "吉野家日式料理店",
                           "store_name": None,
                           "store_id": None,
                           "time_desc": time if type(time) is str else None,
                           "time_start": time["time_start"] if type(time) is dict else None,
                           "time_end": time["time_end"] if type(time) is dict else None,
                           "terminal_type": "指定终端" if type(terminal) is dict else terminal,
                           "terminal_name": terminal["name"] if type(terminal) is dict else None,
                           "terminal_id": terminal["terminal_id"] if type(terminal) is dict else None,
                           "type_source": payment,
                           "status": status
                           }
                    data.append(res)
    logging.info("测试数据: {}".format(data))
    logging.info("账单筛选测试数据量: {}".format(len(data)))
    return data


# screen_data = order_main_screen_data()
# screen_data = order_child_screen_data()
screen_data = order_child_cashier_screen_data()
# screen_data = order_main_cashier_screen_data()


if __name__ == '__main__':
    result = order_main_cashier_screen_data()
    print(result)
    print(len(result))



