#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import re
import urllib
import binascii

from Config.config_proxies import proxies
from Config.config_requests import headers
requests.packages.urllib3.disable_warnings()

########################################################################################################################
# 脚本信息
NAME = 'UnauthorizedScript'
AUTHOR = "RabbitMask"
REMARK = 'Jenkins未授权脚本执行'
FOFA_RULE = 'app="Jenkins"'

########################################################################################################################
# 漏洞检测模块
def poc(target):
    result = {}
    try:
        req = requests.get(target+'/script', headers=headers, timeout=5,proxies=proxies)
        if req.status_code == 200 and 'Jenkins.instance.pluginManager.plugins' in req.text:
            result['target'] = target
            result['poc'] = NAME
            result['url'] = target+'/script'
            return result
    except:
        pass


