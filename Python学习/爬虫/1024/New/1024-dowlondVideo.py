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
from MysqlHelper import *
import log
import logging


"""
    单线程爬取视频
    author：gengzi
    version：0.0.1.3
    sj：2018年3月10日00:12:30
"""
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
mysql = MysqlHelper(host="123.206.30.117",user="root",passwd="111",db="1024",port=3306)
logger = logging.getLogger("1024")



def selectVideoUrl(params):
    """
    查询指定索引的视频索引
    :param params: 参数list
    :return:
    """
    sql = "select videoname,videoaddress,vid  from huli11 where isdowlond is null  limit %s,%s"
    return mysql.get_all(sql=sql,params=params)

def updateVideo(isdowlond,videofileaddress,videodownloadtime,vid):
    """
    更新下载视频的信息
    :param isdowlond: 是否下载，0 没有下载  1 下载  -1 下载失败
    :param videofileaddress: 视频下载后的地址
    :param videodownloadtime: 视频下载时间
    :param vid: 视频的主键id
    :return: num
    """
    params = [isdowlond,videofileaddress,videodownloadtime,vid]
    sql = "update huli11 set isdowlond= %s ,videofileaddress = %s,videodownloadtime =%s where vid =%s"
    num = mysql.update(sql=sql,params=params)
    if num > 0:
        logger.info(str(vid)+"插入成功")
    else:
        logger.error(str(vid)+"插入失败")

def getNewFormatTime(formatStr):
    """
    返回当前格式后的时间
    :param:formatStr 时间的格式 str
    :return:
    """
    return time.strftime(formatStr,time.localtime(time.time()))


if __name__ == "__main__":
    #根据mysql 查询视频所在的网址
    startitem = 0
    enditem = 999
    params = (startitem,enditem)
    # 先爬取300 条
    videolist = selectVideoUrl(params)
    print videolist
    for video in videolist:
        filname =  video[0]
        videourl =  video[1]
        vid = video[2]
        #下载视频，写入文件中
        try:
            start_time = time.time()
            req = requests.get(videourl, headers=headers, timeout=20)
            spcontent = req.content
            print(unicode(filname.encode('utf-8'), "utf-8"))
            name = unicode(filname.encode('utf-8'), "utf-8")
            # 创建目录
            dir = "H:\\fl01\\new\\" + str(startitem)+"-"+str(enditem)+"\\"
            isExists = os.path.exists(dir)
            # 判断结果
            if not isExists:
                os.makedirs(dir)
                logger.info(dir + ' 创建成功')
            #文件的名字
            name = dir + unicode(filname.encode('utf-8'), "utf-8") + '.mp4'
            with open(name, "wb") as code:
                code.write(spcontent)
            end_time = time.time() - start_time
            logger.info("耗时：" + str(end_time))
            #下载一个视频，将视频的属性写入到mysql数据库中 随后
            updateVideo(isdowlond="1",videofileaddress=name,videodownloadtime=str(getNewFormatTime("%Y-%m-%d %H:%M:%S")),vid=int(vid))
        except Exception, e:
            updateVideo(isdowlond="-1", videofileaddress="---",
                        videodownloadtime=str(getNewFormatTime("%Y-%m-%d %H:%M:%S")), vid=int(vid))
            logger.error(e)
            logger.error(str(vid)+"访问超时")
            continue





































