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
    解析json数据
    author：gengzi
    version：0.0.1.3
    sj：2018年2月13日13:00:54
"""
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

def download(url,imagename):
    try:
        start_time = time.time()
        time.sleep(1)
        print(url)
        req = requests.get(url, headers=headers, timeout=10)
        spcontent = req.content
        # 下载图片
        with open(imagename, "wb") as code:
            code.write(spcontent)
        end_time = time.time() - start_time
        print("耗时：" + str(end_time))
    except Exception, e:
        print(e)


def loadJson(filepath):
    """
        读取本地文件的json数据，解析出需要下载的文件
    :return:
    """
    print(filepath)
    # file = open(filepath,"rU")
    # content = file.readline()
    fileList = open(filepath,"r").readlines()
    for index,filecontent in enumerate(fileList):
        print("第"+str(index)+"行")
        jsondata = json.loads(filecontent[index])
        data = jsonpath.jsonpath(jsondata,"$.data.messageBOs[*]")
        for i  in range(0,len(data)):
            try:
                studentdata = jsonpath.jsonpath(jsondata, "$.data.messageBOs[" + str(i) + "]")
                # 学校名字
                schooleName = jsonpath.jsonpath(studentdata, "$..schoolName")
                # 手机类型
                phonelx = jsonpath.jsonpath(studentdata, "$..source")
                # 头像
                studenttx = jsonpath.jsonpath(studentdata, "$..studentBO.fullAvatarUrl")
                # id
                studentid = jsonpath.jsonpath(studentdata, "$..studentBO.id")
                # 上传时间
                sj = jsonpath.jsonpath(studentdata, "$..issueTime")
                # 姓名
                studentName = jsonpath.jsonpath(studentdata, "$..studentBO.nickName")

                # 照片的个数
                photo = jsonpath.jsonpath(studentdata, "$..qiniuImgBOs[*]")
                if schooleName != False:
                    # print(schooleName[0])
                    # print(phonelx[0])
                    # 格式化时间 1518441204000
                    upload_time = sj[0]
                    time_local = time.localtime(int(str(upload_time)[0:10]))
                    upload_time = time.strftime("%Y-%m-%d", time_local)
                    # print(upload_time)
                    # 格式化头像 http://qiniu.myfriday.cn/2_4003_27016263_1507248286166.jpg?imageView2/1/w/110/h/110/q/90
                    filename1 = time.strftime("%Y-%m-%d", time.localtime())
                    filename2 = schooleName[0]
                    filename3 = str(studentid[0]) + "-" + str(studentName[0])
                    filename4 = upload_time
                    filename = "I:\\" + unicode(str(filename1).encode('utf-8'), "utf-8")+ "\\" + str(filename2) + "\\" + unicode(str(filename3).encode('utf-8'), "utf-8") + "\\" + str(
                        filename4)
                    print(filename)
                    isExists = os.path.exists(filename)
                    if not isExists:
                        os.makedirs(filename)
                        print filename + ' 创建成功'
                    tx = str(studenttx[0]).split("?")[0]
                    download(tx,filename+"\\"+str(uuid.uuid1())+".jpg")
                    # 下载头像
                    # print(studentid[0])
                    # print(studentName[0])
                    for photo in range(0, len(photo)):
                        photo = jsonpath.jsonpath(studentdata, "$..qiniuImgBOs[" + str(photo) + "].url")
                        imagename = str(phonelx[0])+"-"+unicode(str(studentName[0]).encode('utf-8'),"utf-8")+"-"+str(uuid.uuid1())+".jpg"
                        download(str(photo[0]),filename+"\\"+imagename)

            except Exception, e:
                print(e)
                continue


if __name__ == "__main__":
    try:
        filename = time.strftime("%Y-%m-%d", time.localtime())
        loadJson("H:\\python\\xiakeliao\\"+str(filename)+".txt")
    except Exception, e:
        print(e)



    # filename = "I:\\aa\\bb\\bbb\\vvvv"
    # isExists = os.path.exists(filename)
    # if not isExists:
    #     os.makedirs(filename)
    #     print filename + ' 创建成功'




