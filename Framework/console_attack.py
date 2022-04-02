#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import datetime
from multiprocessing import Pool, Manager
from Tools.ReBuild import get_payload
from Config.config_logging import loglog
from Moudle.Moudle_index import *

def urlcheck(url):
    if 'http' in url:
        return url
    else:
        return ('http://'+str(url))

def get_urls(file):
    f=open(file,'r')
    r=f.readlines()
    f.close()
    res=[]
    for i in r:
        res.append(urlcheck(i).replace('\n',''))
    return res

def record_res(dic):
    if dic:
        res='['+datetime.datetime.now().strftime('%X')+']  '
        for key in dic:
            value = dic[key]
            res=res+str(key)+' : '+str(value)+'\t'
        print(res)
        loglog(res)


def pocs(target,moudle,q):
    q.put(target)
    return eval(moudle).poc(target)

def poolmana(moudle,urls):
    p = Pool(30)
    q = Manager().Queue()
    for i in urls:
        p.apply_async(pocs, args=(i,moudle,q,),callback=record_res)
    p.close()
    p.join()


def run_poc(*args):
    if len(args)==2:
        if isinstance(args[1],str):
            record_res(eval(args[0]).poc(urlcheck(args[1])))
        elif isinstance(args[1], list):
            poolmana(args[0], args[1])

def run_moudle(*args):
    if len(args)==2:
        if isinstance(args[1],str):
            for i in get_payload(args[0]):
                record_res(eval(i[0]).poc(urlcheck(args[1])))
        elif isinstance(args[1], list):
            print('任务加载数量：' + str(len(args[1])))
            for i in get_payload(args[0]):
                poolmana(i[0], args[1])


if __name__ == '__main__':
    run_poc('zabbix_admin',"http://127.0.0.1")
