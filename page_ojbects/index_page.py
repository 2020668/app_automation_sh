# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""


import logging
import time


from common.basepage import BasePage
from page_locators.index_page_locator import IndexPageLocator as Loc
from common import logger


class IndexPage(BasePage):

    # 点击导航栏内容
    def click_nav_by_name(self, nav_name):
        """
        :param nav_name: 导航名称 首页、服务、我的
        :return: None
        """
        if nav_name == "首页":
            self.click_element(Loc.nav_loc, "首页_点击主页按钮", 0)
        elif nav_name == "服务":
            self.click_element(Loc.nav_loc, "首页_点击服务按钮", 1)
        elif nav_name == "我的":
            self.click_element(Loc.nav_loc, "首页_点击我的按钮", 2)
        else:
            logging.ERROR("没有此导航名称 --> {}".format(nav_name))

    # 点击 首页 按钮
    def click_home_page_button(self):
        self.wait_ele_visible(loc=Loc.home_page_button_loc, img_desc="首页_点击首页按钮")
        self.click_element(loc=Loc.home_page_button_loc, img_desc="首页_点击首页按钮")

    # 点击 服务 按钮
    def click_service_button(self):
        self.wait_ele_visible(loc=Loc.service_button_loc, img_desc="首页_点击服务按钮")
        self.click_element(loc=Loc.service_button_loc, img_desc="首页_点击服务按钮")

    # 点击 我的 按钮
    def click_my_button(self):
        self.wait_ele_visible(loc=Loc.my_button_loc, img_desc="首页_点击我的按钮")
        self.click_element(loc=Loc.my_button_loc, img_desc="首页_点击我的按钮")

    # 获取登录状态
    def get_login_status(self):
        status = self.get_text(Loc.order_nav_loc, img_desc="首页_获取用户登录状态")
        if status == "账单":
            return True
        else:
            return False

    def scan_pay(self, amount):
        self.wait_ele_visible(Loc.scan_loc, img_desc="首页_扫一扫按钮")
        self.click_element(Loc.scan_loc, img_desc="首页_扫一扫按钮")

        self.wait_ele_visible(Loc.input_amount_loc, img_desc="金额输入框")
        self.input_text(Loc.input_amount_loc, value=amount, img_desc="输入金额")

        self.wait_ele_visible(Loc.sure_loc, img_desc="确定按钮")
        self.click_element(Loc.sure_loc, img_desc="确定按钮")

        self.wait_ele_visible(Loc.success_sure_loc, img_desc="确定按钮")
        self.click_element(Loc.success_sure_loc, img_desc="确定按钮")

        # self.wait_ele_visible(Loc.back_loc, img_desc="返回按钮")
        # self.click_element(Loc.back_loc, img_desc="返回按钮")





