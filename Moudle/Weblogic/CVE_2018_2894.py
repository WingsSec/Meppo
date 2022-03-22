#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


import requests
from Config.config_requests import ua
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 脚本信息
######################################################
NAME='CVE_2018_2894'
AUTHOR = "Faith"
REMARK = 'Weblogic任意文件上传漏洞'
FOFA_RULE='app="Oracle-BEA-WebLogic-Server"'
######################################################

def poc(target):
    result={}
    vuln_url1 = target + '/ws_utc/login.do'
    vuln_url2 = target + '/ws_utc/config.do'
    headers = {"User-Agent":ua}
    r1 = requests.get(vuln_url1,headers=headers,timeout=3)
    r2 = requests.get(vuln_url2,headers=headers,timeout=3)
    try:
        if r1.status_code == 200 and r2.status_code == 200:
            result['target'] = target
            result['poc'] = NAME
            result['url1'] = vuln_url1
            result['url2'] = vuln_url2
            return result
        elif r1.status_code == 200 and r2.status_code !=200:
            result['target'] = target
            result['poc'] = NAME
            result['url'] = vuln_url1
            return result
        elif r1.status_code != 200 and r2.status_code == 200:
            result['target'] = target
            result['poc'] = NAME
            result['url'] = vuln_url2
            return result
        else:
            pass
    except:
        pass

if __name__ == '__main__':
    poc("http://127.0.0.1")