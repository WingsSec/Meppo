#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import base64
import requests

from Config.config_decorators import Save_Csv
from Config.config_api import FOFA_EAMIL, FOFA_API_KEY
from Tools.SaveHosts import gethosts


def fofaapi(keyword,num):
    reslist=[]
    bkeyword = bytes(keyword, encoding="utf8")
    bs64 = base64.b64encode(bkeyword)
    bs64 = bs64.decode()
    res = requests.get('https://fofa.info/api/v1/search/all?email={}&key={}&qbase64={}&fields=host,ip,port,country,city,server,title&size={}'.format(FOFA_EAMIL,FOFA_API_KEY,bs64,str(num)))
    result = res.json()['results']
    hosts=[]
    for i in result:
        dic={}
        dic['host'] = i[0]
        dic['ip'] = i[1]
        dic['port'] = i[2]
        dic['country'] = i[3]
        dic['city'] = i[4]
        dic['server'] = i[5]
        dic['title'] = i[6]
        reslist.append(dic)
        print(dic)
    gethosts(hosts)
    return reslist

@Save_Csv
def run(keyword,num):
    return fofaapi(keyword,num)


if __name__ == '__main__':
    fofaapi('app="test"',3)
