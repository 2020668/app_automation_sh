# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/11/5
E-mail:keen2020@outlook.com
=================================

"""


import time
import logging
from appium.webdriver.common.mobileby import MobileBy
from common.basepage import BasePage
from common import logger
from page_locators.report_page_locator import ReportPageLocator as Loc


class ReportPage(BasePage):

    # 查看订单
    def select_all_report(self, week):

        week_name_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}周")'.format(week)

        self.wait_ele_visible(loc=Loc.report_loc, img_desc="报表按钮")
        self.click_element(loc=Loc.report_loc, img_desc="报表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.day_time_loc, img_desc="日按钮")
        self.click_element(loc=Loc.day_time_loc, img_desc="日按钮")

        self.swipe_diy(start_width=0.2, start_height=0.8, end_width=0.2, end_height=0.9)
        time.sleep(1)

        self.swipe_diy(start_width=0.5, start_height=0.8, end_width=0.5, end_height=0.9)
        time.sleep(1)

        self.swipe_diy(start_width=0.8, start_height=0.8, end_width=0.8, end_height=0.9)
        time.sleep(1)

        self.wait_ele_visible(loc=Loc.day_cancel_loc, img_desc="选择日的 取消 按钮")
        self.click_element(loc=Loc.day_cancel_loc, img_desc="选择日的 取消 按钮")
        time.sleep(2)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.day_time_loc, img_desc="日按钮")
        self.click_element(loc=Loc.day_time_loc, img_desc="日按钮")
        time.sleep(1)

        self.swipe_diy(start_width=0.2, start_height=0.8, end_width=0.2, end_height=0.9)
        time.sleep(1)

        self.swipe_diy(start_width=0.5, start_height=0.8, end_width=0.5, end_height=0.95)
        time.sleep(1)

        self.swipe_diy(start_width=0.8, start_height=0.8, end_width=0.8, end_height=0.95)
        time.sleep(1)

        self.wait_ele_visible(loc=Loc.day_confirm_loc, img_desc="选择日的确定按钮")
        self.click_element(loc=Loc.day_confirm_loc, img_desc="选择日的确定按钮")
        time.sleep(3)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        # =====================================   ^ 初始的日报  =====================================

        self.wait_ele_visible(loc=Loc.report_week_loc, img_desc="周报按钮")
        self.click_element(loc=Loc.report_week_loc, img_desc="周报按钮")
        time.sleep(1)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.week_time_loc, img_desc="周按钮")
        self.click_element(loc=Loc.week_time_loc, img_desc="周按钮")

        time.sleep(3)

        self.swipe_until_element_click_area(loc=week_name_loc, img_desc="选择 {} 周".format(week), start_width=0.5,
                                            start_height=0.85, end_width=0.5, end_height=0.6)

        self.wait_ele_visible(loc=Loc.week_cancel_loc, img_desc="选择周的 取消 按钮")
        self.click_element(loc=Loc.week_cancel_loc, img_desc="选择周的 取消 按钮")
        time.sleep(2)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.week_time_loc, img_desc="周按钮")
        self.click_element(loc=Loc.week_time_loc, img_desc="周按钮")

        self.swipe_until_element_click_area(loc=week_name_loc, img_desc="选择 {} 周".format(week), start_width=0.5,
                                            start_height=0.85, end_width=0.5, end_height=0.6)

        self.wait_ele_visible(loc=Loc.week_confirm_loc, img_desc="选择周的 确定 按钮")
        self.click_element(loc=Loc.week_confirm_loc, img_desc="选择周的 确定 按钮")
        time.sleep(3)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        # =====================================   ^ 周报  =====================================

        self.wait_ele_visible(loc=Loc.report_month_loc, img_desc="月报按钮")
        self.click_element(loc=Loc.report_month_loc, img_desc="月报按钮")
        time.sleep(1)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.month_time_loc, img_desc="月按钮")
        self.click_element(loc=Loc.month_time_loc, img_desc="月按钮")
        time.sleep(1)

        self.swipe_diy(start_width=0.75, start_height=0.7, end_width=0.75, end_height=0.8)
        time.sleep(1)

        self.wait_ele_visible(loc=Loc.month_cancel_loc, img_desc="选择月的取消按钮")
        self.click_element(loc=Loc.month_cancel_loc, img_desc="选择月的取消按钮")
        time.sleep(2)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.month_time_loc, img_desc="月按钮")
        self.click_element(loc=Loc.month_time_loc, img_desc="月按钮")
        time.sleep(1)

        self.swipe_diy(start_width=0.75, start_height=0.7, end_width=0.75, end_height=0.8)
        time.sleep(1)

        self.wait_ele_visible(loc=Loc.month_confirm_loc, img_desc="选择月的确定按钮")
        self.click_element(loc=Loc.month_confirm_loc, img_desc="选择月的确定按钮")
        time.sleep(3)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        # =====================================   ^ 月报  =====================================

        self.wait_ele_visible(loc=Loc.report_year_loc, img_desc="年报按钮")
        self.click_element(loc=Loc.report_year_loc, img_desc="年报按钮")
        time.sleep(1)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.year_time_loc, img_desc="年按钮")
        self.click_element(loc=Loc.year_time_loc, img_desc="年按钮")
        time.sleep(1)

        self.swipe_diy(start_width=0.75, start_height=0.75, end_width=0.75, end_height=0.85)
        time.sleep(1)

        self.wait_ele_visible(loc=Loc.year_cancel_loc, img_desc="选择年的 取消 按钮")
        self.click_element(loc=Loc.year_cancel_loc, img_desc="选择年的 取消 按钮")
        time.sleep(2)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.year_time_loc, img_desc="年按钮")
        self.click_element(loc=Loc.year_time_loc, img_desc="年按钮")
        time.sleep(1)

        self.swipe_diy(start_width=0.75, start_height=0.75, end_width=0.75, end_height=0.85)
        time.sleep(1)

        self.wait_ele_visible(loc=Loc.year_confirm_loc, img_desc="选择年的 确定 按钮")
        self.click_element(loc=Loc.year_confirm_loc, img_desc="选择年的 确定 按钮")
        time.sleep(3)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        # =====================================   ^ 年报  =====================================

        self.wait_ele_visible(loc=Loc.report_day_loc, img_desc="日报表按钮")
        self.click_element(loc=Loc.report_day_loc, img_desc="日报表按钮")
        time.sleep(1)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.day_time_loc, img_desc="日按钮")
        self.click_element(loc=Loc.day_time_loc, img_desc="日按钮")

        self.swipe_diy(start_width=0.2, start_height=0.8, end_width=0.2, end_height=0.9)
        time.sleep(1)

        self.swipe_diy(start_width=0.5, start_height=0.8, end_width=0.5, end_height=0.9)
        time.sleep(1)

        self.swipe_diy(start_width=0.8, start_height=0.8, end_width=0.8, end_height=0.9)
        time.sleep(1)

        self.wait_ele_visible(loc=Loc.day_cancel_loc, img_desc="选择日的 取消 按钮")
        self.click_element(loc=Loc.day_cancel_loc, img_desc="选择日的 取消 按钮")
        time.sleep(2)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.day_time_loc, img_desc="日按钮")
        self.click_element(loc=Loc.day_time_loc, img_desc="日按钮")
        time.sleep(1)

        self.swipe_diy(start_width=0.2, start_height=0.8, end_width=0.2, end_height=0.9)
        time.sleep(1)

        self.swipe_diy(start_width=0.5, start_height=0.8, end_width=0.5, end_height=0.95)
        time.sleep(1)

        self.swipe_diy(start_width=0.8, start_height=0.8, end_width=0.8, end_height=0.95)
        time.sleep(1)

        self.wait_ele_visible(loc=Loc.day_confirm_loc, img_desc="选择日的确定按钮")
        self.click_element(loc=Loc.day_confirm_loc, img_desc="选择日的确定按钮")
        time.sleep(3)

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.list_loc, img_desc="列表按钮")
        self.click_element(loc=Loc.list_loc, img_desc="列表按钮")

        self.swipe_up_down_diy(num=2)

        self.wait_ele_visible(loc=Loc.graph_loc, img_desc="图形按钮")
        self.click_element(loc=Loc.graph_loc, img_desc="图形按钮")

        self.swipe_up_down_diy(num=2)
