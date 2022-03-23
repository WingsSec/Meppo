# Meppo
漏洞利用框架 Meppo | By WingsSec

### Version
##### V1.1 `2022-03-23`

```angular2html
python Meppo.py    

    __  ___                     
   /  |/  /__  ____  ____  ____ 
  / /|_/ / _ \/ __ \/ __ \/ __ \
 / /  / /  __/ /_/ / /_/ / /_/ /
/_/  /_/\___/ .___/ .___/\____/ 
           /_/   /_/            

                漏洞检测框架 Meppo | By WingsSec | V 1.1
                  [  26 MOUDLES          55 PAYLOADS ]
Usage:
        python Meppo.py -l                              List All Moudles
        python Meppo.py -ll                             List All Payloads
        python Meppo.py -m xxx -l                       List Payload Of The Moudle
        python Meppo.py -poc xxx -u target              单目标 单POC监测
        python Meppo.py -poc xxx -f targets.txt         多目标 单POC监测
        python Meppo.py -m xxx -u target                单目标 模块监测
        python Meppo.py -m xxx -f targets.txt           多目标 模块监测
        python Meppo.py -fofa APP="DEMO"                FOFA API 报告导出 num默认1000
        python Meppo.py -fofa APP="DEMO" -num 100       FOFA API 报告导出 自定义数量

```
```angular2html
python Meppo.py -h

    __  ___                     
   /  |/  /__  ____  ____  ____ 
  / /|_/ / _ \/ __ \/ __ \/ __ \
 / /  / /  __/ /_/ / /_/ / /_/ /
/_/  /_/\___/ .___/ .___/\____/ 
           /_/   /_/            

                漏洞检测框架 Meppo | By WingsSec | V 1.1
                  [  26 MOUDLES          55 PAYLOADS ]
usage: Meppo.py [-h] [-l] [-ll] [-m MOUDLE] [-u URL] [-f FILE] [-poc POC] [-fofa FOFA] [-num NUM]

options:
  -h, --help  show this help message and exit
  -l          list
  -ll         list all
  -m MOUDLE   moudle
  -u URL      target url
  -f FILE     the file of target list

漏洞检测模块:
  -poc POC    漏洞检测

资产爬取模块:
  -fofa FOFA  资产爬取
  -num NUM    资产数量
```