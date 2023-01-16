#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

from Config.config_proxies import proxies
from Config.config_requests import ua, headers

#这里保留不用管即可，防止https请求报错的
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
    result={}     # 必要的接口，返回值要这个格式

    #可以引入header，默认只带ua，如需自定义headers，仅引入ua即可
    headers={
        "User-Agent":ua
    }

    try:
        req = requests.get(target+'/robots.txt', headers=headers, timeout=3, verify=False,proxies=proxies)
        if "Disallow" in req.text:
            result['target'] = target     #三项四项完全无所谓，只要前两项默认即可
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