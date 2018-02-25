                                                                                                                                                                                                                             #!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言
import re
import random
import requests
import uuid
import json
from Queue import Queue
import threading
import time
# 使用 lxml 的 etree 库
from lxml import etree

"""
    单线程爬取视频  // 修改为多线程爬虫 // 使用代理
    author：gengzi
    version：0.0.1.3
    sj：2018年2月13日13:00:54
"""
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}


# class thread_load(threading.Thread):
#     """
#         读取数据线程类
#     """
#     def __int__(self):
#         pass
#
#     def run(self):
#         pass





def loadPage(url,filname):
    response = requests.get(url,headers=headers)
    html = response.text
    videoformat = r'(?s)<script>var VideoInfoList="mp4\$\$mp4\$(.*?)/\$mp4"</script>'
    videos = re.compile(videoformat)
    content = videos.findall(html)
    print(content)
    for videourl in content:
        try:
            start_time = time.time()
            req = requests.get(videourl,headers=headers,timeout=10)
            spcontent = req.content
            print(unicode(filname.encode('utf-8'),"utf-8"))
            name = unicode(filname.encode('utf-8'), "utf-8")
            name = "H:\\python\\sp\\httpss94ss.com\\"+unicode(filname.encode('utf-8'),"utf-8")+'.mp4'
            with open(name, "wb") as code:
                code.write(spcontent)
            end_time = time.time() - start_time
            print("耗时："+str(end_time))
        except Exception, e:
            print(e)
            continue

    print("end")


# def loadProxies():
#     """
#     url http://www.xicidaili.com/ 提供代理ip 的网站
#         获取免费的代理ip
#     :return: 代理ip
#     """
#     # 1,请求提供代理ip 的网站
#     url = "http://www.xicidaili.com/"
#     response = requests.get(url,headers=headers)
#     proxiesContent = response.text
#     # 2，获取代理ip和端口号
#     formatContent = etree.HTML(proxiesContent)
#     #proxieIps = formatContent.xpath('//tr/td')
#     proxieIps = formatContent.xpath('//tr/td[2]')
#     proxiePorts = formatContent.xpath('//tr/td[3]')
#     proxies = []
#     for index,item in enumerate(proxieIps):
#         proxies.append("http://"+item.text+":"+proxiePorts[index].text)
#
#     #产生一个随机数
#     return proxies[random.randint(0,20)]


def loadUrl():
    # 循环遍历拿到每一个分页的文章链接
    for i in range(150, 153):
        # urllist = "http://ss94ss.com/list/?5-"+str(i)+".html"
        print("第" + str(i) + "页")
        urllist = "http://huli11.info/content/index5-" + str(i) + ".html"
        # proxie = loadProxies()
        # pro = {"http": proxie}
        # print pro
        # response = requests.get("http://www.baidu.com",headers=headers,proxies = pro)
        response = requests.get(urllist, headers=headers)
        html = response.text
        # 使用xpath 解析页面
        # 利用etree.HTML，将字符串解析为HTML文档!
        formatHtml = etree.HTML(html)
        doc_a = formatHtml.xpath('//li[@class="i_list list_n1"]/a/@href')
        doc_title = formatHtml.xpath('//li[@class="i_list list_n1"]/a/@title')
        for index, a in enumerate(doc_a):
            try:
                print(a)
                print("现在下载的视频是" + doc_title[index] + "；网址：http://huli11.info" + str(a))
                filelog = open("H:\\python\\sp\\httpss94ss.com\\log.txt","a")
                filelog.write("现在下载的视频是" + doc_title[index] + "；网址：http://huli11.info" + str(a))
                filelog.flush()
                loadPage("http://huli11.info" + str(a), doc_title[index])
            except Exception, e:
                print(e)
                continue


if __name__ == "__main__":
    loadUrl()





