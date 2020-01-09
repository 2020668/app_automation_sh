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
import os
from appium.webdriver.common.mobileby import MobileBy
from decimal import Decimal

from common.basepage import BasePage
from common import logger
from common.image_to_text import BaiduAIP
from common.dir_config import CUSTOM_SIZE_IMG_DIR
from page_locators.orderbook_page_locator import OrderBookPageLocator as Loc


class OrderBookPage(BasePage):

    # 查看账单前五条记录
    def select_first_five_order(self, data, number):

        num = 0

        self.wait_ele_visible(loc=Loc.order_nav_loc, img_desc="账单按钮")
        self.click_element(loc=Loc.order_nav_loc, img_desc="账单按钮")

        while num < number:

            self.wait_ele_visible(loc=Loc.order_list_status_loc, img_desc="账单状态")
            order_list_status = self.get_element_text(loc=Loc.order_list_status_loc, img_desc="账单状态", num=num,
                                                      find_all=True)

            if order_list_status == "支付成功":
                self.wait_ele_visible(loc=Loc.order_list_shop_name_loc, img_desc="账单列表页指定账单的收款门店")
                order_list_shop_name = self.get_element_text(loc=Loc.order_list_shop_name_loc,
                                                             img_desc="账单列表页指定账单的收款门店", num=num, find_all=True)

                self.wait_ele_visible(loc=Loc.order_list_merchant_name_loc, img_desc="账单列表页指定账单的收款人")
                order_list_merchant_name = self.get_element_text(loc=Loc.order_list_merchant_name_loc,
                                                                 img_desc="账单列表页指定账单的收款人", num=num, find_all=True)[5:]

                self.wait_ele_visible(loc=Loc.order_list_time_loc, img_desc="账单列表页指定账单的交易时间")
                order_list_time = self.get_element_text(loc=Loc.order_list_time_loc,
                                                        img_desc="账单列表页指定账单的交易时间", num=num, find_all=True)

                self.wait_ele_visible(loc=Loc.order_list_amount_loc, img_desc="账单列表页指定账单的交易金额")
                order_list_amount = self.get_element_text(loc=Loc.order_list_amount_loc,
                                                          img_desc="账单列表页指定账单的交易金额", num=num, find_all=True)[1:]

                self.get_element(loc=Loc.order_list_status_loc, img_desc="账单状态", find_all=True)[num].click()

                self.wait_ele_visible(loc=Loc.order_detail_amount_loc, img_desc="账单详情页的金额控件")
                order_detail_amount = self.get_text(loc=Loc.order_detail_amount_loc, img_desc="账单详情页的金额控件")

                self.wait_ele_visible(loc=Loc.order_detail_pyment_loc, img_desc="账单详情页的收款方式")
                order_detail_payment = self.get_text(loc=Loc.order_detail_pyment_loc, img_desc="账单详情页的收款方式")

                self.wait_ele_visible(loc=Loc.order_detail_time_loc, img_desc="账单详情页的订单时间")
                order_detail_time = self.get_text(loc=Loc.order_detail_time_loc, img_desc="账单详情页的订单时间")

                self.wait_ele_visible(loc=Loc.order_detail_id_loc, img_desc="账单详情页的订单号")
                order_detail_id = self.get_text(loc=Loc.order_detail_id_loc, img_desc="账单详情页的订单号")

                self.wait_ele_visible(loc=Loc.order_detail_status_loc, img_desc="账单详情页的交易状态")
                order_detail_status = self.get_text(loc=Loc.order_detail_status_loc, img_desc="账单详情页的交易状态")

                self.wait_ele_visible(loc=Loc.order_detail_merchant_name_loc, img_desc="账单详情页的收银员姓名")
                order_detail_merchant_name = self.get_text(loc=Loc.order_detail_merchant_name_loc,
                                                           img_desc="账单详情页的收银员姓名")

                assert order_list_amount == order_detail_amount

                assert order_list_time == order_detail_time

                assert order_detail_status == "支付成功"

                assert order_list_merchant_name == order_detail_merchant_name

                self.wait_ele_visible(loc=Loc.order_note_button_loc, img_desc="账单备注按钮")
                self.click_element(loc=Loc.order_note_button_loc, img_desc="账单备注按钮")

                self.wait_ele_visible(loc=Loc.order_note_input_loc, img_desc="账单备注内容输入框")
                self.clean_element_text(loc=Loc.order_note_input_loc, img_desc="账单备注内容输入框")
                self.input_text(loc=Loc.order_note_input_loc, value=data["note_pay_success"], img_desc="账单备注内容输入框")

                self.wait_ele_visible(loc=Loc.order_note_save_loc, img_desc="账单备注的保存按钮")
                self.click_element(loc=Loc.order_note_save_loc, img_desc="账单备注的保存按钮")
                time.sleep(2)

                # 备注输入后确认
                self.wait_ele_visible(loc=Loc.order_detail_note_loc, img_desc="订单详情页的备注")
                order_detail_note = self.get_text(loc=Loc.order_detail_note_loc, img_desc="账单详情页的备注")

                assert order_detail_note == data["note_pay_success"]

                self.wait_ele_visible(loc=Loc.detail_back_loc, img_desc="账单详情页的返回按钮")
                self.click_element(loc=Loc.detail_back_loc, img_desc="账单详情页的返回按钮")
                time.sleep(1)

            elif order_list_status == "全额退款":

                self.wait_ele_visible(loc=Loc.order_list_shop_name_loc, img_desc="账单列表页指定账单的收款门店")
                order_list_shop_name = self.get_element_text(loc=Loc.order_list_shop_name_loc,
                                                             img_desc="账单列表页指定账单的收款门店", num=num, find_all=True)
                logging.info("账单列表页指定账单的商户名称为-->{}".format(order_list_shop_name))

                self.wait_ele_visible(loc=Loc.order_list_merchant_name_loc, img_desc="账单列表页指定账单的收款人")
                order_list_merchant_name = self.get_element_text(loc=Loc.order_list_merchant_name_loc,
                                                                 img_desc="账单列表页指定账单的收款人", num=num, find_all=True)[5:]
                logging.info("账单列表页指定账单的收款人为-->{}".format(order_list_merchant_name))

                self.wait_ele_visible(loc=Loc.order_list_time_loc, img_desc="账单列表页指定账单的退款时间")
                order_list_time = self.get_element_text(loc=Loc.order_list_time_loc, img_desc="账单列表页指定账单的退款时间",
                                                        num=num, find_all=True)

                self.wait_ele_visible(loc=Loc.order_list_amount_loc, img_desc="账单列表页指定账单的交易金额")
                order_list_amount = self.get_element_text(loc=Loc.order_list_amount_loc,
                                                          img_desc="账单列表页指定账单的交易金额", num=num, find_all=True)[1:]

                self.wait_ele_visible(loc=Loc.order_list_refund_amount_loc, img_desc="账单列表页指定账单的退款金额")
                order_list_refund_amount = self.get_element_text(loc=Loc.order_list_refund_amount_loc,
                                                                 img_desc="账单列表页指定账单的退款金额", num=num, find_all=True)[4:]

                self.get_element(loc=Loc.order_list_status_loc, img_desc="账单状态", find_all=True)[num].click()

                assert order_list_amount == order_list_refund_amount

                self.wait_ele_visible(loc=Loc.order_detail_amount_loc, img_desc="账单详情页的金额控件")
                order_detail_amount = self.get_text(loc=Loc.order_detail_amount_loc, img_desc="账单详情页的金额控件")

                assert order_list_amount == order_detail_amount

                self.wait_ele_visible(loc=Loc.order_detail_pyment_loc, img_desc="账单详情页的收款方式")
                order_detail_payment = self.get_text(loc=Loc.order_detail_pyment_loc, img_desc="账单详情页的收款方式")
                logging.info("账单详情页的收款方式为-->{}".format(order_detail_payment))

                self.wait_ele_visible(loc=Loc.order_detail_time_loc, img_desc="账单详情页的订单时间")
                order_detail_time = self.get_text(loc=Loc.order_detail_time_loc, img_desc="账单详情页的订单时间")
                logging.info("账单详情页的订单时间为-->{}".format(order_detail_time))

                self.wait_ele_visible(loc=Loc.order_detail_id_loc, img_desc="账单详情页的订单号")
                order_detail_id = self.get_text(loc=Loc.order_detail_id_loc, img_desc="账单详情页的订单号")
                logging.info("账单详情页的订单号为-->{}".format(order_detail_id))

                self.wait_ele_visible(loc=Loc.order_detail_status_loc, img_desc="账单详情页的交易状态")
                order_detail_status = self.get_text(loc=Loc.order_detail_status_loc, img_desc="账单详情页的交易状态")
                logging.info("账单详情页的交易状态为-->{}".format(order_detail_status))

                self.wait_ele_visible(loc=Loc.order_detail_merchant_name_loc, img_desc="账单详情页的收银员姓名")
                order_detail_merchant_name = self.get_text(loc=Loc.order_detail_merchant_name_loc,
                                                           img_desc="账单详情页的收银员姓名")
                logging.info("账单详情页的收银员姓名为-->{}".format(order_detail_merchant_name))

                assert order_list_amount == order_detail_amount

                assert order_list_time > order_detail_time

                assert order_detail_status == "全额退款"

                assert order_list_merchant_name == order_detail_merchant_name

                self.wait_ele_visible(loc=Loc.order_note_button_loc, img_desc="账单备注按钮")
                self.click_element(loc=Loc.order_note_button_loc, img_desc="账单备注按钮")

                self.wait_ele_visible(loc=Loc.order_note_input_loc, img_desc="账单备注内容输入框")
                self.clean_element_text(loc=Loc.order_note_input_loc, img_desc="账单备注内容输入框")
                self.input_text(loc=Loc.order_note_input_loc, value=data["note_refund_all"], img_desc="账单备注内容输入框")

                self.wait_ele_visible(loc=Loc.order_note_save_loc, img_desc="账单备注的保存按钮")
                self.click_element(loc=Loc.order_note_save_loc, img_desc="账单备注的保存按钮")
                time.sleep(2)

                # 备注输入后确认
                self.wait_ele_visible(loc=Loc.order_detail_note_loc, img_desc="订单详情页的备注")
                order_detail_note = self.get_text(loc=Loc.order_detail_note_loc, img_desc="账单详情页的备注")

                assert order_detail_note == data["note_refund_all"]

                self.wait_ele_visible(loc=Loc.detail_back_loc, img_desc="账单详情页的返回按钮")
                self.click_element(loc=Loc.detail_back_loc, img_desc="账单详情页的返回按钮")
                time.sleep(1)

            elif order_list_status == "部分退款":

                self.wait_ele_visible(loc=Loc.order_list_shop_name_loc, img_desc="账单列表页指定账单的收款门店")
                order_list_shop_name = self.get_element_text(loc=Loc.order_list_shop_name_loc,
                                                             img_desc="账单列表页指定账单的收款门店", num=num, find_all=True)

                self.wait_ele_visible(loc=Loc.order_list_merchant_name_loc, img_desc="账单列表页指定账单的收款人")
                order_list_merchant_name = self.get_element_text(loc=Loc.order_list_merchant_name_loc,
                                                                 img_desc="账单列表页指定账单的收款人", num=num, find_all=True)[5:]

                self.wait_ele_visible(loc=Loc.order_list_time_loc, img_desc="账单列表页指定账单的退款时间")
                order_list_time = self.get_element_text(loc=Loc.order_list_time_loc,
                                                        img_desc="账单列表页指定账单的退款时间", num=num, find_all=True)

                self.wait_ele_visible(loc=Loc.order_list_amount_loc, img_desc="账单列表页指定账单的交易金额")
                order_list_amount = self.get_element_text(loc=Loc.order_list_amount_loc,
                                                          img_desc="账单列表页指定账单的交易金额", num=num, find_all=True)[1:]

                self.wait_ele_visible(loc=Loc.order_list_refund_amount_loc, img_desc="账单列表页指定账单的退款金额")
                order_list_refund_amount = self.get_element_text(loc=Loc.order_list_refund_amount_loc,
                                                                 img_desc="账单列表页指定账单的退款金额", num=num, find_all=True)[4:]

                self.get_element(loc=Loc.order_list_status_loc, img_desc="账单状态", find_all=True)[num].click()

                assert order_list_amount > order_list_refund_amount

                self.wait_ele_visible(loc=Loc.order_detail_amount_loc, img_desc="账单详情页的金额控件")
                order_detail_amount = self.get_text(loc=Loc.order_detail_amount_loc, img_desc="账单详情页的金额控件")

                assert order_list_amount == order_detail_amount

                self.wait_ele_visible(loc=Loc.order_detail_pyment_loc, img_desc="账单详情页的收款方式")
                order_detail_payment = self.get_text(loc=Loc.order_detail_pyment_loc, img_desc="账单详情页的收款方式")
                logging.info("账单详情页的收款方式为-->{}".format(order_detail_payment))

                self.wait_ele_visible(loc=Loc.order_detail_time_loc, img_desc="账单详情页的订单时间")
                order_detail_time = self.get_text(loc=Loc.order_detail_time_loc, img_desc="账单详情页的订单时间")
                logging.info("账单详情页的订单时间为-->{}".format(order_detail_time))

                self.wait_ele_visible(loc=Loc.order_detail_id_loc, img_desc="账单详情页的订单号")
                order_detail_id = self.get_text(loc=Loc.order_detail_id_loc, img_desc="账单详情页的订单号")
                logging.info("账单详情页的订单号为-->{}".format(order_detail_id))

                self.wait_ele_visible(loc=Loc.order_detail_status_loc, img_desc="账单详情页的交易状态")
                order_detail_status = self.get_text(loc=Loc.order_detail_status_loc, img_desc="账单详情页的交易状态")
                logging.info("账单详情页的交易状态为-->{}".format(order_detail_status))

                self.wait_ele_visible(loc=Loc.order_detail_merchant_name_loc, img_desc="账单详情页的收银员姓名")
                order_detail_merchant_name = self.get_text(loc=Loc.order_detail_merchant_name_loc,
                                                           img_desc="账单详情页的收银员姓名")
                logging.info("账单详情页的收银员姓名为-->{}".format(order_detail_merchant_name))

                assert order_list_amount == order_detail_amount

                assert order_list_time > order_detail_time

                assert order_detail_status == "部分退款"

                assert order_list_merchant_name == order_detail_merchant_name

                self.wait_ele_visible(loc=Loc.order_note_button_loc, img_desc="账单备注按钮")
                self.click_element(loc=Loc.order_note_button_loc, img_desc="账单备注按钮")

                self.wait_ele_visible(loc=Loc.order_note_input_loc, img_desc="账单备注内容输入框")
                self.clean_element_text(loc=Loc.order_note_input_loc, img_desc="账单备注内容输入框")
                self.input_text(loc=Loc.order_note_input_loc, value=data["note_refund_part"], img_desc="账单备注内容输入框")

                self.wait_ele_visible(loc=Loc.order_note_save_loc, img_desc="账单备注的保存按钮")
                self.click_element(loc=Loc.order_note_save_loc, img_desc="账单备注的保存按钮")
                time.sleep(2)

                # 备注输入后确认
                self.wait_ele_visible(loc=Loc.order_detail_note_loc, img_desc="订单详情页的备注")
                order_detail_note = self.get_text(loc=Loc.order_detail_note_loc, img_desc="账单详情页的备注")

                assert order_detail_note == data["note_refund_part"]

                self.wait_ele_visible(loc=Loc.detail_back_loc, img_desc="账单详情页的返回按钮")
                self.click_element(loc=Loc.detail_back_loc, img_desc="账单详情页的返回按钮")
                time.sleep(1)

            else:
                pass

            num += 1

    # 支付成功的订单查看并添加备注
    def select_pay_success_order(self, note):

        self.wait_ele_visible(loc=Loc.order_nav_loc, img_desc="账单按钮")
        self.click_element(loc=Loc.order_nav_loc, img_desc="账单按钮")

        # amount_list = self.swipe_until_element_click(loc=Loc.pay_success_loc, img_desc="支付成功的订单")[1:]
        # 滑动直到出现支付成功的订单
        self.swipe_until_element_visible(loc=Loc.pay_success_loc, img_desc="支付成功的订单")

        self.wait_ele_visible(loc=Loc.order_list_shop_name_loc, img_desc="账单列表页指定账单的收款门店")
        order_list_shop_name = self.get_text(loc=Loc.order_list_shop_name_loc, img_desc="账单列表页指定账单的收款门店")
        logging.info("账单列表页指定账单的收款门店为-->{}".format(order_list_shop_name))

        self.wait_ele_visible(loc=Loc.order_list_merchant_name_loc, img_desc="账单列表页指定账单的收款人")
        order_list_merchant_name = self.get_text(loc=Loc.order_list_merchant_name_loc, img_desc="账单列表页指定账单的收款人")[5:]
        logging.info("账单列表页指定账单的收款人为-->{}".format(order_list_merchant_name))

        self.wait_ele_visible(loc=Loc.order_list_time_loc, img_desc="账单列表页指定账单的交易时间")
        order_list_time = self.get_text(loc=Loc.order_list_time_loc, img_desc="账单列表页指定账单的交易时间")
        logging.info("账单列表页指定账单的交易时间为-->{}".format(order_list_time))

        self.wait_ele_visible(loc=Loc.order_list_amount_loc, img_desc="账单列表页指定账单的交易金额")
        order_list_amount = self.get_text(loc=Loc.order_list_amount_loc, img_desc="账单列表页指定账单的交易金额")[1:]
        logging.info("账单列表页指定账单的交易金额为-->{}".format(order_list_amount))

        self.click_element(loc=Loc.pay_success_loc, img_desc="支付成功的订单")

        self.wait_ele_visible(loc=Loc.order_detail_amount_loc, img_desc="账单详情页的金额控件")
        order_detail_amount = self.get_text(loc=Loc.order_detail_amount_loc, img_desc="账单详情页的金额控件")
        logging.info("当前选中的账单在账单详情页的交易金额显示为-->{}".format(order_detail_amount))

        self.wait_ele_visible(loc=Loc.order_detail_pyment_loc, img_desc="账单详情页的收款方式")
        order_detail_payment = self.get_text(loc=Loc.order_detail_pyment_loc, img_desc="账单详情页的收款方式")
        logging.info("账单详情页的收款方式为-->{}".format(order_detail_payment))

        self.wait_ele_visible(loc=Loc.order_detail_time_loc, img_desc="账单详情页的订单时间")
        order_detail_time = self.get_text(loc=Loc.order_detail_time_loc, img_desc="账单详情页的订单时间")
        logging.info("账单详情页的订单时间为-->{}".format(order_detail_time))

        self.wait_ele_visible(loc=Loc.order_detail_id_loc, img_desc="账单详情页的订单号")
        order_detail_id = self.get_text(loc=Loc.order_detail_id_loc, img_desc="账单详情页的订单号")
        logging.info("账单详情页的订单号为-->{}".format(order_detail_id))

        self.wait_ele_visible(loc=Loc.order_detail_status_loc, img_desc="账单详情页的交易状态")
        order_detail_status = self.get_text(loc=Loc.order_detail_status_loc, img_desc="账单详情页的交易状态")
        logging.info("账单详情页的交易状态为-->{}".format(order_detail_status))

        self.wait_ele_visible(loc=Loc.order_detail_merchant_name_loc, img_desc="账单详情页的收银员姓名")
        order_detail_merchant_name = self.get_text(loc=Loc.order_detail_merchant_name_loc, img_desc="账单详情页的收银员姓名")
        logging.info("账单详情页的收银员姓名为-->{}".format(order_detail_merchant_name))

        # 备注内容,使用此方法请确保目标账单有备注,否则会报错
        # try:
        #     self.wait_ele_visible(loc=Loc.order_detail_note_loc, img_desc="账单详情页的备注")
        #     order_detail_note = self.get_text(loc=Loc.order_detail_note_loc, img_desc="账单详情页的备注")
        #     logging.info("账单详情页的备注为 {}".format(order_detail_note))
        # except:
        #     logging.info("未找到该笔订单的备注信息,请确定该笔订单是否存在备注")

        # assert order_list_amount == order_detail_amount
        #
        # assert order_list_time == order_detail_time
        #
        # assert order_detail_status == "支付成功"
        #
        # assert order_list_merchant_name == order_detail_merchant_name

        self.wait_ele_visible(loc=Loc.order_note_button_loc, img_desc="账单备注按钮")
        self.click_element(loc=Loc.order_note_button_loc, img_desc="账单备注按钮")

        self.wait_ele_visible(loc=Loc.order_note_input_loc, img_desc="账单备注内容输入框")
        self.clean_element_text(loc=Loc.order_note_input_loc, img_desc="账单备注内容输入框")
        self.input_text(loc=Loc.order_note_input_loc, value=note, img_desc="账单备注内容输入框")

        self.wait_ele_visible(loc=Loc.order_note_save_loc, img_desc="账单备注的保存按钮")
        self.click_element(loc=Loc.order_note_save_loc, img_desc="账单备注的保存按钮")
        time.sleep(2)

        # 备注输入后确认
        self.wait_ele_visible(loc=Loc.order_detail_note_loc, img_desc="订单详情页的备注")
        order_detail_note = self.get_text(loc=Loc.order_detail_note_loc, img_desc="账单详情页的备注")

        assert order_detail_note == note

        self.wait_ele_visible(loc=Loc.detail_back_loc, img_desc="账单详情页的返回按钮")
        self.click_element(loc=Loc.detail_back_loc, img_desc="账单详情页的返回按钮")
        time.sleep(1)

        return self

    # 全额退款的账单查看并添加备注,调用此方法需账单的第一条记录为全额退款的账单
    def select_refund_all_order(self, note):

        self.wait_ele_visible(loc=Loc.order_nav_loc, img_desc="账单按钮")
        self.click_element(loc=Loc.order_nav_loc, img_desc="账单按钮")

        # amount_list = self.swipe_until_element_click(loc=Loc.pay_success_loc, img_desc="支付成功的订单")[1:]
        # 滑动直到出现支付成功的订单
        self.swipe_until_element_visible(loc=Loc.refund_all_loc, img_desc="全额退款的订单")

        self.wait_ele_visible(loc=Loc.order_list_shop_name_loc, img_desc="账单列表页指定账单的收款门店")
        order_list_shop_name = self.get_text(loc=Loc.order_list_shop_name_loc, img_desc="账单列表页指定账单的收款门店")
        logging.info("账单列表页指定账单的收款门店为-->{}".format(order_list_shop_name))

        self.wait_ele_visible(loc=Loc.order_list_merchant_name_loc, img_desc="账单列表页指定账单的收款人")
        order_list_merchant_name = self.get_text(loc=Loc.order_list_merchant_name_loc, img_desc="账单列表页指定账单的收款人")[5:]
        logging.info("账单列表页指定账单的收款人为-->{}".format(order_list_merchant_name))

        self.wait_ele_visible(loc=Loc.order_list_time_loc, img_desc="账单列表页指定账单的交易时间")
        order_list_time = self.get_text(loc=Loc.order_list_time_loc, img_desc="账单列表页指定账单的交易时间")
        logging.info("账单列表页指定账单的交易时间为-->{}".format(order_list_time))

        self.wait_ele_visible(loc=Loc.order_list_amount_loc, img_desc="账单列表页指定账单的交易金额")
        order_list_amount = self.get_text(loc=Loc.order_list_amount_loc, img_desc="账单列表页指定账单的交易金额")[1:]
        logging.info("账单列表页指定账单的交易金额为-->{}".format(order_list_amount))

        self.wait_ele_visible(loc=Loc.order_list_refund_amount_loc, img_desc="账单列表页指定账单的退款金额")
        order_list_refund_amount = self.get_text(loc=Loc.order_list_refund_amount_loc, img_desc="账单列表页指定账单的退款金额")[4:]
        logging.info("账单列表页指定账单的退款金额为-->{}".format(order_list_refund_amount))

        self.click_element(loc=Loc.refund_all_loc, img_desc="全额退款的订单")

        assert order_list_amount == order_list_refund_amount

        self.wait_ele_visible(loc=Loc.order_detail_amount_loc, img_desc="账单详情页的金额控件")
        order_detail_amount = self.get_text(loc=Loc.order_detail_amount_loc, img_desc="账单详情页的金额控件")
        logging.info("当前选中的账单在账单详情页的交易金额显示为-->{}".format(order_detail_amount))

        assert order_list_amount == order_detail_amount

        self.wait_ele_visible(loc=Loc.order_detail_pyment_loc, img_desc="账单详情页的收款方式")
        order_detail_payment = self.get_text(loc=Loc.order_detail_pyment_loc, img_desc="账单详情页的收款方式")
        logging.info("账单详情页的收款方式为-->{}".format(order_detail_payment))

        self.wait_ele_visible(loc=Loc.order_detail_time_loc, img_desc="账单详情页的订单时间")
        order_detail_time = self.get_text(loc=Loc.order_detail_time_loc, img_desc="账单详情页的订单时间")
        logging.info("账单详情页的订单时间为-->{}".format(order_detail_time))

        self.wait_ele_visible(loc=Loc.order_detail_id_loc, img_desc="账单详情页的订单号")
        order_detail_id = self.get_text(loc=Loc.order_detail_id_loc, img_desc="账单详情页的订单号")
        logging.info("账单详情页的订单号为-->{}".format(order_detail_id))

        self.wait_ele_visible(loc=Loc.order_detail_status_loc, img_desc="账单详情页的交易状态")
        order_detail_status = self.get_text(loc=Loc.order_detail_status_loc, img_desc="账单详情页的交易状态")
        logging.info("账单详情页的交易状态为-->{}".format(order_detail_status))

        assert order_detail_status == "全额退款"

        self.wait_ele_visible(loc=Loc.order_detail_merchant_name_loc, img_desc="账单详情页的收银员姓名")
        order_detail_merchant_name = self.get_text(loc=Loc.order_detail_merchant_name_loc, img_desc="账单详情页的收银员姓名")
        logging.info("账单详情页的收银员姓名为-->{}".format(order_detail_merchant_name))

        # 备注内容,使用此方法请确保目标账单有备注,否则会报错
        # try:
        #     self.wait_ele_visible(loc=Loc.order_detail_note_loc, img_desc="账单详情页的备注")
        #     order_detail_note = self.get_text(loc=Loc.order_detail_note_loc, img_desc="账单详情页的备注")
        #     logging.info("账单详情页的备注为 {}".format(order_detail_note))
        # except:
        #     logging.info("未找到该笔订单的备注信息,请确定该笔订单是否存在备注")

        # assert order_list_amount == order_detail_amount
        #
        # assert order_list_time == order_detail_time
        #
        # assert order_detail_status == "支付成功"
        #
        # assert order_list_merchant_name == order_detail_merchant_name

        self.wait_ele_visible(loc=Loc.order_note_button_loc, img_desc="账单备注按钮")
        self.click_element(loc=Loc.order_note_button_loc, img_desc="账单备注按钮")

        self.wait_ele_visible(loc=Loc.order_note_input_loc, img_desc="账单备注内容输入框")
        self.clean_element_text(loc=Loc.order_note_input_loc, img_desc="账单备注内容输入框")
        self.input_text(loc=Loc.order_note_input_loc, value=note, img_desc="账单备注内容输入框")

        self.wait_ele_visible(loc=Loc.order_note_save_loc, img_desc="账单备注的保存按钮")
        self.click_element(loc=Loc.order_note_save_loc, img_desc="账单备注的保存按钮")
        time.sleep(2)

        # 备注输入后确认
        self.wait_ele_visible(loc=Loc.order_detail_note_loc, img_desc="订单详情页的备注")
        order_detail_note = self.get_text(loc=Loc.order_detail_note_loc, img_desc="账单详情页的备注")

        assert order_detail_note == note

        self.wait_ele_visible(loc=Loc.detail_back_loc, img_desc="账单详情页的返回按钮")
        self.click_element(loc=Loc.detail_back_loc, img_desc="账单详情页的返回按钮")
        time.sleep(1)

        return self

    # 部分退款的订单查看并添加备注
    def select_refund_part_order(self, note):

        amount_list = self.swipe_until_element_click(loc=Loc.refund_part_loc, img_desc="部分退款的订单")[1:]
        logging.info("当前选中的订单在订单列表页的交易金额显示为 {}".format(amount_list))

        self.wait_ele_visible(loc=Loc.order_detail_amount_loc, img_desc="订单详情页的金额控件")
        amount_detail = self.get_text(loc=Loc.order_detail_amount_loc, img_desc="订单详情页的金额控件")
        logging.info("当前选中的订单在订单详情页的交易金额显示为 {}".format(amount_detail))

        assert amount_list == amount_detail

        self.wait_ele_visible(loc=Loc.order_note_button_loc, img_desc="订单备注按钮")
        self.click_element(loc=Loc.order_note_button_loc, img_desc="订单备注按钮")

        self.wait_ele_visible(loc=Loc.order_note_input_loc, img_desc="订单备注内容输入框")
        self.input_text(loc=Loc.order_note_input_loc, value=note, img_desc="订单备注内容输入框")

        self.wait_ele_visible(loc=Loc.order_note_save_loc, img_desc="订单备注的保存按钮")
        self.click_element(loc=Loc.order_note_save_loc, img_desc="订单备注的保存按钮")
        time.sleep(2)

        self.wait_ele_visible(loc=Loc.detail_back_loc, img_desc="订单详情页的返回按钮")
        self.click_element(loc=Loc.detail_back_loc, img_desc="订单详情页的返回按钮")
        time.sleep(1)

        return self

    # 账单筛选
    def screen_order(self, login_phone, login_pwd, main_store_name, store_name, store_id, time_desc,
                     time_start, time_end, terminal_type, terminal_name, terminal_id, type_source, status):

        store_name_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'.format(store_name)
        terminal_name_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'.format(terminal_name)

        self.wait_ele_visible(loc=Loc.order_nav_loc, img_desc="账单按钮")
        self.click_element(loc=Loc.order_nav_loc, img_desc="账单按钮")

        self.wait_ele_visible(loc=Loc.screen_loc, img_desc="筛选按钮")
        self.click_element(loc=Loc.screen_loc, img_desc="筛选按钮")

# ================================= C H O I C E     T I M E =================================

        # 快速选择时间区域 本月 近7天 近24小时
        if time_desc:
            time_desc_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'.format(time_desc)
            self.wait_ele_visible(loc=time_desc_loc, img_desc="时间描述-->{}".format(time_desc))
            self.click_element(loc=time_desc_loc, img_desc="时间描述-->{}".format(time_desc))

        # 自定义开始时间和结束时间
        if time_start:
            self.wait_ele_visible(loc=Loc.start_time_loc, img_desc="开始时间")
            self.click_element(loc=Loc.start_time_loc, img_desc="开始时间")

            self.select_datetime(datetime=time_start)

            self.wait_ele_visible(loc=Loc.time_confirm_loc, img_desc="选择时间确定按钮")
            self.click_element(loc=Loc.time_confirm_loc, img_desc="选择时间确定按钮")

        if time_end:
            self.wait_ele_visible(loc=Loc.end_time_loc, img_desc="结束时间")
            self.click_element(loc=Loc.end_time_loc, img_desc="结束时间")

            self.select_datetime(datetime=time_end)

            self.wait_ele_visible(loc=Loc.time_confirm_loc, img_desc="选择时间确定按钮")
            self.click_element(loc=Loc.time_confirm_loc, img_desc="选择时间确定按钮")

        # 获取滑动选择的开始时间和结束时间 包括选择的固定时间后自动写入的时间
        self.wait_ele_visible(loc=Loc.start_time_loc, img_desc="开始时间")
        api_time_start = self.get_text(loc=Loc.start_time_loc, img_desc="开始时间")

        self.wait_ele_visible(loc=Loc.end_time_loc, img_desc="结束时间")
        api_time_end = self.get_text(loc=Loc.end_time_loc, img_desc="结束时间")


# ================================= C H O I C E     S T O R E =================================

        if store_name:
            if store_name != "全部门店":

                # 选择门店
                self.wait_ele_visible(loc=Loc.store_choose_loc, img_desc="选择门店按钮")
                self.click_element(loc=Loc.store_choose_loc, img_desc="选择门店按钮")

                self.wait_ele_visible(loc=Loc.all_store_name_loc, img_desc="所有门店按钮")
                self.click_element(loc=Loc.all_store_name_loc, img_desc="所有门店按钮")

                self.wait_ele_visible(loc=store_name_loc, img_desc="门店->{}".format(store_name))
                self.click_element(loc=store_name_loc, img_desc="门店->{}".format(store_name))

                self.wait_ele_visible(loc=Loc.store_confirm_loc, img_desc="选择门店后的确定按钮")
                self.click_element(loc=Loc.store_confirm_loc, img_desc="选择门店后的确定按钮")
            else:
                pass
        else:
            pass

# ================================= C H O I C E     T E R M I N A L =================================

        if terminal_name:

            self.wait_ele_visible(loc=Loc.terminal_loc, img_desc="全部终端 按钮")
            self.click_element(loc=Loc.terminal_loc, img_desc="全部终端 按钮")

            self.wait_ele_visible(loc=terminal_name_loc, img_desc="终端-->{}".format(terminal_name))
            self.click_element(loc=terminal_name_loc, img_desc="终端-->{}".format(terminal_name))

            self.wait_ele_visible(loc=Loc.terminal_confirm_loc, img_desc="选择终端后的确定按钮")
            self.click_element(loc=Loc.terminal_confirm_loc, img_desc="选择终端后的确定按钮")
        else:
            pass

# ================================= C H O I C E     P A Y M E N T =================================

        if type_source == "全部":
            self.wait_ele_visible(loc=Loc.payment_method_all_loc, img_desc="支付方式 全部 按钮")
            self.click_element(loc=Loc.payment_method_all_loc, img_desc="支付方式 全部 按钮")
        elif type_source == "微信":
            self.wait_ele_visible(loc=Loc.payment_method_wechat_loc, img_desc="支付方式 微信 按钮")
            self.click_element(loc=Loc.payment_method_wechat_loc, img_desc="支付方式 微信 按钮")
        elif type_source == "支付宝":
            self.wait_ele_visible(loc=Loc.payment_method_alipay_loc, img_desc="支付方式 支付宝 按钮")
            self.click_element(loc=Loc.payment_method_alipay_loc, img_desc="支付方式 支付宝 按钮")
        elif type_source == "刷卡":
            self.wait_ele_visible(loc=Loc.payment_method_pos_loc, img_desc="支付方式 刷卡 按钮")
            self.click_element(loc=Loc.payment_method_pos_loc, img_desc="支付方式 刷卡 按钮")
        elif type_source == "预授权":
            self.wait_ele_visible(loc=Loc.payment_method_auth_loc, img_desc="支付方式 预授权 按钮")
            self.click_element(loc=Loc.payment_method_auth_loc, img_desc="支付方式 预授权 按钮")
        elif type_source == "其他":
            self.wait_ele_visible(loc=Loc.payment_method_other_loc, img_desc="支付方式 其他 按钮")
            self.click_element(loc=Loc.payment_method_other_loc, img_desc="支付方式 其他 按钮")
        else:
            pass

# ================================= C H O I C E     S T A T U S =================================

        if status == "全部订单":
            self.wait_ele_visible(loc=Loc.status_all_loc, img_desc="支付状态 全部订单 按钮")
            self.click_element(loc=Loc.status_all_loc, img_desc="支付状态 全部订单 按钮")
        elif status == "支付成功":
            self.wait_ele_visible(loc=Loc.status_success_loc, img_desc="支付状态 收款成功 按钮")
            self.click_element(loc=Loc.status_success_loc, img_desc="支付状态 收款成功 按钮")
        elif status == "退款成功":
            self.wait_ele_visible(loc=Loc.status_refund_loc, img_desc="支付状态 退款成功 按钮")
            self.click_element(loc=Loc.status_refund_loc, img_desc="支付状态 退款成功 按钮")

        self.wait_ele_visible(loc=Loc.confirm_loc, img_desc="筛选界面的确定按钮")
        self.click_element(loc=Loc.confirm_loc, img_desc="筛选界面的确定按钮")

        time.sleep(2)

# ================================= G E T     S C R E E N  R E S U L T =================================

        self.wait_ele_visible(loc=Loc.screen_result_start_end_time, img_desc="筛选结果中的起始时间")
        screen_result_start_end_time = self.get_text(loc=Loc.screen_result_start_end_time, img_desc="筛选结果中的起始时间")
        screen_result_start_time = screen_result_start_end_time[:16]
        logging.info("筛选结果中的开始时间为-->{}".format(screen_result_start_time))
        screen_result_end_time = screen_result_start_end_time[19:35]
        logging.info("筛选结果中的结束时间为-->{}".format(screen_result_end_time))

        self.wait_ele_visible(loc=Loc.screen_result_store_name_loc, img_desc="筛选结果中的门店名称")
        screen_result_store_name = self.get_text(loc=Loc.screen_result_store_name_loc, img_desc="筛选结果中的门店名称")

        self.wait_ele_visible(loc=Loc.screen_result_payment_loc, img_desc="筛选结果中的支付方式")
        screen_result_payment = self.get_text(loc=Loc.screen_result_payment_loc, img_desc="筛选结果中的支付方式")

        self.wait_ele_visible(loc=Loc.screen_result_success_num_loc, img_desc="筛选结果中的收款笔数")
        screen_result_success_num = self.get_text(loc=Loc.screen_result_success_num_loc, img_desc="筛选结果中的收款笔数")

        self.wait_ele_visible(loc=Loc.screen_result_refund_num_loc, img_desc="筛选结果中的退款笔数")
        screen_result_refund_num = self.get_text(loc=Loc.screen_result_refund_num_loc, img_desc="筛选结果中的退款笔数")

        self.wait_ele_visible(loc=Loc.screen_result_terminal_loc, img_desc="筛选结果中的收银终端")
        screen_result_terminal = self.get_text(loc=Loc.screen_result_terminal_loc, img_desc="筛选结果中的收银终端")

        self.wait_ele_visible(loc=Loc.screen_result_status_loc, img_desc="筛选结果中的支付状态")
        screen_result_status = self.get_text(loc=Loc.screen_result_status_loc, img_desc="筛选结果中的支付状态")

        self.wait_ele_visible(loc=Loc.screen_result_success_amount_loc, img_desc="筛选结果中的收款金额")
        screen_result_success_amount = self.get_text(loc=Loc.screen_result_success_amount_loc, img_desc="筛选结果中的收款金额")

        self.wait_ele_visible(loc=Loc.screen_result_refund_amount_loc, img_desc="筛选结果中的退款金额")
        screen_result_refund_amount = self.get_text(loc=Loc.screen_result_refund_amount_loc, img_desc="筛选结果中的退款金额")

# ================================= G E T    A P I    D A T A =================================

        # 转换支付方式 供接口调用
        if type_source == "全部":
            api_type_source = ""
        elif type_source == "微信":
            api_type_source = "weixin"
        elif type_source == "支付宝":
            api_type_source = "alipay"
        elif type_source == "刷卡":
            api_type_source = "pos"
        elif type_source == "预授权":
            api_type_source = "auth"
        elif type_source == "其他":
            # 筛选条件是 其他 筛选结果变成了 其它
            type_source = "其它"
            api_type_source = "other"
        else:
            api_type_source = None

        # 转换支付状态 供断言和接口调用
        if status == "全部订单":
            status_name = "全部"
            api_status = ""
        elif status == "支付成功":
            status_name = "收款成功"
            api_status = "1"
        else:
            status_name = "退款成功"
            api_status = "3"

        # 处理门店
        if store_name != "全部门店":
            api_store_id = store_id
            api_store_name = "指定门店"
        else:
            api_store_id = ""
            api_store_name = "全部门店"

        # 判断全部和部分设备
        if terminal_name:
            api_terminal_name = "指定终端"
            api_terminal_id = terminal_id
        else:
            api_terminal_name = "全部终端"
            api_terminal_id = ""

        self.wait_ele_visible(loc=Loc.screen_back_loc, img_desc="筛选结果的返回按钮")
        self.click_element(loc=Loc.screen_back_loc, img_desc="筛选结果的返回按钮")

        self.wait_ele_visible(loc=Loc.order_list_back_loc, img_desc="账单列表的返回按钮")
        self.click_element(loc=Loc.order_list_back_loc, img_desc="账单列表的返回按钮")

        # 断言筛选后的起始时间、门店名称、收银终端、支付方式、支付状态 与 测试数据是否一致
        # 筛选之后需要调接口返回的数据 在测试脚本test_那边断言
        assert screen_result_start_time == api_time_start

        assert screen_result_end_time == api_time_end

        # 子门店无需断言门店名称
        if store_name:
            assert screen_result_store_name == api_store_name
        else:
            pass

        assert screen_result_payment == type_source

        assert screen_result_terminal == api_terminal_name

        assert screen_result_status == status_name

        # 在测试类中调用接口 返回接口必须的数据 以及供断言所需的数据
        return {"screen_result_success_num": screen_result_success_num,
                "screen_result_success_amount": screen_result_success_amount,
                "screen_result_refund_num": screen_result_refund_num,
                "screen_result_refund_amount": screen_result_refund_amount,
                "api_status": api_status,
                "api_store_id": api_store_id,
                "api_store_name": api_store_name,
                "api_terminal_id": api_terminal_id,
                "api_terminal_name": api_terminal_name,
                "api_time_start": api_time_start,
                "api_time_end": api_time_end,
                "api_type_source": api_type_source,
                }

    def refund(self, amount=None, pwd="123456", num=1):

        i = 0

        # 点击首页账单按钮
        self.wait_ele_visible(Loc.order_nav_loc, img_desc="首页_账单按钮")
        self.click_element(Loc.order_nav_loc, img_desc="首页_账单按钮")

        while i < num:
            # 点击支付成功的订单
            # self.wait_ele_visible(Loc.pay_success_loc, img_desc="支付成功的订单")
            # self.click_element(Loc.pay_success_loc, img_desc="支付成功的订单")
            self.swipe_until_element_click(loc=Loc.pay_success_loc, img_desc="支付成功的订单")

            self.wait_ele_visible(loc=Loc.order_detail_amount_loc, img_desc="账单详情页的金额")
            if amount:
                pass
            else:
                amount = self.get_text(loc=Loc.order_detail_amount_loc, img_desc="账单详情页的金额")

            # 点击订单详情页的退款按钮
            self.wait_ele_visible(loc=Loc.refund_button_loc, img_desc="账单详情页的退款按钮")
            self.click_element(loc=Loc.refund_button_loc, img_desc="账单详情页的退款按钮")

            if amount:
                # 输入退款金额
                self.wait_ele_visible(loc=Loc.edit_amount_loc, img_desc="退款金额输入框")
                self.input_text(loc=Loc.edit_amount_loc, value=amount, img_desc="输入退款金额")
            else:
                pass

            # 输入支付密码
            self.wait_ele_visible(loc=Loc.edit_pay_password_loc, img_desc="支付密码输入框")
            self.input_text(loc=Loc.edit_pay_password_loc, value=pwd, img_desc="输入支付密码")

            self.wait_ele_visible(loc=Loc.refund_confirm_loc, img_desc="退款确定按钮")
            self.click_element(loc=Loc.refund_confirm_loc, img_desc="退款确定按钮")

            time.sleep(3)

            i += 1
            logging.info("已完成第 {} 次退款, 退款金额 {}".format(i, amount))

        time.sleep(3)

        self.wait_ele_visible(loc=Loc.order_list_back_loc, img_desc="账单列表的返回按钮")
        self.click_element(loc=Loc.order_list_back_loc, img_desc="账单列表的返回按钮")

# ================================= C O M M O N   M E T H O D =================================

    def select_datetime(self, datetime):
        """
        如出现第一个00识别失败,可先滑动一格再来获取值进行判断
        :param datetime:
        :return: None
        """

        time.sleep(1)
        # 分别获取年月日小时分钟并转换成int型
        year = int(datetime[:4])
        month = int(datetime[5:7])
        day = int(datetime[8:10])
        hour = int(datetime[11:13])
        minute = int(datetime[14:16])
        logging.info("滑动输入的时间为-->{}{}{}{}{}".format(year, month, day, hour, minute))

        # 处理year  先截图获取文本 判断 是否滑动
        while True:

            # 对开始时间的年份进行截图
            self.save_img_by_custom_size(start_x=0.02, start_y=0.895, end_x=0.155, end_y=0.92, img_desc="时间的年份")

            time.sleep(2)

            # 获取截图的文本
            api = BaiduAIP()
            text = api.picture_text(os.path.join(CUSTOM_SIZE_IMG_DIR, "时间的年份.png"))
            text = int(text) if text != '' else 1
            logging.info("当前年份是-->{}, 继续滑动...".format(text) if text != year else "年份-->{} 滑动选中OK".format(text))

            if text == year:
                break
            # 判断然后滑动一个单位
            elif text < year:
                self.swipe_diy(start_width=0.1, start_height=0.9, end_width=0.1, end_height=0.87)
            else:
                self.swipe_diy(start_width=0.1, start_height=0.87, end_width=0.1, end_height=0.9)

        # 处理month
        while True:

            self.save_img_by_custom_size(start_x=0.27, start_y=0.895, end_x=0.335, end_y=0.92, img_desc="时间的月份")

            time.sleep(2)

            api = BaiduAIP()
            text = api.picture_text(os.path.join(CUSTOM_SIZE_IMG_DIR, "时间的月份.png"))
            text = int(text) if text != '' else 1
            logging.info("当前的月份是-->{}, 继续滑动...".format(text) if text != month else "月份-->{} 滑动选中OK".format(text))

            if text == month:
                break
            elif text < month:
                delta = month - text if text != '' else 1
                i = 0
                while i < delta:
                    self.swipe_diy(start_width=0.3, start_height=0.9, end_width=0.3, end_height=0.87)
                    i += 1
            else:
                delta = text - month if text != '' else 1
                i = 0
                while i < delta:
                    self.swipe_diy(start_width=0.3, start_height=0.87, end_width=0.3, end_height=0.9)
                    i += 1

        # 处理day
        while True:

            # 单独识别数字存在成功率低的问题 故加上单位截图 然后只取数字部分的文本
            self.save_img_by_custom_size(start_x=0.46, start_y=0.895, end_x=0.528, end_y=0.92, img_desc="时间的日期")

            time.sleep(2)

            api = BaiduAIP()
            text = api.picture_text(os.path.join(CUSTOM_SIZE_IMG_DIR, "时间的日期.png"))
            text = int(text) if text != '' else 1
            logging.info("当前的日期是-->{}, 继续滑动...".format(text) if text != day else "日期-->{} 滑动选中OK".format(text))

            if text == day:
                break

            elif text < day:
                # 防止数字识别失败 返回空字符串 给个默认值1
                delta = day - text if text != '' else 1
                i = 0
                while i < delta:
                    self.swipe_diy(start_width=0.49, start_height=0.9, end_width=0.49, end_height=0.87)
                    i += 1
            else:
                delta = text - day if text != '' else 1
                i = 0
                while i < delta:
                    self.swipe_diy(start_width=0.49, start_height=0.87, end_width=0.49, end_height=0.9)
                    i += 1

        # 处理hour
        while True:

            self.save_img_by_custom_size(start_x=0.652, start_y=0.895, end_x=0.717, end_y=0.923, img_desc="时间的小时")

            time.sleep(2)

            api = BaiduAIP()
            text = api.picture_text(os.path.join(CUSTOM_SIZE_IMG_DIR, "时间的小时.png"))
            text = int(text) if text != '' else 1
            logging.info("当前的小时是-->{}, 继续滑动...".format(text) if text != hour else "小时-->{} 滑动选中OK".format(text))

            if text == hour:
                break
            elif text < hour:
                delta = hour - text if text != '' else 1
                i = 0
                while i < delta:
                    self.swipe_diy(start_width=0.68, start_height=0.9, end_width=0.68, end_height=0.87)
                    i += 1
            else:
                delta = text - hour if text != '' else 1
                i = 0
                while i < delta:
                    self.swipe_diy(start_width=0.68, start_height=0.87, end_width=0.68, end_height=0.9)
                    i += 1

        # 处理minute
        while True:

            self.save_img_by_custom_size(start_x=0.847, start_y=0.895, end_x=0.912, end_y=0.92, img_desc="时间的分钟")

            time.sleep(2)

            # 获取截图的文本
            api = BaiduAIP()
            text = api.picture_text(os.path.join(CUSTOM_SIZE_IMG_DIR, "时间的分钟.png"))
            text = int(text) if text != '' else 1
            logging.info("当前的分钟是-->{}, 继续滑动...".format(text) if text != minute else "分钟-->{} 滑动选中OK".format(text))

            if text == minute:
                break
            elif text < minute:
                delta = minute - text if text != '' else 1
                i = 0
                while i < delta:
                    self.swipe_diy(start_width=0.88, start_height=0.9, end_width=0.88, end_height=0.87)
                    i += 1
            else:
                delta = text - minute if text != '' else 1
                i = 0
                while i < delta:
                    self.swipe_diy(start_width=0.88, start_height=0.87, end_width=0.88, end_height=0.9)
                    i += 1

    # def screen_success_sum(self):
    #
    #     num_success = 0
    #     num_time = 0
    #     flag = True
    #     sum_success_num = 0
    #     sum_success_amount = 0
    #     info_time = ["2018-01-01"]
    #     num_swipe = 0
    #     while flag is True:
    #
    #         try:
    #
    #             logging.info("num_time-->{}".format(num_time))
    #             self.wait_ele_visible(loc=Loc.screen_result_list_time_loc, img_desc="筛选结果中每条数据的时间")
    #             list_time = self.get_element_text(loc=Loc.screen_result_list_time_loc,
    #                                               img_desc="筛选结果中每条数据的时间", num=num_time, find_all=True)
    #
    #             num_time += 1
    #
    #         except:
    #             list_time = "2000-01-01"
    #
    #         try:
    #
    #             logging.info("num的值为-->{}".format(num_success))
    #
    #             self.wait_ele_visible(loc=Loc.screen_result_list_success_amount_loc, img_desc="筛选结果中每条数据的收款金额")
    #             list_success_amount = self.get_element_text(loc=Loc.screen_result_list_success_amount_loc,
    #                                                         img_desc="筛选结果中每条数据的收款金额", num=num_success, find_all=True)
    #
    #             list_success_num = 1
    #             num_success += 1
    #
    #             list_success_amount = float(list_success_amount[1:-1])
    #             list_success_amount = Decimal.from_float(list_success_amount).quantize(Decimal("0.00"))
    #             logging.info("记录中的收款金额为-->{}".format(list_success_amount))
    #
    #             if list_time not in info_time:
    #                 info_time.append(list_time)
    #                 sum_success_num += list_success_num
    #                 sum_success_amount += list_success_amount
    #
    #                 logging.info("收款笔数合计为-->{}".format(sum_success_num))
    #                 logging.info("收款金额合计为-->{}".format(sum_success_amount))
    #
    #             else:
    #                 pass
    #
    #         except:
    #             self.swipe_diy(start_width=0.5, start_height=0.8, end_width=0.5, end_height=0.3)
    #             time.sleep(1)
    #             num_time = 0
    #             num_success = 0
    #             num_swipe += 1
    #             list_success_num = 0
    #             list_success_amount = "+0.00元"
    #
    #         if num_swipe == 7:
    #             flag = False
    #
    #     logging.info(info_time)
    #     logging.info("收款笔数合计为-->{}".format(sum_success_num))
    #     logging.info("收款金额合计为-->{}".format(sum_success_amount))
    #
    # def screen_success_sum1(self):
    #
    #     num_success = 0
    #     num_time = 0
    #     flag = True
    #     sum_success_num = 0
    #     sum_success_amount = 0
    #     info_time = ["2018-01-01"]
    #     num_swipe = 0
    #     while flag is True:
    #
    #         try:
    #
    #             logging.info("num_time-->{}".format(num_time))
    #             self.wait_ele_visible(loc=Loc.screen_result_list_time_loc, img_desc="筛选结果中每条数据的时间")
    #             list_time = self.get_element_text(loc=Loc.screen_result_list_time_loc,
    #                                               img_desc="筛选结果中每条数据的时间", num=num_time, find_all=True)
    #
    #             num_time += 1
    #
    #         except:
    #             list_time = "2000-01-01"
    #
    #         try:
    #
    #             logging.info("num的值为-->{}".format(num_success))
    #
    #             self.wait_ele_visible(loc=Loc.screen_result_list_success_amount_loc, img_desc="筛选结果中每条数据的收款金额")
    #             list_success_amount = self.get_element_text(loc=Loc.screen_result_list_success_amount_loc,
    #                                                         img_desc="筛选结果中每条数据的收款金额", num=num_success, find_all=True)
    #
    #             list_success_num = 1
    #             num_success += 1
    #
    #             list_success_amount = float(list_success_amount[1:-1])
    #             list_success_amount = Decimal.from_float(list_success_amount).quantize(Decimal("0.00"))
    #             logging.info("记录中的收款金额为-->{}".format(list_success_amount))
    #
    #             if list_time not in info_time:
    #                 info_time.append(list_time)
    #                 sum_success_num += list_success_num
    #                 sum_success_amount += list_success_amount
    #
    #                 logging.info("收款笔数合计为-->{}".format(sum_success_num))
    #                 logging.info("收款金额合计为-->{}".format(sum_success_amount))
    #
    #             else:
    #                 pass
    #
    #         except:
    #             self.swipe_diy(start_width=0.5, start_height=0.8, end_width=0.5, end_height=0.3)
    #             time.sleep(1)
    #             num_time = 0
    #             num_success = 0
    #             num_swipe += 1
    #             list_success_num = 0
    #             list_success_amount = "+0.00元"
    #
    #         if num_swipe == 7:
    #             flag = False
    #
    #     logging.info(info_time)
    #     logging.info("收款笔数合计为-->{}".format(sum_success_num))
    #     logging.info("收款金额合计为-->{}".format(sum_success_amount))
    #
    # def screen_refund_sum(self):
    #
    #     num_status = 0
    #     num_refund = 0
    #     num_time = 0
    #     flag = True
    #     sum_refund_num = 0
    #     sum_refund_amount = 0
    #     info_time = ["2018-01-01"]
    #     num_swipe = 0
    #     while flag is True:
    #
    #         try:
    #             self.wait_ele_visible(loc=Loc.screen_result_list_status_loc, img_desc="筛选结果中每条数据的支付状态")
    #             list_status = self.get_element_text(loc=Loc.screen_result_list_status_loc,
    #                                                 img_desc="筛选结果中每条数据的支付状态", num=num_refund, find_all=True)
    #
    #             num_refund += 1
    #
    #         except:
    #             self.swipe_diy(start_width=0.5, start_height=0.8, end_width=0.5, end_height=0.6)
    #             time.sleep(1)
    #             num_refund = 0
    #             num_swipe += 1
    #             list_status = "unknown"
    #
    #         if "退款" in list_status:
    #
    #             try:
    #
    #                 logging.info("num_time-->{}".format(num_time))
    #                 self.wait_ele_visible(loc=Loc.screen_result_list_time_loc, img_desc="筛选结果中每条数据的时间")
    #                 list_time = self.get_element_text(loc=Loc.screen_result_list_time_loc,
    #                                                   img_desc="筛选结果中每条数据的时间", num=num_time, find_all=True)
    #
    #                 num_time += 1
    #
    #             except:
    #                 list_time = "2000-01-01"
    #
    #             try:
    #
    #                 logging.info("num的值为-->{}".format(num_refund))
    #
    #                 self.wait_ele_visible(loc=Loc.screen_result_list_refund_amount_loc, img_desc="筛选结果中每条数据的退款金额")
    #                 list_refund_amount = self.get_element_text(loc=Loc.screen_result_list_refund_amount_loc,
    #                                                            img_desc="筛选结果中每条数据的退款金额", num=num_refund, find_all=True)
    #
    #                 list_refund_num = 1
    #                 num_refund += 1
    #
    #                 list_refund_amount = float(list_refund_amount[4:-1])
    #                 list_refund_amount = Decimal.from_float(list_refund_amount).quantize(Decimal("0.00"))
    #                 logging.info("记录中的退款金额为-->{}".format(list_refund_amount))
    #
    #                 if list_time not in info_time:
    #                     info_time.append(list_time)
    #                     sum_refund_num += list_refund_num
    #                     sum_refund_amount += list_refund_amount
    #
    #                     logging.info("退款笔数合计为-->{}".format(sum_refund_num))
    #                     logging.info("退款金额合计为-->{}".format(sum_refund_amount))
    #
    #                 else:
    #                     pass
    #
    #             except:
    #                 # self.swipe_diy(start_width=0.5, start_height=0.8, end_width=0.5, end_height=0.6)
    #                 # time.sleep(1)
    #                 num_time = 0
    #                 num_refund = 0
    #                 num_swipe += 1
    #                 list_refund_num = 0
    #                 list_refund_amount = "+0.00元"
    #
    #             if num_swipe == 12:
    #                 flag = False
    #
    #     logging.info(info_time)
    #     logging.info("退款笔数合计为-->{}".format(sum_refund_num))
    #     logging.info("退款金额合计为-->{}".format(sum_refund_amount))


