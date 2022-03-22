#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _    
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   < 
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
                                                    
'''
import os
from importlib import import_module
from collections import Counter

########################################################################################################################
#pro
def get_moudle():
    dir = 'Moudle'    #pro
    # dir = '../Moudle'   #dev
    list=os.listdir(dir)
    moudles=[]
    for i in list:
        if i !='__pycache__':
            path = os.path.join(dir, i)
            if os.path.isdir(path):
                moudles.append(i)
    return moudles

def get_payload(moudle):
    dir = 'Moudle/'+moudle    #pro
    # dir = '../Moudle/'+moudle   #dev
    list = os.listdir(dir)
    payloads = []
    for i in list:
        tmp=[]
        path = os.path.join(dir, i)
        if os.path.isfile(path):
            if '.py' in i:
                payload=i.replace('.py','')
                tmp.append(payload)
                tmp.append(get_remark(moudle,payload))
                payloads.append(tmp)
    return payloads

def get_remark(moudle,payload):
    return import_module('Moudle.'+moudle+'.'+payload).REMARK





def Rebuild():
    str=""
    moudles=get_moudle()
    MOUDLE_NUM = len(moudles)
    PAYLOAD_NUM = 0
    for i in moudles:
        str=str+("# {}\n".format(i))
        for j in get_payload(i):
            str=str+("from Moudle.{} import {}\n".format(i,j[0]))
            PAYLOAD_NUM=PAYLOAD_NUM+1
        str=str+("\n")
    NUM="MOUDLE_NUM={}\nPAYLOAD_NUM={}\n\n".format(MOUDLE_NUM,PAYLOAD_NUM)
    f=open('Moudle/Moudle_index.py','w')
    f.write(NUM+str)
    f.close()


########################################################################################################################
#dev
def get_moudle_dev():
    # dir = 'Moudle'    #pro
    dir = '../Moudle'   #dev
    list=os.listdir(dir)
    moudles=[]
    for i in list:
        if i !='__pycache__':
            path = os.path.join(dir, i)
            if os.path.isdir(path):
                moudles.append(i)
    return moudles
def get_payload_dev(moudle):
    # dir = 'Moudle/'+moudle    #pro
    dir = '../Moudle/'+moudle   #dev
    list = os.listdir(dir)
    payloads = []
    for i in list:
        tmp=[]
        path = os.path.join(dir, i)
        if os.path.isfile(path):
            if '.py' in i:
                payload=i.replace('.py','')
                tmp.append(payload)
                tmp.append(get_remark(moudle,payload))
                tmp.append(get_author(moudle, payload))     #dev
                payloads.append(tmp)
    return payloads
    
def get_author(moudle,payload):
    return import_module('Moudle.'+moudle+'.'+payload).AUTHOR
    
def Rebuild_dev():
    moudles=get_moudle_dev()
    res=[]
    for i in moudles:
        for j in get_payload_dev(i):
            res.append(j[2])
    dic=Counter(res)
    for key in dic:
        value = dic[key]
        print(key,value)


if __name__ == '__main__':
    # get_moudle()
    # Rebuild()
    Rebuild_dev()