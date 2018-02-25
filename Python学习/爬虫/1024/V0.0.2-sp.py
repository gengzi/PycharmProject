#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言


import re
import urllib
import urllib2
import json
# 使用 lxml 的 etree 库
from lxml import etree
import uuid
"""
    单线程爬取视频
    author：gengzi
    version：0.0.1.3
    sj：2018年2月11日23:30:36
"""


def loadPage(url):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
    headers = {'User-Agent': user_agent}
    req = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(req)
    # 读取页面源码
    html = response.read()
    print(html)
    videoformat = r'(?s)<script>var VideoInfoList="mp4\$\$mp4\$(.*?)/\$mp4"</script>'
    videos = re.compile(videoformat)
    content = videos.findall(html)
    print(content)
    for videourl in content:
        req1 = urllib2.Request(videourl, headers=headers)
        f = urllib2.urlopen(req1)
        data = f.read()
        name = "H:\\python\\sp\\httpss94ss.com\\"+str(uuid.uuid1())+'.mp4'
        with open(name, "wb") as code:
            code.write(data)

    print("end")


if __name__ == "__main__":
    # 循环遍历拿到每一个分页的文章链接
    for i in range(20,30):
        urllist = "http://ss94ss.com/list/?5-"+str(i)+".html"
        user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0'
        headers = {'User-Agent': user_agent}
        req = urllib2.Request(urllist, headers=headers)
        response = urllib2.urlopen(req)
        html = response.read()
        #使用xpath 解析页面
        # 利用etree.HTML，将字符串解析为HTML文档!
        formatHtml = etree.HTML(html)
        doc_a = formatHtml.xpath('//div[@class="well well-sm"]/a/@href')
        print(doc_a)
        for a in doc_a:
            try:
                print("http://ss94ss.com"+str(a))
                loadPage("http://ss94ss.com"+str(a))
            except Exception, e:
                print(e)
                continue


