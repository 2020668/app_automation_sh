# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/29
E-mail:keen2020@outlook.com
=================================

"""

import yaml

"""
读取yaml文件的数据，并转换成python对象
1、打开yaml文件
2、使用yaml的load()函数
"""

fs = open("conf.yaml")
obj = yaml.load(fs)
print(obj)
