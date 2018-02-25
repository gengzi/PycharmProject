#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习

import urllib2
import urllib

def tiebaSpider(url,startPage,endPage):
    for page in range(startPage,endPage+1):
        pagenum = 50 * (page -1)
        urlpn= url+"&pn="+str(pagenum)
        print(urlpn)
        loadPage(url,"page.html")


def loadPage(url,filename):
    pass

def writeFile(html,filename):
    pass


# 模拟一个main 函数
if __name__ == "__main__":
    """
        爬取百度贴吧的网页内容
    """
#    用户输入需要爬取的吧名，开始页码，结束页码
tiebaname =raw_input("请输入爬取贴吧的名字：")
startPage=int(input("请输入爬取的开始页码："))
endPage=int(input("请输入爬取的结束页码："))
url = "https://tieba.baidu.com/f?"
data = {"kw":tiebaname}
url = url+ urllib.urlencode(data)
print(url)
#    爬取网页
tiebaSpider(url,startPage,endPage)

#    存放到本地磁盘






