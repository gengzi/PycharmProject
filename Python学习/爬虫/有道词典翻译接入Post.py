#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习


import urllib
import urllib2

# 组拼一个post 请求
# 头信息
# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    # "Cookie":"_ntes_nnid=ff0a3a1310ba27d0bfe96dab00a42ada,1514020462210; OUTFOX_SEARCH_USER_ID_NCOO=1769872124.6754887; OUTFOX_SEARCH_USER_ID=1983567464@61.51.95.202; JSESSIONID=aaarvE636wrCdgcOd7cew; fanyi-ad-id=39535; fanyi-ad-closed=1; ___rl__test__cookies=1516172686204"
}
# 提交的字段信息
formdata ={
    "i":"love",
    "from":	"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb" ,
    # "salt":"1514020462210",
    # "sign":"9142113e52f9042c4652bd8a705fb478",
    "doctype":"json",
     "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_CLICKBUTTION",
    "typoResult":"true"
}

formdatas = urllib.urlencode(formdata)
request = urllib2.Request(url,data=formdatas,headers=headers)
print(urllib2.urlopen(request).read())