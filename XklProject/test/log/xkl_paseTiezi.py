# -*- coding:utf-8 -*-

import time
import json
import os
import jsonpath
import datetime
import MySQLdb
import log
import logging
from wechat_sender import Sender
from DateUtils import  *
from MysqlHelper import *
from FileUtils import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')


"""
    author：gengzi
    version：0.0.1.3
    sj：2018年2月27日23:43:35
"""

logger = logging.getLogger("xkl")



def paseJsondata2Timestamp(response):
    """
    解析出timestamp
    :param response: 响应的数据
    :return: timestamp
    """
    # 将响应数据写入txt文件
    jsondata = json.loads(response)
    # 解析出来下一次分页的时间戳
    timestampList = jsonpath.jsonpath(jsondata, "$.data.timestampLong")
    #文件名为时间戳.txt
    timestamp = str(timestampList[0])
    filename = timestamp+".txt"
    #目录
    yesterday = getYesterday("%Y-%m-%d")
    # 创建目录
    path = "/home/ubuntu/python_workspace/xiakeliao/tiezidata/"+yesterday+"/"
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path)
        print path + '创建成功'
    filepath = path+filename
    #先写入文件
    with open(filepath, "w") as code:
        code.write(response)
    return timestamp



def insertData(response,formatTime,topicId,timestamp,formatTimeday):
    """
    将数据写入数据库
    :param response: 响应的json数据
    :param formatTime: 年月日时分秒
    :param topicId: 栏目的编号
    :param timestamp: 时间戳
    :param formatTimeday: 年月日
    :return: 是否成功
    """
    try:
        conn = MySQLdb.connect(host="123.206.30.117",port=3306,user="root",passwd="111",db="xklinfo",charset="utf8")
        cursor =conn.cursor()
        # 封装参数
        # 将响应数据中的 unicode
        params = [str(formatTimeday),response,str(timestamp),str(formatTime),str(topicId)]
        #插入
        sql ="insert into messagedata(nowtime,datajson,timestamp,stampdate,topicid) values(%s,%s,%s,%s,%s)"
        count = cursor.execute(sql, params)
        if count >= 1:
            logger.info("插入成功"+getNewFormatTime())
        conn.commit()
    except Exception,e:
        print(e)
    finally:
        cursor.close()
        conn.close()



def parseContentByJSONPATH(content):
    """
    解析content 内容 使用jsonpath
    :param content:  json数据
    :return: Studnet
    """





if __name__ == "__main__":
    # send = Sender()
    # logger.info("<<<<<<<<<<<<<<<<<<<<<<解析帖子数据开始>>>>>>>>>>>>>>>>>>>>>>>>")

    #帖子数据中，有非常多的数据，现在只获取其中的 学生编号，存入sql 文件中， 并去除
    #[1] 读取昨天linux 的本地txt文件
    yesterday = getYesterday("%Y-%m-%d")
    filepaths = foreachPath2file("H:\\python\\ubuntu\\"+yesterday+"\\")
    for filepath in filepaths:
        #读取每一个文件
        with open(filepath) as f:
             content = f.read()
        #解析内容



    #[2] 解析文本

    #[3] 插入数据库中









