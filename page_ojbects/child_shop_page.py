# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""


from appium.webdriver.common.mobileby import MobileBy
import time
from common.basepage import BasePage
from page_locators.child_shop_page_locator import ChildShopPageLocator as Loc
from common.tools import uninstall_appium_settings, uninstall_uiautomator2
from data import child_shop_data as ad


class ChildShopPage(BasePage):

    # 添加子门店
    def add_shop_action(self, shop_name, shop_address, people_name, phone_num, pwd):

        self.wait_ele_visible(loc=Loc.my_loc, img_desc="我的 按钮")
        self.get_element(loc=Loc.my_loc, img_desc="我的 按钮", find_all=True)[2].click()

        self.wait_ele_visible(loc=Loc.shop_manage_loc, img_desc="门店管理 按钮")
        self.click_element(loc=Loc.shop_manage_loc, img_desc="门店管理 按钮")

        self.wait_ele_visible(loc=Loc.add_shop_loc, img_desc="添加门店 按钮")
        self.click_element(loc=Loc.add_shop_loc, img_desc="添加门店 按钮")

        self.wait_ele_visible(loc=Loc.shop_name_input_loc, img_desc="门店名称输入框")
        self.input_text(loc=Loc.shop_name_input_loc, value=shop_name, img_desc="门店名称输入框")

        self.wait_ele_visible(loc=Loc.shop_address_input_loc, img_desc="门店地址输入框")
        self.input_text(loc=Loc.shop_address_input_loc, value=shop_address, img_desc="门店地址输入框")

        self.wait_ele_visible(loc=Loc.people_name_input_loc, img_desc="联系人姓名输入框")
        self.input_text(loc=Loc.people_name_input_loc, value=people_name, img_desc="联系人姓名输入框")

        self.wait_ele_visible(loc=Loc.phone_input_loc, img_desc="联系人电话号码输入框")
        self.input_text(loc=Loc.phone_input_loc, value=phone_num, img_desc="联系人电话号码输入框")

        self.wait_ele_visible(loc=Loc.next_loc, img_desc="下一步 按钮")
        self.click_element(loc=Loc.next_loc, img_desc="下一步 按钮")

        time.sleep(2)

        self.wait_ele_visible(loc=Loc.pwd_input_loc, img_desc="登录密码输入框")
        self.input_text(loc=Loc.pwd_input_loc, value=pwd, img_desc="登录密码输入框")

        self.wait_ele_visible(loc=Loc.next_loc, img_desc="下一步 按钮")
        self.click_element(loc=Loc.next_loc, img_desc="下一步 按钮")

        time.sleep(2)

        self.wait_ele_visible(loc=Loc.sure_loc, img_desc="确定按钮")
        self.click_element(loc=Loc.sure_loc, img_desc="确定按钮")

        self.wait_ele_visible(loc=Loc.finish_loc, img_desc="完成按钮")
        self.click_element(loc=Loc.finish_loc, img_desc="完成按钮")

        return self

    def edit_child_shop_login_pwd(self, shop_num, pwd):

        self.wait_ele_visible(loc=Loc.my_loc, img_desc="我的 按钮")
        self.get_element(loc=Loc.my_loc, img_desc="我的 按钮", find_all=True)[2].click()

        self.wait_ele_visible(loc=Loc.shop_manage_loc, img_desc="门店管理 按钮")
        self.click_element(loc=Loc.shop_manage_loc, img_desc="门店管理 按钮")

        self.wait_ele_visible(loc=Loc.shop_name_loc, img_desc="子门店名称")
        self.get_element(loc=Loc.shop_name_loc, img_desc="子门店名称", find_all=True)[shop_num].click()

        self.wait_ele_visible(loc=Loc.edit_login_pwd_loc, img_desc="重置门店密码 按钮")
        self.click_element(loc=Loc.edit_login_pwd_loc, img_desc="重置门店密码 按钮")

        # 输入新密码
        self.wait_ele_visible(loc=Loc.pwd_input_loc, img_desc="登录密码输入框")
        self.input_text(loc=Loc.pwd_input_loc, value=pwd, img_desc="登录密码输入框")

        self.wait_ele_visible(loc=Loc.next_loc, img_desc="完成 按钮")
        self.click_element(loc=Loc.next_loc, img_desc="完成 按钮")

        time.sleep(1)

        self.wait_ele_visible(loc=Loc.finish_loc, img_desc="完成 按钮")
        self.click_element(loc=Loc.finish_loc, img_desc="完成 按钮")

    # 获取登出状态
    def get_add_status(self, shop_name):

        # 门店名称
        shop_name_loc = MobileBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceID('com.cashier.jiutongshanghu:id" \
                                                      "/tv_store_name').text('{}')".format(shop_name)
        self.wait_ele_visible(shop_name_loc, "商户名称")
        status = self.get_text(shop_name_loc, "商户名称")
        if status == ad.add_success_data["shop_name"]:
            return True
        else:
            return False
