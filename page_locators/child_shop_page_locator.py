# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/5

E-mail:keen2020@outlook.com

=================================


"""

from appium.webdriver.common.mobileby import MobileBy


class ChildShopPageLocator(object):

    # 点击 我的
    my_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_tab_icon"

    # 点击设置
    set_loc = (MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId('com.cashier.jiutongshanghu:id/tv_setting')")

    # 点击 退出登录
    logout_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_loginout"

    # 点击确定   取消-->   com.cashier.jiutongshanghu:id/dialog_normal_leftbtn

    # 确定按钮
    yes_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/dialog_normal_rightbtn"

    # 门店管理
    # shop_manage_loc = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().text('门店管理')"
    shop_manage_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_me_mendian"

    # 添加门店
    add_shop_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_add_store"

    # 请输入门店名称
    shop_name_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_add_store_name"

    # 请输入门店地址
    shop_address_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_add_store_address"

    # 联系人输入框
    people_name_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_add_store_people"

    # 联系电话输入框
    phone_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_add_store_phone"

    # 联系邮箱输入框
    email_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_add_store_email"

    # 下一步按钮
    next_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_store_next"

    # 门店登录密码输入框
    pwd_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/edit_password"

    # 确定按钮
    sure_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/yes"

    # 完成按钮
    finish_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_finish"

    # 选择门店,目前只能定位className,然后通过下标
    shop_name_loc = MobileBy.CLASS_NAME, "android.widget.RelativeLayout"

    # 重置门店密码按钮
    edit_login_pwd_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_reset_password"




