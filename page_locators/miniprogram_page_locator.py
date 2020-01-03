# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/11/5
E-mail:keen2020@outlook.com
=================================

"""

from appium.webdriver.common.mobileby import MobileBy


class MiniProgramPageLocator(object):

    # 点餐按钮
    order_button_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("点餐")'

    # 乐付零售按钮
    retail_button_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("乐付零售")'

    # 开启点餐按钮
    open_order_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/bt_open_order"

    # 返回按钮
    back_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 今日营收金额
    total_today_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_today_earning"

    # 今日总订单数
    total_today_num_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_today_order"

    # =================================================================================================

    # 营业统计
    order_statistics_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_home_statistics"

    # 今日
    today_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_bill_day"

    # 昨日
    yesterday_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_bill_yesterday"

    # 本月
    this_month_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_bill_month"

    # 选择日期按钮
    screen_day_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_date"

    # 取消按钮
    day_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btnCancel"

    # 确定按钮
    day_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btnSubmit"

    # 指定日期的总营收
    total_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_total_earning"

    # 指定日期的总订单数
    total_num_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_total_num"

    # =================================================================================================

    # 店内订单
    order_list_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_home_order"

    # 返回按钮
    order_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 全部
    order_status_all_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_all"

    # 已下单
    order_status_ordered_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_ordered"

    # 待支付
    order_status_wait_pay_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_unpaid"

    # 已支付
    order_status_paid_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_paid"

    # 已取消
    order_status_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_cancel"

    # 已退款
    order_status_refund_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_refund"

    # 订单状态
    order_list_status_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_order_status"

    # 订单人数
    order_list_people_num_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_order_num"

    # 餐单
    order_list_menu_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_order_menu"

    # 餐位费
    order_list_table_price_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_tab_price"

    # 总价
    order_list_total_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_order_total"

    # 应付
    order_list_pay_amount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_order_pay"

    # 下单时间
    order_list_order_time_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_order_order_time"

    # 支付时间
    order_list_pay_time_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_order_payment_time"

    # 支付描述
    order_list_pay_comment_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_pay_desc"

    # 撤消按钮
    order_undo_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/bt_order_revocation"

    # 确认按钮
    order_confirm_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/bt_order_confirm"

    # 打印小票
    order_print_ticket_loc_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/bt_order_print"

    # 结账
    order_settles_accounts_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/bt_order_pay"

    # =================================================================================================

    # 菜品管理
    menu_manage_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_home_dishes"

    # 返回按钮
    menu_manage_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 上架中
    upper_shelf_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_put_away"

    # 已下架
    lower_shelf_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_sold_out"

    # 菜品类别
    menu_category_name_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_category"

    # 菜品名称
    menu_name_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_name"

    # 菜品价格
    menu_price_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_price"

    # 菜品库存
    menu_stock_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_states"

    # 类别管理
    menu_category_manage_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_category_management"

    # 类别管理的返回按钮
    menu_category_manage_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 类别管理的添加按钮
    menu_category_manage_add_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/rl_tltle_add"

    # 修改按钮
    menu_category_manage_edit_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_edit"

    # 类别修改的类别名称输入框
    menu_category_manage_edit_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/edit_name"

    # 类别修改的取消按钮
    menu_category_manage_edit_cancle_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/no"

    # 类别修改的确定按钮
    menu_category_manage_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/yes"

    # 删除按钮
    menu_category_manage_delete_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_delete"

    # 删除的取消按钮
    menu_category_manage_delete_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/dialog_normal_leftbtn"

    # 类别删除的确定按钮
    menu_category_manage_delete_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/dialog_normal_rightbtn"

    # 添加菜品
    menu_add_dishes_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_add_dishes"

    # 添加菜品的返回按钮
    menu_add_dishes_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 菜品名称输入框
    menu_dishes_name_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_dishes_name"

    # 菜品图片上传
    menu_deshes_img_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/img_dishes"

    # 菜品单价输入框
    menu_dishes_price_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_dishes_price"

    # 菜品类别选择框
    menu_category_name_select_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_select"

    # 类别选择框返回按钮
    menu_category_name_select_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 选择的类别名称
    menu_category_select_name_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("")'

    # 状态管理 上架按钮
    menu_dishes_status_up_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/rb_up"

    # 下架按钮
    menu_dishes_status_down_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/rb_down"

    # 库存开关
    menu_dishes_stock_status_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tb_set_supply"

    # 库存数量输入框
    menu_dishes_stock_num_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_supply_num"

    # 添加菜品取消按钮
    menu_dishes_add_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_cancel"

    # 添加菜品确定按钮
    menu_dishes_add_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_confirm"

    # =================================================================================================

    # 活动管理
    promotion_manage_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_event_settings"

    # 活动管理页返回按钮
    promotion_manage_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 满金额减
    man_jian_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("满金额减")'

    # 首单立减
    shou_dan_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("首单立减")'

    # 活动规则
    promotion_rule_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_menu_action_reduces"

    # 活动状态
    promotion_status_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/iv_status"

    # 适用场景
    promotion_scene_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_scene"

    # 适用菜品
    promotion_dishes_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_menu"

    # 活动开始时间
    promotion_start_time_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_start_time"

    # 活动结束时间
    promotion_end_time_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_end_time"

    # 删除按钮
    promotion_delete_button_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_delete"

    # 添加活动
    promotion_add_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/bt_add_event"

    # 活动设置返回按钮
    promotion_add_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 满金额
    man_amount_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_quota"

    # 减金额
    jian_amount_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_cut_quota"

    # 添加下一优惠级别
    add_next_discount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_add_event"

    # 删除优惠
    delete_discount_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_remove"

    # 活动开始时间
    promotion_start_time_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_start_time"

    # 时间选择的取消按钮
    promotion_time_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btnCancel"

    # 时间选择的确定按钮
    promotion_time_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btnSubmit"

    # 活动结束时间
    promotion_end_time_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_end_time"

    # 适用菜品选择框
    promotion_dishes_select_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_choose_order"

    # 全场菜品
    promotion_dishes_all_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_all_order"

    # 部分菜品
    promotion_dishes_part_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_part_order"

    # 取消按钮
    promotion_dishes_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_zhaopian_quxiao"

    # 适用场景
    promotion_scene_select_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_scene"

    # 支付宝蜻蜓点餐小程序
    promotion_qt_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_ali_scene"

    # 取消按钮
    promotion_scene_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_quxiao"

    # 完成按钮
    promotion_add_finish_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/bt_add_event"

    # =================================================================================================

    # 优惠券设置
    coupon_setting_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_coupon"

    # 优惠券设置返回按钮
    coupon_setting_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 可领用
    coupon_use_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_use"

    # 未开始
    coupon_no_start_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_not_started"

    # 已领完
    coupon_receive_finished_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_already_end"

    # 已过期
    coupon_overdue_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_overdue"

    # 已撤销
    coupon_revoke_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_cancel"

    # 添加优惠券
    add_coupon_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_add_coupon"

    # 优惠券设置的返回按钮
    add_coupon_setting_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 优惠券金额
    coupon_amount_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_limit"

    # 使用条件
    coupon_condition_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_lowest_limit"

    # 劵的库存
    coupon_stock_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/et_stock"

    # 开始时间
    coupon_start_time_select_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_start_time"

    # 取消按钮
    coupon_time_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btnCancel"

    # 确定按钮
    coupon_time_confirm_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btnSubmit"

    # 结束时间
    coupon_end_time_select_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_end_time"

    # 领取方式
    way_receive_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_payment"

    # 蜻蜓点餐小程序
    way_qt_mini_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_ali_scene"

    # 取消
    way_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_quxiao"

    # 适用菜品
    dishes_select_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_choose_order"

    # 全店菜品
    dishes_select_all_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_all_order"

    # 部分菜品
    dishes_select_part_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_part_order"

    # 取消按钮
    dishes_select_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_zhaopian_quxiao"

    # 完成按钮
    dishes_select_finish_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/btn_add_coupon"

    # =================================================================================================

    # 扫码点餐设置
    scan_order_setting_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_home_set_code_order"

    # 返回按钮
    scan_order_setting_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 设置桌台号
    setting_table_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_home_set_num"

    # 返回按钮
    setting_table_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 添加按钮
    setting_table_add_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/rl_tltle_add"

    # 桌台设置
    table_name_setting_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_states"

    # 返回按钮
    table_name_setting_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 添加按钮
    table_name_setting_add_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/rl_tltle_add"

    # 桌台名称
    table_name_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_table_num"

    # 设置餐位费
    setting_table_price_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_home_set_table_money"

    # 返回按钮
    setting_table_price_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 餐位费开关
    table_price_switch_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tb_set_price"

    # 餐位费
    table_price_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/edit_price"

    # 确认保存
    table_price_save_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_save"

    # 设置小票打印机
    setting_ticket_printer_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_home_set_receipt"

    # 返回按钮
    setting_ticket_printer_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 连接状态
    ticket_connect_status_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_printer_state"

    # 打印联数
    print_unit_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_printer_coupon"

    # 选择打印联数
    select_print_unit_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/rl2"

    # 选择具体联数
    select_print_unit_num_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")'

    # 取消按钮
    select_print_unit_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_num_cancel"

    # 选择打印机
    select_printer_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/rl3"

    # 确认并保存
    setting_printer_save_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_save"

    # 编辑按钮
    edit_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_edit"

    # 设置厨房打印机
    setting_kitchen_printer_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_home_set_kitchen"

    # 返回按钮
    setting_kitchen_printer_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 连接状态
    kitchen_connect_status_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_printer_state"

    # 打印联数
    kitchen_printer_unit_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_printer_coupon"

    # 选择具体联数
    kitchen_printer_num_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")'

    # 取消按钮
    kitchen_printer_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_num_cancel"

    # 编辑按钮
    kitchen_edit_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_edit"

    # 确认并保存
    kitchen_printer_save_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_save"

    # =================================================================================================

    # 蜻蜓点餐设置
    qt_order_setting_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_home_set_dragonfly_order"

    # 返回按钮
    qt_order_setting_back_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 设置餐位费
    qt_setting_table_price_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_home_set_table_money"

    # 餐位费开关
    qt_setting_table_price_switch_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tb_set_price"

    # 餐位费
    qt_setting_price_input_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/edit_price"

    # 确认保存
    qt_setting_price_save_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_save"

    # 设置小票打印机
    qt_setting_ticket_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_home_set_receipt"

    # 返回按钮
    qt_setting_ticket_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 连接状态
    qt_setting_ticket_connect_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_printer_state"

    # 打印联数
    qt_ticket_printer_unit_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_printer_coupon"

    # 编辑按钮
    qt_ticket_edit_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_edit"

    # 选择具体联数
    qt_ticket_printer_num_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")'

    # 取消按钮
    qt_ticket_printer_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_num_cancel"

    # 选择打印机
    qt_ticket_printer_select_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_printer_type"

    # 取消按钮
    qt_ticket_printer_select_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_num_cancel"

    # 设置厨房打印机
    qt_setting_kitchen_printer_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/ll_home_set_kitchen"

    # 返回按钮
    qt_setting_kitchen_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/back_iv"

    # 连接状态
    qt_setting_kitchen_connect_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_printer_state"

    # 打印联数
    qt_kitchen_printer_unit_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_printer_coupon"

    # 编辑按钮
    qt_kitchen_edit_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/but_edit"

    # 选择具体联数
    qt_kitchen_printer_num_loc = MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")'

    # 取消按钮
    qt_kitchen_printer_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_num_cancel"

    # 选择打印机
    qt_kitchen_printer_select_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_printer_type"

    # 取消按钮
    qt_kitchen_printer_select_cancel_loc = MobileBy.ID, "com.cashier.jiutongshanghu:id/tv_num_cancel"

