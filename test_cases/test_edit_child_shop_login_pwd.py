# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/11/1
E-mail:keen2020@outlook.com
=================================

"""

import pytest

from page_ojbects.login_page import LoginPage
from page_ojbects.child_shop_page import ChildShopPage
from common.tools import uninstall_appium_settings, uninstall_uiautomator2
from data import child_shop_data as ad


@pytest.mark.edit_child_shop_login_pwd
@pytest.mark.usefixtures("run_app")
class TestEditChildShopPwd(object):

    @pytest.mark.parametrize("data", ad.edit_success_data)
    def test_edit_child_shop_pwd(self, data, run_app):
        # 执行登录
        LoginPage(run_app).login_action(data["login_phone"], data["login_pwd"])

        # 执行添加子门店
        ChildShopPage(run_app).edit_child_shop_login_pwd(
                                        shop_num=data["shop_num"],
                                        pwd=data["new_pwd"]
                                    )

        uninstall_appium_settings()
        uninstall_uiautomator2()
