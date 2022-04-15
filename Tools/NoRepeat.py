#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _    
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   < 
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
                                                    
'''
from Config.config_print import status_print


def Norepeat(mylist):
    status_print("数据去重前：{}条数据".format(len(mylist)),0)
    data = list(set(mylist))
    data.sort()
    status_print("数据去重后：{}条数据".format(len(data)),0)
    return data