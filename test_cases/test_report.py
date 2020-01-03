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
from page_ojbects.report_page import ReportPage
from common.tools import uninstall_appium_settings, uninstall_uiautomator2
from common import logger
from data import report_data as rd


@pytest.mark.report
@pytest.mark.usefixtures("run_app")
class TestReport(object):

    @pytest.mark.parametrize("data", rd.success_data)
    def test_report_all(self, data, run_app):
        # 执行登录
        # LoginPage(run_app).login_action(data["login_phone"], data["login_pwd"])

        # 执行查看订单
        ReportPage(run_app).select_all_report(week=data["week"])

        uninstall_appium_settings()
        uninstall_uiautomator2()
