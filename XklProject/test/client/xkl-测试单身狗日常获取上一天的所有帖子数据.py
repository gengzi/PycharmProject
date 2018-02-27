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
import json
import os
import jsonpath
import datetime

"""
    author：gengzi
    version：0.0.1.3
    sj：2018年2月27日23:43:35
"""
headers = {"User-Agent": 'okhttp/3.6.0'}
posturl = "http://120.55.151.61/V2/Treehole/Message/getMessageByTopicIdV5.action"
def postStudent(session,beforTimestamp,afterTimestamp,topicId):
    print("开始的时间戳:"+beforTimestamp)
    print("结束的时间戳:"+afterTimestamp)
    post_url= "http://120.55.151.61/V2/Treehole/Message/getMessageByTopicIdV5.action"
    #
    postdata = {
        "channel":"XiaoMiMarket",
        "genderType":"-1",
        "phoneBrand":"Xiaomi",
        "phoneModel":"HM 2A",
        "phoneVersion":"19",
        "platform":"1",
        "selectType":"0",
        "timestamp":afterTimestamp,
        "topicId":topicId,
        "type":"1",
        "versionNumber":"9.3.1",
    }
    student_response = session.post(url=post_url,headers=headers,data=postdata)
    timestamp = paseJsondata2Timestamp(student_response.text)
    # 休眠10秒，模拟人工操作
    time.sleep(10)
    if int(timestamp) >= 1519574400181:
        postStudent(session,timestamp)
    else:
        return


def paseJsondata2Timestamp(response):
    # 将响应数据写入txt文件
    jsondata = json.loads(response)
    # 解析出来下一次分页的时间戳
    timestampList = jsonpath.jsonpath(jsondata, "$.data.timestampLong")
    #文件名为时间戳.txt
    timestamp = str(timestampList[0])
    filename = timestamp+".txt"
    #目录
    filepath = "H:\\python\\xiakeliao\\2018-2-26\\"+filename
    #先写入文件
    with open(filepath, "w") as code:
        code.write(response)
    return timestamp






def login():
    """
    登陆，返回登陆成功的session
    :return:  session
    """
    try:
        url_login = "http://120.55.151.61/V2/StudentSkip/loginCheckV4.action"
        # 密码和账号都是加密后的
        login_data = {
            "account": "F5169A5DCC50A9DE4EB747493BCD3BCB",
            "channel": "XiaoMiMarket",
            "deviceCode": "868291022946681",
            "password": "07912E33F75EAF6172814A17E2EE0059",
            "phoneBrand": "Xiaomi",
            "phoneModel": "HM 2A",
            "phoneVersion": "19",
            "platform": "1",
            "updateInfo": "false",
            "versionNumber": "9.3.1",
        }
        # 模拟登陆
        session = requests.session()
        session.post(url=url_login, headers=headers, data=login_data)
        # session会携带登陆后的cookie回来
        return session
    except Exception,e:
        print("登陆失败："+e)


def getYesterday(formatStr):
    """
     获取昨天的日期
    :param formatStr: 时间格式
    :return: 年-月-日
    """


    return (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(formatStr)

def getTimeStamp(formateTime):
    """
    获取当前时间的时间戳
    :param formateTime 格式好的时间  %Y-%m-%d %H:%M:%S
    :return: int类型的时间戳
    """
    return int(time.mktime(time.strptime(formateTime, "%Y-%m-%d %H:%M:%S")))

def gettopicIds():
    """
    获取需要抓取的栏目的id
    :return:
    """
    return (19,13,38,41,15)

if __name__ == "__main__":
    # [1]拿到登陆成功的session
    session = login()

    # [2] 抓取昨天发布的全部帖子，一些小的栏目帖子不算
    # 获取上一天的年月日
    yesterday = getYesterday("%Y-%m-%d")
    # 模拟抓取的时间戳
    # 0.0.0 的时间戳  23.59.59 的时间戳
    befor_timestamp = str(yesterday)+" 00:00:00"
    after_timestamp = str(yesterday)+" 23:59:59"
    beforTimestamp = getTimeStamp(befor_timestamp)
    afterTimestamp = getTimeStamp(after_timestamp)
    # 组拼成13位的时间戳
    beforTimestamp = str(beforTimestamp)+"000"
    afterTimestamp = str(afterTimestamp)+"999"
    # 调用请求数据方法
    print(str(yesterday)+"抽取数据开始>>>")

    # [2.1] 将五个模块的数据都抓取出来
    topicIds = gettopicIds()
    for i in topicIds:
        try:
            print("爬取的栏目编号:"+str(i))
            postStudent(session,beforTimestamp,afterTimestamp,str(i))
        except Exception,e:
            print("栏目编号:"+str(i)+"爬取出错")
            continue



