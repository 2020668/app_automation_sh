# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/11/5
E-mail:keen2020@outlook.com
=================================

"""

from appium.webdriver.common.mobileby import MobileBy


class ReportPageLocator(object):

    # 报表按钮
    report_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("报表")'

    # 日报
    report_day_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_day"

    # 日期按钮
    day_time_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_select_time"

    # 选择某一天 滑动

    # 确定按钮
    day_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_confirm"

    # 取消按钮
    day_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_cancel"

    # 周报
    report_week_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_week"

    # 周按钮
    week_time_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_select_time"

    # 选择某一周
    week_name_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_week_item"

    # 前一年按钮
    year_before_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_left"

    # 后一年按钮
    year_after_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_right"

    # 确定按钮
    week_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_sure"

    # 取消按钮
    week_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_cancel"

    # 月报
    report_month_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_month"

    # 月按钮
    month_time_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_select_time"

    # 选择某一月 滑动

    # 确定按钮
    month_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_confirm"

    # 取消按钮
    month_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_cancel"

    # 年报
    report_year_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_year"

    # 年按钮
    year_time_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_select_time"

    # 选择某一年 滑动

    # 确定按钮
    year_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_confirm"

    # 取消按钮
    year_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_cancel"

    # 图形按钮
    graph_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_graph"

    # 列表按钮、
    list_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_list"
