#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import requests

# 程序主入口
if __name__ == "__main__":
    url = 'https://localhost:8596/bop-oms/pay/query'
    headers = {
        'Content-Type': 'application/json',
        'client': 'WEB',
        'projectId': '5000430'
    }
    dataDict = {
        "data": {
            "serialNo": "79241011513313528544"
        }
    }
    dataJson = json.dumps(dataDict)
    request = requests.post(url, dataJson, headers=headers)
    text = request.text
    print(text)
