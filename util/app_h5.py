# -*- coding: utf-8 -*-
"""

=================================
Author: keen
Created on: 2019/10/2

E-mail:keen2020@outlook.com

=================================


"""

"""
app自动化 + web自动化 结合  从原生应用切换到 webview网页
1、确认页面是混合页面，内嵌html android.webkit.webview
2、开启webview的调试模式  让代码识别到webview网页的存在
3、操作到内嵌html页面时，需要切换到html页面，才能对html页面的元素进行操作
    driver.switch_to.context(webview)
4、切换到html后，一切都是web自动化
    1、元素定位
    2、chromedriver版本（与内核webview匹配）

"""