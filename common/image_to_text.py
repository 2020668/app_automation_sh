# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/12/30
E-mail:keen2020@outlook.com
=================================

"""

from PIL import ImageGrab, Image
import keyboard         # 监控键盘
from time import sleep
import sys
from aip import AipOcr
import os
import time
import logging

from common.dir_config import CUSTOM_SIZE_IMG_DIR
from common import logger


class BaiduAIP(object):

    """
    需要以下第三方库支持
    Pillow  Pillow-PIL  baidu-aip  beautifulsoup4  certifi
    cardet  gImageGrabber  idna  keyboard  pip
    requests  selenium  setuptools  urllib3

    识别成功率不是百分百

    """

    def picture_text(self, file_path):
        api_id = '18139952'
        api_key = 'P8n2xzTINvdL9D60PrlDt1vg'
        secret_key = 'xbBu1GIhMqAtVeY9NuGE3LxGyLk9WnBA'

        aipocr = AipOcr(api_id, api_key, secret_key)

        image = self.get_file_content(file_path)
        texts = aipocr.basicGeneral(image)
        allTexts = ''

        for words in texts['words_result']:
            allTexts = allTexts + ''.join(words.get('words', ''))
        logging.info("文字识别成功,返回值-->{}".format(allTexts) if allTexts != '' else "文字识别失败,返回空str")
        time.sleep(1)
        return allTexts

    #   print(texts)

    def get_file_content(self, a):
        with open(a, 'rb') as fp:
            return fp.read()


def screen_shot():

    # 用于获取剪切板图片信息并保存到本地
    # ctrl+alt+a 这个看你用什么截图，qq是个
    if keyboard.wait(hotkey='ctrl+alt+a') is None:
        if keyboard.wait(hotkey='enter') is None:
            sleep(0.01)
            im_gray = ImageGrab.grabclipboard()
            #            print(im_gray)
            if isinstance(im_gray, Image.Image):
                im_gray.save("demo.jpg")
            else:
                print('请重新截图')
    else:
        print('请使用qq截图，记得截图后按enter')


if __name__ == '__main__':
    api = BaiduAIP()
    test = api.picture_text(os.path.join(CUSTOM_SIZE_IMG_DIR, "时间的小时.png"))
    print(test)
    print(type(test))
    if test == '':
        print("识别失败,返回为None")

