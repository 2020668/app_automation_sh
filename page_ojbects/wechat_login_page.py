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
from page_locators.wechat_login_page_locator import WechatLoginPageLocator as Loc
from common import logger


class WechatLoginPage(BasePage):

    # 微信登录
    def wechat_login(self):
        self.wait_ele_visible(loc=Loc.wechat_login_button_loc, img_desc="登录页的微信登录按钮")
        self.click_element(loc=Loc.wechat_login_button_loc, img_desc="登录页的微信登录按钮")

    # 绑定微信登录
    def binding_wechat_login(self, phone):
        self.wait_ele_visible(loc=Loc.wechat_login_button_loc, img_desc="登录页的微信登录按钮")
        self.click_element(loc=Loc.wechat_login_button_loc, img_desc="登录页的微信登录按钮")

        self.wait_ele_visible(loc=Loc.phone_input_loc, img_desc="手机号输入框")
        self.input_text(loc=Loc.phone_input_loc, value=phone, img_desc="手机号输入框")

        self.wait_ele_visible(loc=Loc.get_code_button_loc, img_desc="获取验证码按钮")
        self.click_element(loc=Loc.get_code_button_loc, img_desc="获取验证码按钮")

        code = input("请输入短信验证码:")

        self.wait_ele_visible(loc=Loc.code_input_loc, img_desc="短信验证码输入框")
        self.input_text(loc=Loc.code_input_loc, value=code, img_desc="短信验证码输入框")

        self.wait_ele_visible(loc=Loc.binding_button_loc, img_desc="立即绑定按钮")
        self.click_element(loc=Loc.binding_button_loc, img_desc="立即绑定按钮")

    def get_wecaht_login_status(self):
        self.wait_ele_visible(loc=Loc.wechat_login_status, img_desc="我的 页 的微信登录绑定状态")
        status = self.get_text(loc=Loc.wechat_login_status, img_desc="我的 页 的微信登录绑定状态")
        return status

    # 解绑微信登录
    def untying_wecaht_login(self):
        self.wait_ele_visible(loc=Loc.me_wechat_login, img_desc="我的 页 的微信快捷登录按钮")
        self.click_element(loc=Loc.me_wechat_login, img_desc="我的 页 的微信快捷登录按钮")

        self.wait_ele_visible(loc=Loc.untying_cancel_loc, img_desc="解绑的取消按钮")
        self.click_element(loc=Loc.untying_cancel_loc, img_desc="解绑的取消按钮")

        self.wait_ele_visible(loc=Loc.me_wechat_login, img_desc="我的 页 的微信快捷登录按钮")
        self.click_element(loc=Loc.me_wechat_login, img_desc="我的 页 的微信快捷登录按钮")

        self.wait_ele_visible(loc=Loc.untying_confirm_loc, img_desc="解绑的确定按钮")
        self.click_element(loc=Loc.untying_confirm_loc, img_desc="解绑的确定按钮")

    # 解绑后的确认
    def after_untying_wecaht_login(self):
        self.wait_ele_visible(loc=Loc.wechat_login_button_loc, img_desc="微信登录按钮")
        self.click_element(loc=Loc.wechat_login_button_loc, img_desc="微信登录按钮")

        self.wait_ele_visible(loc=Loc.account_binding_title_loc, img_desc="账号绑定页的标题")
        title = self.get_text(loc=Loc.account_binding_title_loc, img_desc="账号绑定页的标题")

        return title
