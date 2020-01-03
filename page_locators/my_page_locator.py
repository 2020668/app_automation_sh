# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/5

E-mail:keen2020@outlook.com

=================================


"""

from appium.webdriver.common.mobileby import MobileBy


class MyPageLocator(object):

    # 点击 我的
    my_loc = MobileBy.ID, 'com.cashier.jiutongshanghu:id/iv_tab_icon'

    # 点击设置
    set_loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/tv_setting")')

    # 点击 退出登录
    # logout_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/ll_loginout")'
    logout_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_loginout"

    # 点击确定   取消-->   com.cashier.jiutongshanghu:id/dialog_normal_leftbtn
    # yes_loc = MobileBy.ANDROID_UIAUTOMATOR, \
    #       'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/dialog_normal_rightbtn")'

    # 确定按钮
    yes_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/dialog_normal_rightbtn"
