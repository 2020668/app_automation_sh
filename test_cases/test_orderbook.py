# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/11/5
E-mail:keen2020@outlook.com
=================================

"""

import pytest
import logging

from page_ojbects.login_page import LoginPage
from page_ojbects.logout_page import LogoutPage
from page_ojbects.orderbook_page import OrderBookPage
from common.tools import uninstall_appium_settings, uninstall_uiautomator2
from common import logger
from data import orderbook_data as od
from API.api_screen_orderbook import api_my_order_book


@pytest.mark.smoke
@pytest.mark.order
@pytest.mark.usefixtures("run_app")
class TestOrderBook(object):

    @pytest.mark.select
    @pytest.mark.parametrize("data", od.success_data)
    def test_select_order_book(self, data, run_app):
        # 执行登录
        LoginPage(run_app).login_action(data["login_phone"], data["login_pwd"])

        # 执行查看订单并添加备注
        OrderBookPage(run_app).select_pay_success_order(note=data["note_pay_success"])

        OrderBookPage(run_app).select_refund_all_order(note=data["note_refund_all"])

        OrderBookPage(run_app).select_refund_part_order(note=data["note_refund_part"])

        OrderBookPage(run_app).select_first_five_order(data=data, number=5)

        uninstall_appium_settings()
        uninstall_uiautomator2()

    @pytest.mark.refund
    @pytest.mark.parametrize("data", od.success_data)
    def test_refund(self, data, run_app):
        # 执行登录
        # LoginPage(run_app).login_action("18971335925", "335925")
        LoginPage(run_app).login_action(data["login_phone"], data["login_pwd"])

        # 执行退款,退款金额amount,支付密码pwd,退款次数num,可不输,默认{全额退款,支付密码123456,退款次数1}
        OrderBookPage(run_app).refund(num=3)

        LogoutPage(run_app).logout_action()

        uninstall_appium_settings()
        uninstall_uiautomator2()

    # 确保APP自动化查询的结果与调相应接口的返回数据一致
    @pytest.mark.screen
    @pytest.mark.parametrize("data", od.screen_data)
    def test_screen_order(self, data, run_app):
        # 执行登录
        LoginPage(run_app).login_action(data["login_phone"], data["login_pwd"])

        screen_result = OrderBookPage(run_app).screen_order(login_phone=data["login_phone"],
                                                            login_pwd=data["login_pwd"],
                                                            main_store_name=data["main_store_name"],
                                                            store_name=data["store_name"],
                                                            store_id=data["store_id"],
                                                            time_desc=data["time_desc"],
                                                            time_start=data["time_start"],
                                                            time_end=data["time_end"],
                                                            terminal_type=data["terminal_type"],
                                                            terminal_name=data["terminal_name"],
                                                            terminal_id=data["terminal_id"],
                                                            type_source=data["type_source"],
                                                            status=data["status"]
                                                            )

        # 调接口会将APP挤下线 所以在调接口前APP退出登录
        LogoutPage(run_app).logout_action()

        api_res = api_my_order_book(login_phone=data["login_phone"],
                                    login_pwd=data["login_pwd"],
                                    page="1",
                                    time_start=screen_result["api_time_start"],
                                    time_end=screen_result["api_time_end"],
                                    store_name=screen_result["api_store_name"],
                                    store_id=screen_result["api_store_id"],
                                    order_status=screen_result["api_status"],
                                    terminal_name=screen_result["api_terminal_name"],
                                    terminal_id=screen_result["api_terminal_id"],
                                    type_source=screen_result["api_type_source"])

        # 调接口获取付款笔数、付款金额、退款笔数、退款金额 与 筛选后的页面数据进行对比 页面滑动汇总数据存在不稳定性
        assert screen_result["screen_result_success_num"] == str(api_res["success_count"])

        assert screen_result["screen_result_success_amount"] == api_res["success_amount"]

        assert screen_result["screen_result_refund_num"] == str(api_res["refund_count"])

        assert screen_result["screen_result_refund_amount"] == api_res["refund_amount"]

        # uninstall_appium_settings()
        # uninstall_uiautomator2()

