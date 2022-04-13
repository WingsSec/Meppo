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

from Config.config_print import status_print
from Tools.NoRepeat import Norepeat
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
    return Norepeat(res)

def record_res(dic):
    if dic:
        res='['+datetime.datetime.now().strftime('%X')+']  '
        for key in dic:
            value = dic[key]
            res=res+str(key)+' : '+str(value)+'\t'
        status_print(res,1)
        loglog(res)

# 讲道理，框架不该对脚本做异常屏蔽的，但是孩子们不听话，不做异常捕获，导致批量异常相互干扰，先启用吧
def pocs(target,moudle,q):
    q.put(target)
    res=""
    try:
        res=eval(moudle).poc(target)
    except:
        pass
    return res

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
            status_print('任务加载数量：' + str(len(args[1])), 0)
            poolmana(args[0], args[1])

def run_moudle(*args):
    if len(args)==2:
        if isinstance(args[1],str):
            for i in get_payload(args[0]):
                record_res(eval(i[0]).poc(urlcheck(args[1])))
        elif isinstance(args[1], list):
            status_print('任务加载数量：' + str(len(args[1])),0)
            for i in get_payload(args[0]):
                poolmana(i[0], args[1])


if __name__ == '__main__':
    run_poc('zabbix_admin',"http://127.0.0.1")
