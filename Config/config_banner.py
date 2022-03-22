#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   <
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
'''
import random

from Moudle.Moudle_index import PAYLOAD_NUM, MOUDLE_NUM

Version = 'V 1.0'
info = '\n\t\t漏洞利用框架 Meppo | By WingsSec | {}\n'.format(Version)
NUM='\t\t  [ {} MOUDLES\t\t{} PAYLOADS ]'.format(str(MOUDLE_NUM).center(3),str(PAYLOAD_NUM).center(3))

banner1 = r'''
  __  __                        
 |  \/  | ___ _ __  _ __   ___  
 | |\/| |/ _ \ '_ \| '_ \ / _ \ 
 | |  | |  __/ |_) | |_) | (_) |
 |_|  |_|\___| .__/| .__/ \___/ 
             |_|   |_|                                                                                    
{}{}'''.format(info,NUM)

banner2 = r'''          
   _____                               
  /     \   ____ ______ ______   ____  
 /  \ /  \_/ __ \\____ \\____ \ /  _ \ 
/    Y    \  ___/|  |_> >  |_> >  <_> )
\____|__  /\___  >   __/|   __/ \____/ 
        \/     \/|__|   |__|                                                                                                                                                  
{}{}'''.format(info,NUM)

banner3 = r'''
    __  ___                     
   /  |/  /__  ____  ____  ____ 
  / /|_/ / _ \/ __ \/ __ \/ __ \
 / /  / /  __/ /_/ / /_/ / /_/ /
/_/  /_/\___/ .___/ .___/\____/ 
           /_/   /_/            
{}{}'''.format(info,NUM)

bannerlist = [banner1, banner2, banner3]


def Banner():
    print(bannerlist[random.randrange(len(bannerlist))])


if __name__ == '__main__':
    Banner()
