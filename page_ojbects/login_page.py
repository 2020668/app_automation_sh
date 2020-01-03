# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

from common.basepage import BasePage
from page_locators.login_page_locator import LoginPageLocator as Loc
from common.tools import uninstall_appium_settings, uninstall_uiautomator2
from data.common_data import CommonData as Cd


class LoginPage(BasePage):

    # 登录操作
    def login_action(self, username, pwd):
        self.wait_ele_visible(Loc.user_loc, "登录页_等待用户名元素可见")
        self.input_text(Loc.user_loc, value=username, img_desc="登录页_输入用户名")
        self.input_text(Loc.pwd_loc, value=pwd, img_desc="登录页_输入密码")
        self.click_element(Loc.login_button_loc, img_desc="登录页_点击登录按钮")
        return self

    # 获取登出状态
    def get_logout_status(self):
        self.wait_ele_visible(Loc.user_loc, "登录页_等待用户名元素可见")
        status = self.get_text(Loc.user_loc, img_desc="登录页_输入用户名")
        if status == Cd.c_username:
            return True
        else:
            return False

    # 获取手机号为空的提示语
    def get_no_user_msg(self):
        self.wait_ele_exists(Loc.input_user_loc, "登录页_等待 提示语 请输入账号 元素存在")
        status = self.get_text(Loc.input_user_loc, img_desc="登录页_提示语 请输入账号")
        return status

    # 获取手机号为空的提示语
    def get_no_pwd_msg(self):
        self.wait_ele_exists(Loc.input_pwd_loc, "登录页_等待 提示语 请输入密码 元素存在")
        status = self.get_text(Loc.input_pwd_loc, img_desc="登录页_提示语 请输入密码")
        return status

    # 获取手机号为空的提示语
    def get_wrong_msg(self):
        self.wait_ele_visible(Loc.wrong_user_pwd_loc, "登录页_等待 提示语 账号不存在或密码错误 元素可见")
        status = self.get_text(Loc.wrong_user_pwd_loc, img_desc="登录页_提示语 账号不存在或密码错误")
        return status

    # 点击我知道了
    def click_i_know(self):
        self.wait_ele_visible(Loc.i_know_loc, "登录页_等待 提示语 我知道了 元素可见")
        self.click_element(Loc.i_know_loc, img_desc="登录页_提示语 我知道了")

# if __name__ == '__main__':
#     lg = LoginPage(BasePage)
#     lg.login_action('13072721092', '123456')
#     uninstall_appium_settings()
#     uninstall_uiautomator2()
