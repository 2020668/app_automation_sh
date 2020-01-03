# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/5

E-mail:keen2020@outlook.com

=================================


"""

from common.basepage import BasePage
from page_locators.my_page_locator import MyPageLocator as Loc
from common.tools import uninstall_appium_settings, uninstall_uiautomator2


class LogoutPage(BasePage):

    # 登录操作
    def logout_action(self):
        self.wait_ele_visible(Loc.my_loc, "首页_等待 我的 元素可见")
        self.get_element(Loc.my_loc, "首页_等待 我的 元素可见", find_all=True)[2].click()
        # self.click_element(Loc.my_loc, img_desc="首页_我的按钮")

        self.wait_ele_visible(Loc.set_loc, "我的页_等待 设置 元素可见")
        self.click_element(Loc.set_loc, img_desc="我的页_设置按钮")

        self.wait_ele_visible(Loc.logout_loc, "设置页_等待 退出登录 元素可见")
        self.click_element(Loc.logout_loc, img_desc="设置页_退出登录按钮按钮")

        self.wait_ele_visible(Loc.yes_loc, "退出登录弹窗_等待 确定 元素可见")
        self.click_element(Loc.yes_loc, img_desc="退出登录弹窗_确定按钮")

        return self

    # uninstall_appium_settings()
    # uninstall_uiautomator2()
