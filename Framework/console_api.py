#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
'''
 ____       _     _     _ _   __  __           _    
|  _ \ __ _| |__ | |__ (_) |_|  \/  | __ _ ___| | __
| |_) / _` | '_ \| '_ \| | __| |\/| |/ _` / __| |/ /
|  _ < (_| | |_) | |_) | | |_| |  | | (_| \__ \   < 
|_| \_\__,_|_.__/|_.__/|_|\__|_|  |_|\__,_|___/_|\_\
                                                    
'''
# from time import sleep
# from Tools.ReBuild import Rebuild
#
# Rebuild()
# sleep(3)

from Config.config_banner import Banner
from flask import Flask
from gevent import pywsgi
from flask import request

from Config.config_print import status_print
from Framework.console_attack import run_poc_api
from Tools.ReBuild import get_moudle, get_payload

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'A Lovely Gift From WingsSec'

#
@app.route('/api', methods=['GET'])
def api():
    try:
        poc = request.args.get('poc')
        target = request.args.get('target')
        data = run_poc_api(poc, target)
        if data:
            res =  {'msg':'success','data':data}
        else:
            res = {'msg': 'fail', 'data':'NULL'}
        return res
    except:
        return 'Usage:<br>&emsp;&emsp;&emsp;&emsp;/api?poc=Test&target=http://127.0.0.1'


@app.route('/list', methods=['GET'])
def list():
    res= {}
    moudles = get_moudle()
    for i in moudles:
        res[i]=get_payload(i)
    return res

def run(port=1988):
    status_print('服务已启动：'+'0.0.0.0:'+str(port))
    server = pywsgi.WSGIServer(('0.0.0.0', port), app)
    server.serve_forever()

if __name__ == '__main__':
    Banner()
    app.run(host='0.0.0.0', port=1988, debug=False)
