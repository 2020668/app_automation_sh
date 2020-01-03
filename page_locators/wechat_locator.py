# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/19

E-mail:keen2020@outlook.com

=================================


"""

from appium.webdriver.common.mobileby import MobileBy


class WechatLocator(object):

    # 密码输入框
    pwd_input_loc = MobileBy.ID, "com.tencent.mm:id/m6"

    # 登录按钮
    login_button_loc = MobileBy.ID, "com.tencent.mm:id/d0q"

    # 点击 + 号
    add_button_loc = MobileBy.ID, "com.tencent.mm:id/ra"

    # 点击 扫一扫按钮
    scan_loc = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().text('扫一扫')"

    # 点击屏幕右上方的更多按钮
    more_loc = MobileBy.ID, "com.tencent.mm:id/ln"
    # more_loc = MobileBy.CLASS_NAME, "android.widget.ImageButton"

    # 从相册选择二维码
    album_loc = MobileBy.ID, "com.tencent.mm:id/dc"

    # 选取第一张图片
    first_pic_loc = MobileBy.ID, "com.tencent.mm:id/cem"

    # 等待webview出现
    webview_loc = MobileBy.CLASS_NAME, "com.tencent.tbs.core.webkit.WebView"

    # 确认支付按钮
    pay_sure_loc = MobileBy.XPATH, "//button[@class='tijiao']"

    # 使用密码按钮
    use_pwd_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("使用密码")'

    # 支付密码输入框
    pay_pwd_input_loc = MobileBy.CLASS_NAME, "android.widget.RelativeLayout"

    # 完成按钮
    finish_loc = MobileBy.CLASS_NAME, "android.widget.ImageView"

    # 点击页面左上角 X
    close_loc = MobileBy.ID, "com.tencent.mm:id/m0"

    # 点击 我 按钮
    me_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.mm:id/djv").text("我")'

    # 点击 设置 按钮
    setting_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/title").text("设置")'

    # 退出按钮
    out_button_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.mm:id/d8").text("退出")'

    # 退出登录
    logout_button_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.tencent.mm:id/dc").text("退出登录")'

    # 退出按钮
    logout_sure_loc = MobileBy.ID, "com.tencent.mm:id/b47"

    # loc = MobileBy.ID, "com.tencent.mm:id/m0"
