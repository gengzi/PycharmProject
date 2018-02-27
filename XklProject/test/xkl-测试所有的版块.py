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

def postStudent(session,topicId):
        print(topicId)
        post_url= "http://120.55.151.61/V2/Treehole/Message/getMessageByTopicIdV5.action"

        postdata = {
            "channel":"XiaoMiMarket",
            "genderType":"-1",
            "phoneBrand":"Xiaomi",
            "phoneModel":"HM 2A",
            "phoneVersion":"19",
            "platform":"1",
            "selectType":"0",
            "timestamp":"0",
            "topicId":topicId,
            "type":"1",
            "versionNumber":"9.3.1",
        }
        student_response = session.post(url=post_url,headers=headers,data=postdata)
        print(student_response.text)
        # 休眠10秒，模拟人工操作
        time.sleep(1)










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
    for i in range(1,100):
        try:
            postStudent(session,str(i))
        except Exception,e:
            print(e)
            continue





