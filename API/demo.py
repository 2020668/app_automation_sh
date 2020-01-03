# -*- coding: utf-8 -*-
"""
=================================
Author: keen
Created on: 2019/12/18
E-mail:keen2020@outlook.com
=================================

"""

import logging
from common import logger

from API.http_request import HTTPRequest
from common.tools import get_line_token

url = "https://isv.hczypay.com/api/merchant/getStoreFaceCount"

data = {"storeId": "2019121709394369062",
        "deviceId": "HMDF4PQ191122009582",
        "beginTime": "2019-11-24 18:46:45",
        "endTime": "2019-12-24 18:46:07"}

request = HTTPRequest()

# data = {"page": page, "terminalName": terminal_name, "time_start": time_start, "time_end": time_end,
#         "type_source": type_source, "token": token, "storeName": store_name, "status": order_status}

response = request.request(method="post", url=url, data=data)

res = response.json()
print(res)


