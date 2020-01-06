# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/29
E-mail:keen2020@outlook.com
=================================

"""

import logging
from logging.handlers import RotatingFileHandler
import os
import time
from common import dir_config

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

handler_1 = logging.StreamHandler()

curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())

log_name = dir_config.LOGS_DIR + "/App_Automation_{0}.log".format(curTime)

handler_2 = RotatingFileHandler(log_name, backupCount=20, encoding='utf-8')

# handler_2 = RotatingFileHandler(dir_config.LOGS_DIR + "/App_Autotest.log", backupCount=20, encoding='utf-8')

# 设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO, handlers=[handler_1, handler_2])

if __name__ == '__main__':
    logging.info("hehehe")
