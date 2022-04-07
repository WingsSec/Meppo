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
from Tools.ReBuild import get_moudle, get_payload

def get_cn_number(char):
    count = 0
    for item in char:
        if 0x4E00 <= ord(item) <= 0x9FA5:
            count += 1
    return count

def moudle_list():
    list=get_moudle()
    status_print('【Moudle List】'.center(30),6)
    status_print('Moudle'.center(30), 6)
    status_print('================================',6)
    for i in list:
        status_print('--------------------------------',6)
        status_print('|{}|'.format(i.center(30-get_cn_number(i))),6)
    status_print('================================',6)



def payload_list(moudle):
    list=get_payload(moudle)
    status_print('【Payload List】'.center(110),6)
    status_print('==================================================================================================================',6)
    status_print('|{}|{}|{}|'.format('Moudle'.center(20),'Payload'.center(30), 'Remark'.center(60)))
    for i in list:
        status_print('------------------------------------------------------------------------------------------------------------------',6)
        status_print('|{}|{}|{}|'.format(moudle.center(20),i[0].center(30-get_cn_number(i[0])),i[1].center(60-get_cn_number(i[1]))),6)
    status_print('==================================================================================================================',6)


def payload_list_all():
    status_print('【Payload List】'.center(110),6)
    status_print('==================================================================================================================',6)
    status_print('|{}|{}|{}|'.format('Moudle'.center(20),'Payload'.center(30), 'Remark'.center(60)),6)
    for i in get_moudle():
        list = get_payload(i)
        for j in list:
            status_print('------------------------------------------------------------------------------------------------------------------',6)
            status_print('|{}|{}|{}|'.format(i.center(20-get_cn_number(i)),j[0].center(30-get_cn_number(j[0])),j[1].center(60-get_cn_number(j[1]))),6)
    status_print('==================================================================================================================',6)

if __name__ == '__main__':
    payload_list_all()