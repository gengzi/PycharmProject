#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言


import re
import urllib
import urllib2
"""
    目的：使用正则表达式对csdn爬取博客数据
        版本1 ：最终效果：
                  （0）模拟登陆csdn网站
                  （1）自动爬取用户所关注的csdn用户
                  （2）自动爬取关注用户的所有文章页面，并对每一篇文章的必要数据解析
                  （3）将所爬取的文章信息，存放到数据库
                  （4）将数据库的内容，生成对应的html文件，展示
    author：gengzi
    version：0.0.1
            实现对一篇文章页面的，标题，文章编写时间，文章内容等的爬取
    sj：2018年1月18日15:49:25
"""


def loadPage():
    """
        实现对一个页面的csdn页面文章的必要数据爬取
    :return:
    """
    # 爬取csdn博客页面的url
    url = "http://blog.csdn.net/qq_28817739/article/details/78162552"
    # url = "http://blog.csdn.net/qq_28817739/article/details/79041192"
    #构造User-Agent头
    user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0'
    headers = {'User-Agent': user_agent}
    req = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(req)
    # 读取页面源码
    html = response.read()
    # 存放解析页面的数据
    boke ={}
    # print html
    # ---------------------------------阅读人数
    # 将正则表达式编译成 Pattern 对象
    pattern = re.compile(r"<span .*? title=\"阅读次数\">(.*?)人阅读</span>")
    # findall 返回是一个列表
    # 博客的阅读人数
    loadNum = pattern.findall(html)
    boke["loadNum"] = loadNum[0]
    # ---------------------------------文章的标题
    str = "(?s)<a href=\"\\S*\">\\s+.*</font>\\s+(.*?)\\s+</a>"
    pattern = re.compile(str)
    title = pattern.findall(html)
    # 第一种：是置顶的文章
    if len(title) >0:
        for item in title:
            boke["title"] = item
            # print(item)
    # 第二种：没有置顶的文章
    else:
        str = "(?s)<a href=\"\\S*\">\\s+\\s+(.*?)\\s+</a>"
        pattern = re.compile(str)
        title = pattern.findall(html)
        for item in title:
            boke["title"] = item
            # print(item)

    # ---------------------------------博客的创建时间
    strCrate_date = r"<span class=\"link_postdate\">(.*?)</span>"
    pattern = re.compile(strCrate_date)
    crate_date = pattern.findall(html)
    boke["crate_date"] = crate_date[0]
    # ---------------------------------文章的内容
    str_content = r"(?s)<div id=\"article_content\".*?>(.*?)</div>";
    pattern = re.compile(str_content)
    content = pattern.findall(html)
    boke["content"] = content[0]

    # 遍历打印boke字典中存放的数据
    for name,value in boke.iteritems():
        print(name+":"+value)
    # print(boke)

# 加载页面的方法
loadPage()