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
# headers
headers = {"User-Agent": 'okhttp/3.6.0'}
# 四个url
# 获取个人签名等信息
getTopinfourl = "http://120.55.151.61/V2/Student/getTopInfoById.action"
# 获取她发布的信息
showMovement = "http://120.55.151.61/Treehole/V4/Message/showMovement.action"
# 获取学院等信息
getIndexInfoById = "http://120.55.151.61/V2/Student/getIndexInfoById.action"
# 获取设置的照片
getAlbumWallList = "http://120.55.151.61/Base/V2/Album/getAlbumWallList.action"
# 获取出生年月
getInfoByIdV4 = "http://120.55.151.61/V2/Student/getInfoByIdV4.action"



def foreachFile(loginSession):
    #目录
    filepath  ="I:\\python\\xkl\\allstudent\\studentid.txt"
    with open(filepath,"r") as f:
        linesData = f.readlines()
        for line in range(0,len(linesData)):
            try:
                # 获取studentid 并去除换行
                studentid = linesData[line].rstrip("\n")
                print("第"+str(line)+"个"+"学生id："+studentid)
                loadStrduentInfo(str(studentid),loginSession)
            except Exception,e:
                print(e)
                continue


def login():
    url_login = "http://120.55.151.61/V2/StudentSkip/loginCheckV4.action"
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
    return session

def loadStrduentInfo(studentid,loginSession):
    """
        加载这个studentid 的四个url
    :param studentid:  编号
    :return: txt
    """
    #getTopInfoById
    getTopInfoByid_data={
        "channel":"XiaoMiMarket",
        "phoneBrand":"Xiaomi",
        "phoneModel":"HM 2A",
        "phoneVersion":"19",
        "platform":"1",
        "studentId":studentid,
        "versionNumber":"9.3.1",
    }
    #getIndexInfoById
    getIndexInfoById_data =  getTopInfoByid_data
    getAlbumWallList_data =  getTopInfoByid_data
    getInfoByIdV4_data = getTopInfoByid_data

    # 开始访问
    getTopInfoByid_res = loginSession.post(url=getTopinfourl,headers=headers,data=getTopInfoByid_data)
    getIndexInfoById_res = loginSession.post(url=getIndexInfoById,headers=headers,data=getTopInfoByid_data)
    getAlbumWallList_res = loginSession.post(url=getAlbumWallList,headers=headers,data=getTopInfoByid_data)
    getInfoByIdV4_res = loginSession.post(url=getInfoByIdV4,headers=headers,data=getTopInfoByid_data)

    Jsondata = {
        "topInfo":getTopInfoByid_res.text,
        "indexInfo":getIndexInfoById_res.text,
        "albumWallList":getAlbumWallList_res.text,
        "InfoByIdV4":getInfoByIdV4_res.text,
    }
    # 写入文件中
    filename =  "I:\\python\\xkl\\allstudent\\info\\"+studentid+".txt"
    with open(filename,"w") as f:
        f.write(json.dumps(Jsondata))
    print("一般信息："+filename)
    timestamp = "0"
    dowloadPage(studentid,loginSession,timestamp)



def dowloadPage(studentid,loginSession,timestamp):

    # 单独处理
    # showMovement
    showMovement_data = {
        "channel": "XiaoMiMarket",
        "phoneBrand": "Xiaomi",
        "phoneModel": "HM 2A",
        "phoneVersion": "19",
        "platform": "1",
        "studentId": studentid,
        "timestamp": timestamp,
        "versionNumber": "9.3.1",
    }
    showMovement_res = loginSession.post(url=showMovement,headers=headers,data=showMovement_data)
    jsondata = json.loads(showMovement_res.text)
    # 解析出来下一次分页的时间戳
    timestampList = jsonpath.jsonpath(jsondata, "$.data.timestampLong")
    # 判断hasMore 为 true 就有，fasle 就没有
    hasMore = jsonpath.jsonpath(jsondata, "$.data.hasMore")
    # 写入到文件中
    # 文件名为时间戳.txt
    timestamp = str(timestampList[0])
    filename = studentid+"_"+timestamp + ".txt"
    # 目录
    filepath = "I:\\python\\xkl\\allstudent\\info\\" + filename
    # 先写入文件
    with open(filepath, "w") as code:
        code.write(showMovement_res.text)
    print("列表信息："+filename)
    print("是否为："+str(hasMore[0]).strip())
    if str(hasMore[0]).strip() == "True":
        print("执行列表信息")
        dowloadPage(studentid,loginSession,str(timestamp))



if __name__ == "__main__":
    loginSession = login()
    foreachFile(loginSession)





