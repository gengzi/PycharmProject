#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习

# 添加更多的Header信息
# 构造一个完成的url请求


import urllib2
import urllib


# 请求的url地址
url = "http://www.baidu.com/" #加上这个 / 表示走根目录
# 添加header头信息 是一个字典形式
headers = {
    "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
}
# 请求,添加一个头信息
request = urllib2.Request(url,headers = headers)
# 响应
print(urllib2.urlopen(request).read())

# 可以通过 request.add_header() 来添加 headers 的头信息，通过 get_header()
#  response.code 可以查看响应的状态码
