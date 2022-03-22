#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


import sys
import requests
from Config.config_requests import ua
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 脚本信息
######################################################
NAME='Weblogic_Console_Info_Leak'
AUTHOR = "Faith"
REMARK = 'Weblogic控制台路径泄露'
FOFA_RULE='app="Oracle-BEA-WebLogic-Server"'
######################################################

def poc(target):
    result={}
    vuln_url = target + '/console/login/LoginForm.jsp'
    headers = {"User-Agent":ua}

    r = requests.get(vuln_url, headers=headers,verify=False,timeout=3)
    try:
        if r.status_code == 200:
            result['target'] = target
            result['poc'] = NAME
            result['url'] = vuln_url
            return result
        else:
            pass
    except:
        pass


if __name__ == '__main__':
    poc("http://127.0.0.1")