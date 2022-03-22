#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from Config.config_requests import headers

requests.packages.urllib3.disable_warnings()


########################################################################################################################
# 脚本信息
NAME='Demo'
AUTHOR="RabbitMask"
REMARK='robots.txt敏感信息泄露'
FOFA_RULE='对应漏洞框架的fofa语法'
########################################################################################################################
# 漏洞检测模块
def poc(target):
    result={}
    try:
        req = requests.get(target+'/robots.txt', headers=headers, timeout=3, verify=False)
        if "Disallow" in req.text:
            result['target'] = target
            result['poc'] = NAME
            result['xxx'] = '按需求随便写，删了都行'
            return result
    except:
        pass
########################################################################################################################
                                        #以上为模板限制区域，以下为自由发挥区域
########################################################################################################################
# 漏洞利用模块
def exp(target):
    try:
        req = requests.get(target+'/robots.txt', headers=headers, timeout=3, verify=False)
        if "Disallow" in req.text:
            print(req.text)
    except:
        pass

if __name__ == '__main__':
    exp('http://127.0.0.1')