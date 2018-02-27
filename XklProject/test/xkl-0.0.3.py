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
url_login = "http://120.55.151.61/V2/StudentSkip/loginCheckV4.action"

def postStudent(studentid):

    url = "http://120.55.151.61/Treehole/V4/Message/showMovement.action"

    xs_url="http://120.55.151.61/Treehole/V4/Message/showMovement.action"

    school_url ="http://120.55.151.61/V2/Student/getIndexInfoById.action"
    # JSON
    # data
    # academyName: "经济系"
    # gender: 0
    # grade: 14
    # professionAndGrade: "经济系 2014级"
    # progress: 65
    # schoolName: "西南财经大学天府学院"
    # status: 1



    url1 ="http://120.55.151.61/Base/V2/Album/getAlbumWallList.action"

    login_data ={
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
    postdata = {
        "timestamp":"1495630881000",
        "phoneBrand":"Xiaomi",
        "platform":"1",
        "phoneBrand":"Xiaomi",
        "studentId":studentid,
        "phoneVersion":"19",
        "channel":"XiaoMiMarket",
        "phoneModel":"HM 2A",
        "versionNumber":"9.3.1",
    }
    # 模拟登陆
    session =requests.session()
    login_response = session.post(url=url_login,headers=headers,data=login_data)
    # print(login_response.text)

    student_response = session.post(url=url,headers=headers,data=postdata)
    print(student_response.text)





if __name__ == "__main__":
   postStudent("11143253")




