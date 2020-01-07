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
from caps.read_yaml import conf

from API.http_request import HTTPRequest
from common.tools import get_token


def api_my_order_book(login_phone, login_pwd, page, terminal_name, terminal_id, time_start, time_end, type_source, store_name,
                      store_id, order_status):
    """
    data = {"page": 1, "terminalName": "全部终端", "time_start": "2019-11-18 23:59", "time_end": "2019-12-18 23:59",
             "type_source": "weixin", "token": token, "storeName": "全部门店", "status": "", store_id: ""}
    全部门店 不传store_id   storeName 全部门店
    指定门店 storeName 指定门店  传对应门店的store_id
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

    # url = "https://api.hczypay.com/api/merchant/myOrderBook"
    url = conf.get("env").get("url") + "/api/merchant/myOrderBook"

    # 调用登录方法获取
    token = get_token(phone=login_phone, pwd=login_pwd,
                      imei="919dc52afd82279be4f9ff04288be30a9de665ff8fd68b437dbe93953b8e07c9")

    request = HTTPRequest()

    data = {"page": page,
            "terminalName": terminal_name,
            "terminal": terminal_id,
            "time_start": time_start,
            "time_end": time_end,
            "type_source": type_source,
            "token": token,
            "storeName": store_name,
            "store_id": store_id,
            "status": order_status}

    response = request.request(method="post", url=url, data=data)

    result = response.json()
    logging.info("======================================")
    logging.info("账单筛选请求地址--> {}".format(url))
    logging.info("账单筛选请求参数--> {}".format(data))
    logging.info("账单筛选返回结果--> {}".format(result))
    logging.info("======================================")

    # # 收款人 全部收款人
    # api_merchant_name = res["data"]["inquire"]["merchantName"]
    #
    # # 支付状态 全部
    # api_order_status = res["data"]["inquire"]["orderStatus"]
    #
    # # 门店选择 全部门店
    # api_store_name = res["data"]["inquire"]["storeName"]
    #
    # # 收银终端 全部终端
    # api_terminal_name = res["data"]["inquire"]["terminalName"]
    #
    # # 支付方式 微信
    # api_type_source = res["data"]["inquire"]["typeSource"]
    #
    # # 收款笔数
    # api_success_count = res["data"]["inquire"]["success_count"]
    #
    # # 开始时间 去掉秒钟
    # api_time_start = res["data"]["inquire"]["timeStart"][0:-3]
    #
    # # 结束时间 去掉秒钟
    # api_time_end = res["data"]["inquire"]["timeEnd"][0:-3]
    #
    # # 收款金额
    # api_success_amount = res["data"]["inquire"]["success_amount"]
    #
    # # 退款笔数
    # api_refund_count = res["data"]["inquire"]["refund_count"]
    #
    # # 退款金额
    # api_refund_amount = res["data"]["inquire"]["refund_amount"]

    return result["data"]["inquire"]


if __name__ == '__main__':
    res = api_my_order_book(login_phone="18971335925",
                            login_pwd="335925",
                            page=1,
                            terminal_name="全部终端",
                            terminal_id="",
                            time_start="2019-11-18 23:59",
                            time_end="2019-12-18 23:59",
                            type_source="weixin",
                            store_name="全部门店",
                            store_id="",
                            order_status="",
                            )

    print(res)

