#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import argparse
from Framework import console_attack
from Seek import fofaapi
from Framework.console_attack import get_urls
from Framework.console_list import moudle_list, payload_list, payload_list_all
from Moudle.Moudle_index import *



def Console():
    parser = argparse.ArgumentParser()
    M_POC = parser.add_argument_group('漏洞检测模块')
    M_SEEK = parser.add_argument_group('资产爬取模块')

########################################################################################################################
    parser.add_argument("-l", dest='list',help="list",action='store_true')
    parser.add_argument("-ll", dest='listall',help="list all",action='store_true')
    parser.add_argument("-m", dest='moudle',help="moudle")
    parser.add_argument("-u", dest='url',help="target url")
    parser.add_argument("-f", dest='file',help="the file of target list")


    #漏洞检测模块
    M_POC.add_argument("-poc", dest='poc',help="漏洞检测")


    #资产爬取模块
    M_SEEK.add_argument("-fofa", dest='fofa',help="资产爬取")
    M_SEEK.add_argument("-num", dest='num',help="资产数量")

    args = parser.parse_args()

########################################################################################################################

    if args.fofa:
        if args.num and int(args.num) > 10000:
            print("Num Don't > 10000 PLS~")
        else:
            fofaapi.run(args.fofa, 1000)
    elif args.poc:
        try:
            if args.url:
                console_attack.run_poc(args.poc, args.url)
            elif args.file:
                console_attack.run_poc(args.poc, get_urls(args.file))
            else:
                print("Usage:\n\tpython Meppo.py -poc xxx -u http:xxx\n\tpython Meppo.py -poc xxx -f target.txt")
        except:
            print("Usage:\n\tpython Meppo.py -poc xxx -u http:xxx\n\tpython Meppo.py -poc xxx -f target.txt")
    elif args.moudle:
        try:
            if args.list:
                payload_list(args.moudle)
            elif args.url:
                console_attack.run_moudle(args.moudle, args.url)
            elif args.file:
                console_attack.run_moudle(args.moudle, get_urls(args.file))
            else:
                print("Usage:\n\tpython Meppo.py -m -l\n\tpython Meppo.py -m xxx -u http:xxx\n\tpython Meppo.py -m -f target.txt")
        except:
            print("Usage:\n\tpython Meppo.py -m -l\n\tpython Meppo.py -m xxx -u http:xxx\n\tpython Meppo.py -m -f target.txt")
    elif args.list:
        moudle_list()
    elif args.listall:
        payload_list_all()
    else:
        print("Usage:\n\tStep 1: python Meppo.py -l\n\tStep 2: python Meppo.py -m xxx -l\n\tStep 3: python Meppo.py -m / -poc \n\t")


########################################################################################################################
