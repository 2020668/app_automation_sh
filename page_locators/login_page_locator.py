# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

from appium.webdriver.common.mobileby import MobileBy


class LoginPageLocator(object):

    # 用户名输入框
    user_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ed_login_phone"
    # 密码输入框
    pwd_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ed_login_password"
    # 登录按钮
    login_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_login"
    # 提示语请输入账号
    input_user_loc = MobileBy.XPATH, '//*[contains(@text, "请输入账号")]'
    # 提示语请输入密码
    input_pwd_loc = MobileBy.XPATH, '//*[contains(@text, "请输入密码")]'
    # 提示语 账号不存在或密码错误
    wrong_user_pwd_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_tishi_content"
    # 我知道了
    i_know_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_tishi"
