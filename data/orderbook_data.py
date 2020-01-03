# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/12/18
E-mail:keen2020@outlook.com
=================================

"""

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

screen_data = [
    {"login_phone": "18971335925",
     "login_pwd": "335925",
     "main_store_name": "吉野家日式料理店",
     "store_name": "吉野家日式料理店",
     "store_id": "2019121716261782222",
     "time_desc": None,
     "time_start": None,  # 时间随便填 只能滑动选择 不能精确输入
     "time_end": None,  # 时间随便填 只能滑动选择 不能精确输入
     "terminal_name": None,  # 暂时按下标定位,为空就是所有终端
     "terminal_id": None,
     "type_source": "all",
     "status": "all"},
    # {"login_phone": "18971335925",
    #  "login_pwd": "335925",
    #  "main_store_name": "吉野家日式料理店",
    #  "store_name": "吉野家日式料理店",
    #  "store_id": "2019122413571152189",
    #  "time_desc": "本月",
    #  "time_start": None,
    #  "time_end": None,
    #  "terminal_name": None,
    #  "terminal_id": None,
    #  "type_source": "all",
    #  "status": "all"},
    # {"login_phone": "18971335925",
    #  "login_pwd": "335925",
    #  "main_store_name": "吉野家日式料理店",
    #  "store_name": "吉野家日式料理店",
    #  "store_id": "2019122413571152189",
    #  "time_desc": "近7天",
    #  "time_start": None,
    #  "time_end": None,
    #  "terminal_name": None,
    #  "terminal_id": None,
    #  "type_source": "all",
    #  "status": "all"},
    # {"login_phone": "18971335925",
    #  "login_pwd": "335925",
    #  "main_store_name": "吉野家日式料理店",
    #  "store_name": "吉野家日式料理店",
    #  "store_id": "2019122413571152189",
    #  "time_desc": "近24小时",
    #  "time_start": None,
    #  "time_end": None,
    #  "terminal_name": None,
    #  "terminal_id": None,
    #  "type_source": "all",
    #  "status": "all"},
    # {"login_phone": "18971335925",
    #  "login_pwd": "335925",
    #  "main_store_name": "吉野家日式料理店",
    #  "store_name": "吉野家日式料理店",
    #  "store_id": "2019122413571152189",
    #  "time_start": "2019-10-16 23:59",
    #  "time_end": "2019-11-15 23:59",
    #  "terminal_name": None,
    #  "terminal_id": None,
    #  "type_source": "weixin",
    #  "status": "all"},
    # {"login_phone": "18971335925",
    #  "login_pwd": "335925",
    #  "main_store_name": "吉野家日式料理店",
    #  "store_name": "吉野家日式料理店",
    #  "store_id": "2019122413571152189",
    #  "time_start": "2019-10-16 23:59",
    #  "time_end": "2019-11-15 23:59",
    #  "terminal_name": None,
    #  "terminal_id": None,
    #  "type_source": "alipay",
    #  "status": "all"},
    # {"login_phone": "18971335925",
    #  "login_pwd": "335925",
    #  "main_store_name": "吉野家日式料理店",
    #  "store_name": "吉野家日式料理店",
    #  "store_id": "2019122413571152189",
    #  "time_start": "2019-10-16 23:59",
    #  "time_end": "2019-11-15 23:59",
    #  "terminal_name": None,
    #  "terminal_id": None,
    #  "type_source": "pos",
    #  "status": "all"},
    # {"login_phone": "18971335925",
    #  "login_pwd": "335925",
    #  "main_store_name": "吉野家日式料理店",
    #  "store_name": "吉野家日式料理店",
    #  "store_id": "2019122413571152189",
    #  "time_start": "2019-10-16 23:59",
    #  "time_end": "2019-11-15 23:59",
    #  "terminal_name": None,
    #  "terminal_id": None,
    #  "type_source": "auth",
    #  "status": "all"},
    # {"login_phone": "18971335925",
    #  "login_pwd": "335925",
    #  "main_store_name": "吉野家日式料理店",
    #  "store_name": "吉野家日式料理店",
    #  "store_id": "2019122413571152189",
    #  "time_start": "2019-10-16 23:59",
    #  "time_end": "2019-11-15 23:59",
    #  "terminal_name": None,
    #  "terminal_id": None,
    #  "type_source": "other",
    #  "status": "all"},
]
