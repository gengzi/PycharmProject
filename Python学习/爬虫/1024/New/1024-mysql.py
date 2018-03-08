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
import logging
import log
from MysqlHelper import *

logger = logging.getLogger("1024")
# 初始化mysql
mysql = MysqlHelper(host="123.206.30.117",user="root",passwd="111",db="1024",port=3306)
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def getNewFormatTime(formatStr):
    """
    返回当前格式后的时间
    :param:formatStr 时间的格式 str
    :return:
    """
    return time.strftime(formatStr,time.localtime(time.time()))


def insert1024(params):
    sql = "insert into huli11(host,videoname,videoaddress,createtime) values(%s,%s,%s,%s)"
    num = mysql.insert(sql=sql,params=params)
    if num >0:
        logger.info("成功插入"+str(params[2]))
    else:
        logger.error("插入失败"+str(params[2]))



def loadPage(url,filname,ym):
    response = requests.get(url,headers=headers,timeout=8)
    html = response.text
    videoformat = r'(?s)<script>var VideoInfoList="mp4\$\$mp4\$(.*?)/\$mp4"</script>'
    videos = re.compile(videoformat)
    content = videos.findall(html)
    for videourl in content:
        #将数据插入到库中
        logger.info("视频的地址:"+videourl)
        host = str(url) #视频所在的网页地址
        videoname = str(filname) #视频的名称
        videoaddress = str(videourl) #视频的网址
        createtime = getNewFormatTime("%Y-%m-%d %H:%M:%S") #现在的时刻
        params = [host,videoname,videoaddress,str(createtime)]
        insert1024(params)


def getAllPageNum(path):
    """
    获取该网站的分页数
    :return:
    """
    response = requests.get(url=path,headers=headers)
    html = response.text
    #使用xpath解析
    formatHtml = etree.HTML(html)
    # 加上一个 text() 来获取文本值
    startpage = formatHtml.xpath('//div[@class="nav-links"]/span[@class="page-numbers current"]/text()')
    endpages = formatHtml.xpath('//div[@class="nav-links"]/a[@class="page-numbers"]/text()')
    endpage = endpages[len(endpages)-1]
    logger.info("开始页码:"+str(startpage[0])+";结束页码:"+str(endpage))
    return endpage




def loadUrl(num):
    # 根据num组拼网址
    for numint in range(1,int(num)+1):
        logger.info("当前查询第"+str(numint)+"页")
        urllist = "http://huli11.info/content/index4-"+str(numint)+".html"
        response = requests.get(urllist, headers=headers)
        html = response.text
        # 使用xpath 解析页面
        formatHtml = etree.HTML(html)
        doc_a = formatHtml.xpath('//li[@class="i_list list_n1"]/a/@href')
        doc_title = formatHtml.xpath('//li[@class="i_list list_n1"]/a/@title')
        for index, a in enumerate(doc_a):
            try:
                logger.info("现在访问的视频是" + doc_title[index] + "；网址：http://huli11.info" + str(a))
                loadPage("http://huli11.info" + str(a), doc_title[index],num)
                time.sleep(10)
            except Exception, e:
                print(e)
                continue



if __name__ == "__main__":
    # 获取全部的页数
    path = "http://huli11.info/content/index4.html"
    num = getAllPageNum(path)
    loadUrl(num)







