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
import csv

#列表打印装饰器
def Print_info(fun):
    def work(*args,**kwargs):
        res=fun(*args, **kwargs)
        if res:
            if isinstance(res, str):
                print(res)
            elif isinstance(res, list):
                for i in res:
                    print(i.replace('\n',''))
            else:
                pass
        return fun(*args, **kwargs)
    return work

# 结果导出装饰器
# 保存文件类型为.rabbit，因为我不希望这个结果被记事本草率地打开，
# 因为可能会乱，/哭唧唧，推荐notepad++、SublimeText、VScode等。

def Save_info(fun):
    def work(*args,**kwargs):
        result=(fun(*args, **kwargs))
        if result:
            timetoken = datetime.datetime.now().strftime('%Y%m%d%H%M%S');
            filename='Output/{}_result_{}.rabbit'.format(fun.__name__,timetoken)
            for i in result:
                try:
                    fw = open(filename, 'a')
                    fw.write(i.replace('\n','') + '\n')
                    fw.close()
                except:
                    pass
            print('结果已保存至：'+filename)
        # return fun(*args, **kwargs)
    return work



def Save_Csv(fun):
    def work(*args,**kwargs):
        result=(fun(*args, **kwargs))
        if result:
            timetoken = datetime.datetime.now().strftime('%Y%m%d%H%M%S');
            filename='Output/{}_result_{}.csv'.format(fun.__name__,timetoken)
            with open(filename, 'a',encoding='utf-8',newline='') as f:
                head = ['host','ip','port','country','city','server','title']
                writer = csv.writer(f)
                # 写入一行数据
                writer.writerow(head)
                # 写入多行数据
                for i in result:
                    writer.writerow(list(i.values()))
            print('结果已保存至：'+filename)
        # return fun(*args, **kwargs)
    return work
