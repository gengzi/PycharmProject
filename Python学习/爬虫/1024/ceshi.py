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
import os

"""
    单线程爬取视频  // 修改为多线程爬虫 // 使用代理
    author：gengzi
    version：0.0.1.3
    sj：2018年2月13日13:00:54
"""
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def loadPage(url,name):
        try:
            start_time = time.time()
            req = requests.get(url,headers=headers,timeout=100000)
            spcontent = req.content
            name = unicode(name.encode('utf-8'), "utf-8")
            name = "I:\\python\\sp\\"+name+".mp4"
            with open(name, "wb") as code:
                code.write(spcontent)
            end_time = time.time() - start_time
            print("耗时："+str(end_time))
        except Exception, e:
            print(e)
        print("end")

def loadPagePost(url, name):
        try:
            start_time = time.time()
            req = requests.post(url, headers=headers, timeout=10,verify = False)
            spcontent = req.content
            name = unicode(name.encode('utf-8'), "utf-8")
            name = "I:\\python\\sp\\" + name + ".mp4"
            with open(name, "wb") as code:
                code.write(spcontent)
            end_time = time.time() - start_time
            print("耗时：" + str(end_time))
        except Exception, e:
            print(e)
        print("end")



def load(url):
    req = requests.get(url, headers=headers, timeout=10,verify = False)
    print req.text



if __name__ == "__main__":
    url="http://vo12.top/mp4/17986.mp4?vkey=r0HCl_4RRhKSSQ_KBZiLxA&tm=1519142666"
    name ="饥渴"
    loadPage(url,name)
    # url="https://v.dyzy9.com/20180209/1fEH955K/mp4/1fEH955K.mp4"
    # name ="222"
    # loadPagePost(url,name)

    # load("http://v.dyzy9.com/share/1FJlOWpc4C1y8CCg")





