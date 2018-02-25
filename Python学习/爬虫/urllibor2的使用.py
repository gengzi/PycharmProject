#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言

#------------------------------
# # 下载知乎首页
# import  urllib2
# # 请求# 响应
# url = "http://www.zhihu.com/"
# response_html = urllib2.urlopen(url)
# html = response_html.read()
# print(html)
#------------------------------

#------------------------------
# # 使用 urlopen 不能修改 user-agent （浏览器的标识）
# # 可以使用提供的requests
# import urllib2
# # 请求
# from pip._vendor.requests import request
# url = "http://www.zhihu.com/"
# request =urllib2.Request(url)
# # 响应
# reponse_html = urllib2.urlopen(request)
# html = reponse_html.read()
# print(html)
#------------------------------


#------------------------------
# # post请求
# import urllib2
# import urllib
#
# # 封装请求参数
# url = "https://www.zhihu.com/api/v3/oauth/sign_in"
# postdata={"username":"+8617839166574","password":"songemngele...."}
# # 转码
# data = urllib.urlencode(postdata)
# # 请求
# request = urllib2.Request(url,data)
# reponse=urllib2.urlopen(request)
# print(reponse.read())

# post请求
# import urllib2
# import urllib
#
# # 封装请求参数
# url = "https://www.zhihu.com/api/v3/oauth/sign_in"
# user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
# referer ="https://www.zhihu.com/signup"
# postdata={"username":"+8617839166574","password":"songemngele...."}
# headers={"User-Agent":user_agent,"Referer":referer}
# # 转码
# data = urllib.urlencode(postdata)
# # 请求
# request = urllib2.Request(url,data,headers)
# reponse= urllib2.urlopen(request)
# print(reponse.read())
#------------------------------

#------------------------------
# # cookie的处理
# import urllib2
# import cookielib
# url = "https://www.zhihu.com/"
# cookie=cookielib.CookieJar()  #用于存储cookie对象，此模块捕获cookie并在后续连接请教时重新发送，还可以用来处理包含cookie数据文件
# print(cookie)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# reponse = opener.open(url)
# for item in cookie:
#     print(item.name+":"+item.value)
# alt+1 打开project 窗口


#自定义cookie
import urllib2
url = "https://www.zhihu.com/"

opener =urllib2.build_opener()
opener.addheaders.append(("Cookie","email="+"xxxx163.com"))
req=urllib2.Request(url)
response=opener.open(req)
print(response.headers)
retdata = response.read()






#------------------------------



