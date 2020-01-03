# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

import pytest
import logging
import time
import os

from page_ojbects.login_page import LoginPage
from page_ojbects.index_page import IndexPage
from page_ojbects.logout_page import LogoutPage
from common.tools import uninstall_appium_settings, uninstall_uiautomator2
from data import login_data as ld
from common import logger
from common.send_email import SendEmail
from common.dir_config import LOGS_DIR
from common.dir_config import TEST_DATA_DIR
from common.logger import log_name


# @pytest.mark.usefixtures("start_app")
@pytest.mark.twenty_four_hours
@pytest.mark.usefixtures("run_app")
class TestTwentyFourHours(object):

    @pytest.mark.parametrize("data", ld.success_data)
    def test_twenty_four_hours(self, data, run_app):

        mail_title = "24小时登录登出监测异常邮件"
        mail_message = "详情情查看附件日志,请实际使用手机测试登录!"

        file_path = LOGS_DIR + log_name

        # 执行登录
        LoginPage(run_app).login_action(data["user"], data["pwd"])

        time.sleep(10)

        # 获取登录状态
        assert IndexPage(run_app).get_login_status() is True

        # 执行登出
        LogoutPage(run_app).logout_action()

        time.sleep(10)

        count_file = os.path.join(TEST_DATA_DIR, "count.txt")

        with open(count_file, "r+") as f:
            count = f.read()
            count = int(count) + 1

            f.seek(0)
            f.truncate()

            f.write(str(count))
            f.close()

        logging.info("已完成 {} 次 自动登录登出测试".format(count))

        uninstall_uiautomator2()
        uninstall_appium_settings()
