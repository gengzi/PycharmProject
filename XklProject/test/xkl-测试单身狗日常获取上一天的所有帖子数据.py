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

"""
    模拟请求一个学生的id，获取主页信息
    author：gengzi
    version：0.0.1.3
    sj：2018年2月13日13:00:54
"""
headers = {"User-Agent": 'okhttp/3.6.0'}

def postStudent(session,timestamp):
    print(timestamp)
    post_url= "http://120.55.151.61/V2/Treehole/Message/getMessageByTopicIdV5.action"

    postdata = {
        "channel":"XiaoMiMarket",
        "genderType":"-1",
        "phoneBrand":"Xiaomi",
        "phoneModel":"HM 2A",
        "phoneVersion":"19",
        "platform":"1",
        "selectType":"0",
        "timestamp":timestamp,
        "topicId":"19",
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



if __name__ == "__main__":
    # 拿到登陆成功的session
    session = login()
    # 开始的时间
    postStudent(session,"1519660799999")




