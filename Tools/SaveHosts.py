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

from Config.config_print import status_print


def gethosts(result):
    if result:
        timetoken = datetime.datetime.now().strftime('%Y%m%d%H%M%S');
        filename = 'Output/{}_result_{}.txt'.format('run', timetoken)
        for i in result:
            try:
                fw = open(filename, 'a')
                fw.write(i.replace('\n', '') + '\n')
                fw.close()
            except:
                pass
        status_print('HOST结果已保存至：' + filename, 1)