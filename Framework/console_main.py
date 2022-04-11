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

from Config.config_api import FOFA_API_KEY, SHODAN_API_KEY, HUNTER_API_KEY
from Config.config_print import status_print
from Framework import console_attack
from Seek import fofaapi, shodanapi, hunterapi
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
    M_SEEK.add_argument("-hunter", dest='hunter',help="资产爬取")
    M_SEEK.add_argument("-shodan", dest='shodan',help="资产爬取")
    M_SEEK.add_argument("-num", dest='num',help="资产数量")

    args = parser.parse_args()

########################################################################################################################

    if args.fofa:
        try:
            if FOFA_API_KEY:
                if args.num and int(args.num) > 10000:
                    status_print("Num Don't > 10000 PLS~",2)
                elif args.num and int(args.num) <= 10000:
                    fofaapi.run(args.fofa, args.num)
                else:
                    fofaapi.run(args.fofa,1000)
            else:
                status_print("如需使用FofaAPI，请在Config/config_api下完成相关配置",2)
        except Exception as e:
            status_print("发生错误，%s"%e,3)
    elif args.shodan:
        try:
            if SHODAN_API_KEY:
                if args.num and int(args.num) > 1000:
                    status_print("Num Don't > 1000 PLS~",2)
                elif args.num and int(args.num) <= 1000:
                    shodanapi.run(args.shodan, args.num)
                else:
                    shodanapi.run(args.shodan,1000)
            else:
                status_print("如需使用ShodanAPI，请在Config/config_api下完成相关配置",2)
        except Exception as e:
            status_print("发生错误，%s" % e, 3)
    elif args.hunter:
        try:
            if HUNTER_API_KEY:
                if args.num and int(args.num) > 10000:
                    status_print("Num Don't > 10000 PLS~",2)
                elif args.num and int(args.num) <= 1000:
                    hunterapi.run(args.hunter, args.num)
                else:
                    hunterapi.run(args.hunter,1000)
            else:
                status_print("如需使用HunterAPI，请在Config/config_api下完成相关配置",2)
        except Exception as e:
            status_print("发生错误，%s" % e, 3)
    elif args.poc:
        try:
            if args.url:
                console_attack.run_poc(args.poc, args.url)
            elif args.file:
                console_attack.run_poc(args.poc, get_urls(args.file))
            else:
                status_print("Usage:\n\tpython Meppo.py -poc xxx -u http:xxx\n\tpython Meppo.py -poc xxx -f target.txt",5)
        except Exception as e:
            status_print("发生错误：%s" % e, 3)
    elif args.moudle:
        try:
            if args.list:
                payload_list(args.moudle)
            elif args.url:
                console_attack.run_moudle(args.moudle, args.url)
            elif args.file:
                console_attack.run_moudle(args.moudle, get_urls(args.file))
            else:
                status_print("Usage:\n\tpython Meppo.py -m -l\n\tpython Meppo.py -m xxx -u http:xxx\n\tpython Meppo.py -m -f target.txt",5)
        except Exception as e:
            status_print("发生错误：%s" % e, 3)
    elif args.list:
        moudle_list()
    elif args.listall:
        payload_list_all()
    else:
        status_print("Usage:"
              "\n\tpython Meppo.py -l\t\t\t\tList All Moudles"
              "\n\tpython Meppo.py -ll\t\t\t\tList All Payloads"
              "\n\tpython Meppo.py -m xxx -l\t\t\tList Payload Of The Moudle"
              "\n\tpython Meppo.py -poc xxx -u target\t\t单目标 单POC监测"
              "\n\tpython Meppo.py -poc xxx -f targets.txt\t\t多目标 单POC监测"
              "\n\tpython Meppo.py -m xxx -u target\t\t单目标 模块监测"
              "\n\tpython Meppo.py -m xxx -f targets.txt\t\t多目标 模块监测"
              "\n\tpython Meppo.py -fofa APP=\"DEMO\"\t\tFOFA API 报告导出 num默认1000"
              "\n\tpython Meppo.py -fofa APP=\"DEMO\" -num 100\tFOFA API 报告导出 自定义数量"
              "\n\tpython Meppo.py -hunter APP=\"DEMO\"\t\tHUNTER API 报告导出 num默认1000"
              "\n\tpython Meppo.py -hunter APP=\"DEMO\" -num 100\tSHODAN HUNTER 报告导出 自定义数量"
              "\n\tpython Meppo.py -shodan APP=\"DEMO\"\t\tSHODAN API 报告导出 num默认1000"
              "\n\tpython Meppo.py -shodan APP=\"DEMO\" -num 100\tSHODAN API 报告导出 自定义数量",5)


########################################################################################################################
