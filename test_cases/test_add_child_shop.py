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


@pytest.mark.add
@pytest.mark.usefixtures("run_app")
class TestAddChildShop(object):

    @pytest.mark.parametrize("data", ad.add_success_data)
    def test_add_child_shop(self, data, run_app):
        # 执行登录
        LoginPage(run_app).login_action(data["login_phone"], data["login_pwd"])

        # 执行添加子门店
        ChildShopPage(run_app).add_shop_action(
                                        shop_name=data["shop_name"],
                                        shop_address=data["shop_address"],
                                        people_name=data["people_name"],
                                        phone_num=data["phone_num"],
                                        pwd=data["pwd"]
                                    )

        uninstall_appium_settings()
        uninstall_uiautomator2()
