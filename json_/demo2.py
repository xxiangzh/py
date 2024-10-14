#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

# 程序主入口
if __name__ == "__main__":
    '''
        {
            "errorCode": 0,
            "message": "success",
            "data": {
                "serialNo": "string",
                "state": "PRCESSING",
                "errorMessage": "处理中",
                "records": [
                    {
                        "id": "1",
                        "name": "A"
                    },
                    {
                        "id": "2",
                        "name": "B"
                    }
                ]
            }
        }
    '''

    res = '{"errorCode":0,"message":"success","data":{"serialNo":"string","state":"PRCESSING","errorMessage":"处理中","records":[{"id":"1","name":"A"},{"id":"2","name":"B"}]}}'

    # 字符串转字典
    pythonDict = json.loads(res)

    # []取值，如果key不存在会抛异常
    print(pythonDict['data']['records'][0]['name'])

    # get取值，不会抛异常，不存在返回None，可设置返回默认值
    print(pythonDict.get('data').get('records')[0].get('name', "默认值"))

