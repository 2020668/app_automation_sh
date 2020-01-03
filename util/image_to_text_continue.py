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


class API(object):

    """
    需要以下第三方库支持
    Pillow  Pillow-PIL  baidu-aip  beautifulsoup4  certifi
    cardet  gImageGrabber  idna  keyboard  pip
    requests  selenium  setuptools  urllib3
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
        return allTexts

    #   print(texts)

    def get_file_content(self, a):
        with open(a, 'rb') as fp:
            return fp.read()


def screen_shot():

    # 用于获取剪切板图片信息并保存到本地
    # ctrl+alt+a 这个看你用什么截图，qq是个
    if keyboard.wait(hotkey='ctrl+alt+a') == None:
        if keyboard.wait(hotkey='enter') == None:
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
    api = API()
    for _ in range(sys.maxsize):
        screen_shot()
        test = api.picture_text(r'demo.jpg')
        print(test)

