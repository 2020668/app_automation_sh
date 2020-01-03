# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/11/5
E-mail:keen2020@outlook.com
=================================

"""

from appium.webdriver.common.mobileby import MobileBy


class OrderBookPageLocator(object):
    # 账单按钮
    order_nav_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("账单")'

    # 账单状态
    order_list_status_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_status"

    # 账单列表的支付成功
    pay_success_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("支付成功")'

    # 账单列表的全额退款
    refund_all_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("全额退款")'

    # 账单列表的部分退款
    refund_part_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("部分退款")'

    # 账单列表的支付方式图标
    order_list_payment_img_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_show"

    # 账单列表的日期控件
    order_list_date_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_date"

    # 账单列表的金额控件
    order_list_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_bill"

    # 账单列表的收款门店控件
    order_list_shop_name_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_remark"

    # 账单列表收银员名称控件
    order_list_merchant_name_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_shouyinyuan"

    # 账单列表交易时间控件
    order_list_time_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_time"

    # 账单列表退款金额控件
    order_list_refund_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_refund_bill"

    # 账单详情页的金额控件
    order_detail_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_details_money"

    # 账单详情页的支付方式控件
    order_detail_pyment_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_details_fanghsi"

    # 账单详情页的订单时间控件
    order_detail_time_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_details_time"

    # 账单详情页的订单号控件
    order_detail_id_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_details_dingdan"

    # 账单详情页的支付状态
    order_detail_status_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_details_type"

    # 订单详情页的收银员名称
    order_detail_merchant_name_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_details_name"

    # 订单详情页的订单备注内容
    order_detail_note_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_show_beizhu"

    # 账单备注按钮
    order_note_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/rel_order_note"

    # 账单备注输入框
    order_note_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_order_note"

    # 账单备注的保存按钮
    order_note_save_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_save"

    # 账单列表的返回按钮
    order_list_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 账单详情页的退款按钮
    refund_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_flow_refund"

    # 退款金额输入框
    edit_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/edit_amount"

    # 支付密码输入框  先点击再输入
    edit_pay_password_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/edit_password"

    # 确定按钮
    refund_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/yes"

    # 取消按钮
    refund_no_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/no"

    # 订单详情页的返回按钮
    detail_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_flow_back"

    # 账单列表页的筛选按钮
    screen_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_title_zhangdan"

    # 开始时间按钮
    start_time_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/nct_start_time"

    # 确定按钮
    time_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btnSubmit"

    # 取消按钮
    time_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btnCancel"

    # 结束时间按钮
    end_time_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/nct_end_time"

    # 门店选择按钮
    store_choose_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_store"

    # 具体的门店
    # 全部门店
    all_store_name_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/cb_all_store"

    # 具体名称
    # store_name_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("吉野家")'

    # 确定按钮
    store_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_sure"

    # 终端选择按钮
    terminal_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_equipment"

    # 选择某个终端,所有终端都是相同的id
    terminal_name_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/rel_check"

    # 重置按钮
    terminal_reset_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/nct_terminal_reset"

    # 确定按钮
    terminal_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/nct_terminal_confirm"

    # 支付方式
    # 全部
    payment_method_all_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:' \
                                                           'id/tv_state").text("全部")'

    # 微信
    payment_method_wechat_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.' \
                                                              'jiutongshanghu:id/tv_state").text("微信")'

    # 支付宝
    payment_method_alipay_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:' \
                                                              'id/tv_state").text("支付宝")'

    # 刷卡
    payment_method_pos_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:' \
                                                           'id/tv_state").text("刷卡")'

    # 预授权
    payment_method_auth_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:' \
                                                            'id/tv_state").text("预授权")'

    # 其他
    payment_method_other_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:' \
                                                             'id/tv_state").text("其他")'

    # 支付状态
    # 全部订单
    status_all_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu:' \
                                                   'id/tv_state").text("全部订单")'

    # 收款成功
    status_success_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu' \
                                                       ':id/tv_state").text("收款成功")'

    # 已退款
    status_refund_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.cashier.jiutongshanghu' \
                                                      ':id/tv_state").text("已退款")'

    # 重置按钮
    reset_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/nct_reset"

    # 确定按钮
    confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/nct_confirm"

    # 筛选结果中的起始时间
    screen_result_start_end_time = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_filter_time"

    # 筛选结果中门店名称
    screen_result_store_name_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_mendian_select"\

    # 筛选结果中的支付方式
    screen_result_payment_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_pay_way"

    # 筛选结果中的收款笔数
    screen_result_success_num_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_success_count"

    # 筛选结果中的退款笔数
    screen_result_refund_num_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_refund_count"

    # 筛选结果中的收银终端
    screen_result_terminal_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_receive_people"

    # 筛选结果中的支付状态
    screen_result_status_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_pay_status"

    # 筛选结果中的收款金额
    screen_result_success_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_success_money"

    # 筛选结果中的退款金额
    screen_result_refund_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_refund_money"

    # 筛选结果中每条数据的支付状态
    screen_result_list_status_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_status"

    # 筛选结果中每条数据的收款金额
    screen_result_list_success_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_bill"

    # 筛选结果中每条数据的退款金额
    screen_result_list_refund_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_refund_bill"

    # 筛选结果中每条数据的更新时间
    screen_result_list_time_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_time"

    # 筛选结果页的返回按钮
    screen_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_back"
