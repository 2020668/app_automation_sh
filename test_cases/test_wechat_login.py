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

from page_ojbects.wechat_login_page import WechatLoginPage
from page_ojbects.index_page import IndexPage
from page_ojbects.logout_page import LogoutPage
from common.tools import uninstall_appium_settings, uninstall_uiautomator2
from data import wechat_login_data as wld
from data import index_data as id


# @pytest.mark.usefixtures("start_app")
@pytest.mark.smoke
@pytest.mark.wechat_login
@pytest.mark.usefixtures("run_app")
class TestWecahtLogin(object):

    @pytest.mark.parametrize("data", wld.success_data)
    def test_wechat_login_0_success(self, data, run_app):

        # 安卓端还缺少服务协议

        # 绑定微信登录,并登录
        WechatLoginPage(run_app).binding_wechat_login(phone=data["phone"])

        # 获取登录状态
        assert IndexPage(run_app).get_login_status() is True

        # 点击我的 跳转到我也页
        IndexPage(run_app).click_my_button()

        # 获取绑定状态并断言
        assert WechatLoginPage(run_app).get_wecaht_login_status() == "已绑定"

        # 防止短信还未消失 干扰点击设置按钮
        time.sleep(3)

        # 退出登录
        LogoutPage(run_app).logout_action()

        # 执行微信登录
        WechatLoginPage(run_app).wechat_login()

        # 获取登录状态并断言
        assert IndexPage(run_app).get_login_status() is True

        # 点击我的 跳转到我也页
        IndexPage(run_app).click_my_button()

        # 获取绑定状态并断言
        assert WechatLoginPage(run_app).get_wecaht_login_status() == "已绑定"

        # 解绑
        WechatLoginPage(run_app).untying_wecaht_login()

        # 获取绑定状态并断言
        assert WechatLoginPage(run_app).get_wecaht_login_status() == "未绑定"

        # 登出
        LogoutPage(run_app).logout_action()

        # 解绑后的确认并断言 再次打开APP的状态显示
        assert WechatLoginPage(run_app).after_untying_wecaht_login() == "账号绑定"

        uninstall_uiautomator2()
        uninstall_appium_settings()



