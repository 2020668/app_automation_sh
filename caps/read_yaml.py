# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/29
E-mail:keen2020@outlook.com
=================================

"""

import yaml
import os
from common.dir_config import CAPS_DIR

"""
读取yaml文件的数据，并转换成python对象
1、打开yaml文件
2、使用yaml的load()函数
"""


def read_config():
    fs = open(os.path.join(CAPS_DIR, "env.yaml"), encoding="utf8")
    obj = yaml.safe_load(fs)
    if obj.get("env") == "produce":
        fs = open(os.path.join(CAPS_DIR, "produce.yaml"), encoding="utf8")
    elif obj.get("env") == "test":
        fs = open(os.path.join(CAPS_DIR, "test.yaml"), encoding="utf8")
    obj = yaml.safe_load(fs)
    return obj


conf = read_config()


if __name__ == '__main__':
    y = conf.get("env").get("url")
    print(y)
