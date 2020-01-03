# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/4

E-mail:keen2020@outlook.com

=================================


"""

import os
import pytest
import time
import logging

from common import logger
from common.send_email import SendEmail
from common.dir_config import LOGS_DIR
from common.tools import get_cmd_result

"""
运行前的注意事项
1. 当前设备是否连接OK
2. 当前启动参数是否与所连接设配一致
3. 配置工具是否卸载完成


"""

if __name__ == '__main__':
    mail_title = "24小时登录登出监测异常邮件"
    mail_message = "详情情查看附件日志,请实际使用手机测试登录"
    log_name = "log.log"
    file_path = os.path.join(LOGS_DIR, log_name)

    # 参数 -x 代表用例失败就停止运行测试脚本
    pytest.main(
        ["-s", "-v", "-m", "screen", "--html=output/reports/report.html", "--alluredir=output/allure"])

    # 直接打开报告
    os.system("allure serve output/allure")

    # print("error")
    # SendEmail.send_qq1_file_mail(mail_title, mail_message, file_path)
