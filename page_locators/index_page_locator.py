# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

from appium.webdriver.common.mobileby import MobileBy


class IndexPageLocator(object):

    # 导航栏  首页、服务、我的  id相同
    my_button_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/' \
                                                  'tv_tab_title").text("我的")'

    home_page_button_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/' \
                                                         'tv_tab_title").text("首页")'

    service_button_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:id/' \
                                                       'tv_tab_title").text("服务")'

    # 扫一扫
    scan_loc = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().text('扫一扫')"
    # 金额输入框
    input_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_show"
    # 确定按钮
    sure_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ib_finish"
    # 付款成功后点击确认按钮
    success_sure_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_succ_chenggong"
    # 付款成功后的返回按钮
    success_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 账单按钮
    order_nav_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("账单")'
    # 账单列表的支付成功
    pay_success_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("支付成功")'
    # 账单详情页的退款按钮
    refund_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_flow_refund"
    # 退款金额输入框
    edit_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/edit_amount"
    # 支付密码输入框  先点击再输入
    edit_pay_password_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/edit_password"
    # 确定按钮
    refund_sure_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/yes"
    # 取消按钮
    refund_no_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/no"

    # 微信扫一扫付款 金额输入框
    wechat_input_amount_loc = MobileBy.XPATH, '//span[@id="amount"]'
    wechat_sure_loc = MobileBy.XPATH, '//input[@type="button"]'

