#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言


import re
import urllib
import urllib2
import cookielib
from lxml import etree
"""
    目的：使用正则表达式对csdn爬取博客数据
        版本1 ：最终效果：
                  （0）模拟登陆csdn网站
                  （1）自动爬取用户所关注的csdn用户
                  （2）自动爬取关注用户的所有文章页面，并对每一篇文章的必要数据解析
                  （3）将所爬取的文章信息，存放到数据库
                  （4）将数据库的内容，生成对应的html文件，展示
    author：gengzi
    version：0.0.2
        实现模拟登陆csdn网站
    sj：2018年1月20日18:37:26
"""


# "gps":""
# "username":"17839166574"
# "password":"123456"
# "rememberMe":"true"
# lt:LT-1783043-6m7aFRJes7RZSCo2fdFSFU0XCucwgS
# "execution":"e2s1_eventId"
# "submit":""


def login_CSDN(username,password):
    """
           作用：模拟登陆csdn
    :param username: 用户名
    :param password: 密码
    :return: 登陆成功后的页面
    """
    # 1, 构建一个CookieJar对象实例来保存cookie

    handers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
    cookie = cookielib.CookieJar()

    cook_Handler=urllib2.HTTPCookieProcessor()

    opener =urllib2.build_opener(cook_Handler)
    opener.add_handler = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")]

    # 先访问一次，获取it 和 ex
    login_url ="https://passport.csdn.net/account/login"
    response = opener.open(login_url)
    html  = response.read()

    # 解析html 为 HTML 文档
    selector = etree.HTML(html)

    # 抓取当前页面的所有帖子的url的后半部分，也就是帖子编号
    # http://tieba.baidu.com/p/4884069807里的 “p/4884069807”
    it = selector.xpath('//div[@class="user-pass"]/form/input[@name="lt"]/@value')
    ex = selector.xpath('//div[@class="user-pass"]/form/input[@name="execution"]/@value')

    print("it:"+str(it))
    print("ex:"+str(ex))

    opener.add_handler = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")]

    url="https://passport.csdn.net/account/verify"

    formdate = {
        "gps":"",
        "username":"17839166574",
        "password":"songmengke.521",
        "rememberMe":"true",
         "lt":str(it[0]),
         "execution":str(ex[0]),
         "_eventId":"submit"
    }
    data=urllib.urlencode(formdate)

    request =urllib2.Request(url,data= data)

    opener.open(request)

    response = opener.open("http://blog.csdn.net/dushimou/article/details/74898025")
    # 10. 打印响应内容
    html_content =response.read()

    print(html_content)


login_CSDN("17839166574","songmengke.521")