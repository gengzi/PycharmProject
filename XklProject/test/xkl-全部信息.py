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
def foreachFile():
    #目录
    filepath  ="I:\\python\\xkl\\allnv"
    for filename in os.listdir(filepath):
        try:
            print(filename)
            filecontent = open(filepath+"\\"+filename,"r").read()
            loadJson(filecontent)
        except Exception,e:
            print(e)
            continue


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}


def loadJson(fileContent):
    """
        读取本地文件的json数据，解析出需要下载的文件
    :return:
    """
    jsondata = json.loads(fileContent)
    data = jsonpath.jsonpath(jsondata,"$.data.messageBOs[*]")
    for i  in range(0,len(data)):
        try:
            studentdata = jsonpath.jsonpath(jsondata, "$.data.messageBOs[" + str(i) + "]")
            # id
            studentid = jsonpath.jsonpath(studentdata, "$..studentBO.id")

            if studentid != False:
                with open("I:\\python\\xkl\\allstudent\\studentid.txt","a") as f:
                    f.write(str(studentid[0])+"\n")


        except Exception, e:
            print(e)
            continue


if __name__ == "__main__":
    foreachFile()





