# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

from appium.webdriver.common.mobileby import MobileBy


class WechatLoginPageLocator(object):

    # 微信登录按钮
    wechat_login_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_wechat"

    # 绑定页的标题 账号绑定
    account_binding_title_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/title_tv"

    # 手机号输入框
    phone_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/edit_partner_phone"

    # 获取验证码按钮
    get_code_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/cv_get_countdown"

    # 验证码输入框
    code_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_partner_code"

    # 服务协议按钮
    service_agreement_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_regi_xieyi"

    # 立即绑定按钮
    binding_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_bind"

    # 我的 页的微信快捷登录
    me_wechat_login = MobileBy.ID, 'com.cashier.jiutongshanghu:id/ll_me_wechat'

    # 微信登录绑定状态
    wechat_login_status = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_wechat_status"

    # 微信登录解绑确定按钮
    untying_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/dialog_normal_leftbtn"

    # 微信登录解绑取消按钮
    untying_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/dialog_normal_rightbtn"
