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

import json




# if __name__ == "__main__":
      # info={'name':'Tom',
      #       'age':'12',
      #       'job':'work',}
      # f=open('I:\\python\\xkl\\allstudent\\file1.txt','w')
      # f.write(json.dumps(info))
      # f.close()
     # if "False" == "True":
     #       print("11")

import os
import sys


# def search(path, word):
#       for filename in os.listdir(path):
#             # 遍历所有的文件
#             fp = os.path.join(path, filename)
#             # 判断 word 是否在文件名中
#             if os.path.isfile(fp) and word in filename:
#                   print fp
#             #没有，递归循环到子目录中
#             elif os.path.isdir(fp):
#                   search(fp, word)
#
#
# search("I:\\python\\xkl\\allstudent\\info\\", "28646108")


# dirname = "I:\\python\\xkl\\allstudent\\allinfo\\\u5f90\u5dde\u533b\u79d1\u5927\u5b66"+u"\t-"
# print(dirname)

# def foreachFile():
#     #目录
#     filepath  ="I:\\python\\xkl\\allstudent\\studentid.txt"
#     with open(filepath,"r") as f:
#         linesData = f.readlines()
#         for line in range(0,len(linesData)):
#             try:
#                 # 获取studentid 并去除换行
#                 studentid = linesData[line].rstrip("\n")
#                 # print studentid
#                 print("第"+str(line)+"个"+"学生id："+studentid)
#             except Exception,e:
#                 print(e)
#                 continue
#
# # foreachFile()

import datetime

print   "hello world"



print int(1519574400181)

localtime = time.localtime(time.time())
print "本地时间为 :", localtime

print time.strftime("%Y-%m-%d", time.localtime())
# 获取上一天  2018-02-26
print (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%d")


def getYesterday(formatStr):
    """
    获取昨天的日期
    :return: 年-月-日
    """
    return (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(formatStr)

print getYesterday("%Y/%m/%d")


# 将格式字符串转换为时间戳
a = "2018-2-27 23:24:57"
print time.mktime(time.strptime(a,"%Y-%m-%d %H:%M:%S"))
print str(int(time.mktime(time.strptime(a,"%Y-%m-%d %H:%M:%S"))))
yesterday = "2018-2-27"
befor_timestamp = str(yesterday) + " 00:00:00"
after_timestamp = str(yesterday) + " 23:59:59"
print str(int(time.mktime(time.strptime(befor_timestamp, "%Y-%m-%d %H:%M:%S"))))
print str(int(time.mktime(time.strptime(after_timestamp, "%Y-%m-%d %H:%M:%S"))))



def gettopicIds():
    """
    获取需要抓取的栏目的id
    :return:
    """
    return (19,13,38,41,15)

topicIds = gettopicIds()
for i in topicIds:
    print(str(i))