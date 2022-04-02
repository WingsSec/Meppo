#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import shodan

from Config.config_decorators import Save_Csv
from Config.config_port import HTTPS_PORT
from Config.config_api import SHODAN_API_KEY

api = shodan.Shodan(SHODAN_API_KEY)

def shodanapi(keyword,num):
    reslist=[]
    results = (api.search(keyword,1,num))
    for i in results['matches']:
            if i['port'] in HTTPS_PORT:
                url = 'https://' + i['ip_str']
            else:
                url = 'http://' + i['ip_str']
            dic = {}
            dic['host'] = url
            dic['ip'] = i['ip_str']
            dic['port'] = i['port']
            dic['country'] = i['location']['country_name']
            dic['city'] = i['location']['city']
            try:
                dic['server'] = i['http']['server']
                dic['title'] = i['http']['title']
            except:
                dic['server'] = ''
                dic['title'] = ''
            reslist.append(dic)
            print(dic)
    return reslist


@Save_Csv
def run(keyword,num):
    return shodanapi(keyword,num)


if __name__ == '__main__':
    shodanapi('drupal8',3)