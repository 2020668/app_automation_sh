# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/8/29
E-mail:keen2020@outlook.com
=================================

"""

import os

# 框架项目顶层目录
BASE_DIR = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

TEST_DATA_DIR = os.path.join(BASE_DIR, "data")

TEST_CASES_DIR = os.path.join(BASE_DIR, "test_cases")

REPORT_DIR = os.path.join(BASE_DIR, "output/reports")

LOGS_DIR = os.path.join(BASE_DIR, "output/logs")

# config_dir =  os.path.join(base_dir,"Config")

SCREENSHOT_DIR = os.path.join(BASE_DIR, "output/screenshots")

CUSTOM_SIZE_IMG_DIR = os.path.join(BASE_DIR, "output/custom_size_img")

CAPS_DIR = os.path.join(BASE_DIR, "caps")
