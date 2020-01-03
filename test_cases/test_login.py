# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

import pytest
import time

from page_ojbects.login_page import LoginPage
from page_ojbects.index_page import IndexPage
from page_ojbects.logout_page import LogoutPage
from common.tools import uninstall_appium_settings, uninstall_uiautomator2
from data import login_data as ld
from data import index_data as id


# @pytest.mark.usefixtures("start_app")
@pytest.mark.smoke
@pytest.mark.usefixtures("run_app")
class TestLogin(object):

    @pytest.mark.parametrize("data", ld.success_data)
    def test_login_0_success(self, data, run_app):
        # 执行登录
        LoginPage(run_app).login_action(data["user"], data["pwd"])

        # 获取登录状态
        assert IndexPage(run_app).get_login_status() is True

        # 执行登出
        LogoutPage(run_app).logout_action()

        uninstall_uiautomator2()
        uninstall_appium_settings()

    # @pytest.mark.parametrize("data", ld.no_user)
    # def test_login_1__no_user(self, data, run_app):
    #     # 执行登录
    #     LoginPage(run_app).login_action(data["user"], data["pwd"])
    #     # 获取提示语并断言
    #     assert data["check"] == LoginPage(run_app).get_no_user_msg()
    #
    #     uninstall_uiautomator2()
    #     uninstall_appium_settings()
    #
    # @pytest.mark.parametrize("data", ld.no_pwd)
    # def test_login_2_no_pwd(self, data, run_app):
    #     # 执行登录
    #     LoginPage(run_app).login_action(data["user"], data["pwd"])
    #
    #     # 获取提示语并断言
    #     assert data["check"] == LoginPage(run_app).get_no_pwd_msg()
    #
    #     uninstall_uiautomator2()
    #     uninstall_appium_settings()
    #
    # @pytest.mark.parametrize("data", ld.wrong_data)
    # def test_login_3_wrong_data(self, data, run_app):
    #     # 执行登录
    #     LoginPage(run_app).login_action(data["user"], data["pwd"])
    #
    #     # 获取提示语并断言
    #     assert data["check"] == LoginPage(run_app).get_wrong_msg()
    #
    #     # 点击我知道了
    #     LoginPage(run_app).click_i_know()
    #
    #     uninstall_uiautomator2()
    #     uninstall_appium_settings()
    #
    # @pytest.mark.parametrize("data", ld.success_data)
    # def test_scan_0_success(self, data, run_app):
    #     # 执行登录
    #     LoginPage(run_app).login_action(data["user"], data["pwd"])
    #
    #     # 扫一扫付款
    #     IndexPage(run_app).scan_pay(amount="0.01")
    #
    #     # 执行登出
    #     LogoutPage(run_app).logout_action()
    #
    #     uninstall_uiautomator2()
    #     uninstall_appium_settings()
    #
    # @pytest.mark.parametrize("data", ld.success_data)
    # def test_scan_0_success(self, data, run_app):
    #     # 执行登录
    #     LoginPage(run_app).login_action(data["user"], data["pwd"])
    #
    #     count = 1
    #     for i in range(3):
    #
    #         # 扫一扫付款
    #         IndexPage(run_app).scan_pay(amount="0.01")
    #         print("第{}次付款".format(count))
    #         count += 1
    #
    #     # 执行登出
    #     LogoutPage(run_app).logout_action()
    #
    #     uninstall_uiautomator2()
    #     uninstall_appium_settings()
    #
    # @pytest.mark.parametrize("data", ld.success_data)
    # def test_refund_0_success(self, data, run_app):
    #     # 执行登录
    #     LoginPage(run_app).login_action(data["user"], data["pwd"])
    #
    #     # 执行退款
    #     IndexPage(run_app).refund(amount="0.01", pwd="123456")
    #
    #     # 执行登出
    #     LogoutPage(run_app).logout_action()
    #
    #     uninstall_uiautomator2()
    #     uninstall_appium_settings()

