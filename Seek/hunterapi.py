import base64
import datetime
from time import sleep

import requests
from Config.config_api import HUNTER_USERNAME, HUNTER_API_KEY
from Config.config_decorators import Save_Csv
from Config.config_print import status_print

start_time=((datetime.datetime.now() - datetime.timedelta(365)).strftime("%Y-%m-%d %H:%M:%S"))
end_time=(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def huntersearch(keyword,page,size):
    reslist=[]
    bkeyword = bytes(keyword, encoding="utf8")
    bs64 = base64.urlsafe_b64encode(bkeyword)
    bs64 = bs64.decode()
    res=requests.get('https://hunter.qianxin.com/openApi/search?username={}&api-key={}&search={}&page={}&page_size={}&is_web=1&start_time={}&end_time={}'.format(HUNTER_USERNAME,HUNTER_API_KEY,bs64,str(page),str(size),start_time,end_time))
    result = res.json()['data']
    for i in result['arr']:
        dic = {}
        dic['host'] = i['url']
        dic['ip'] = i['ip']
        dic['port'] = i['port']
        dic['country'] = i['country']
        dic['city'] = i['city']
        server=''
        try:
            for j in i['component']:
                server=server+j['name']+" : "+j['version']+'\t'
        except:
            pass
        dic['server'] = server
        dic['title'] = i['web_title']
        reslist.append(dic)
        print(dic)

    consume_quota=result['consume_quota']
    rest_quota=result['rest_quota']
    status_print(consume_quota +'\t'+rest_quota,0)
    return reslist,result['total']

def hunterapi(keyword,num):
    reslist=[]
    if int(num)<= 100:
        reslist = reslist + huntersearch(keyword,1,num)[0]
    else:
        a,b=huntersearch(keyword, 1, 100)
        reslist = reslist + a


        tmp=int(b) // 100
        if tmp == 0:
            pages = (int(b) // 100)
        else:
            pages = (int(b) // 100) + 1
        tmp=int(num) % 100
        if tmp == 0 :
            needpage = (int(num) // 100)
        else:
            needpage = (int(num) // 100) + 1
        sleep(3)
        for i in range(pages):

            if i + 2 > needpage:
                break
            sleep(3)
            reslist = reslist + huntersearch(keyword, i + 2,100)[0]
    return reslist

@Save_Csv
def run(keyword,num):
    return hunterapi(keyword,num)

if __name__ == '__main__':
    (hunterapi('title="北京"',1))