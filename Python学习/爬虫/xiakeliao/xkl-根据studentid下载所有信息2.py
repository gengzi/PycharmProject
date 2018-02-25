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
dirpath = "I:\\python\\xkl\\allstudent\\info\\"
redirPath =""

def search(path, word):
    """
        查找文件
    :param path: 目录
    :param word: 文件名
    :return: 符合的文件路径
    """
    list = []
    for filename in os.listdir(path):
        # 遍历所有的文件
        fp = os.path.join(path, filename)
        # 判断 word 是否在文件名中
        if os.path.isfile(fp) and word in filename:
            list.append(fp)
        # 没有，递归循环到子目录中
        elif os.path.isdir(fp):
            search(fp, word)
    return  list


def foreachFile():
    #目录
    filepath  ="I:\\python\\xkl\\allstudent\\studentid.txt"
    with open(filepath,"r") as f:
        linesData = f.readlines()
        for line in range(0,len(linesData)):
            try:
                if line > 3000:
                    # 获取studentid 并去除换行
                    studentid = linesData[line].rstrip("\n")
                    print("第"+str(line)+"个"+"学生id："+studentid)
                    filepathList = search(dirpath,str(studentid))
                    print(filepathList)
                    download(filepathList)
            except Exception,e:
                print(e)
                continue


def download(filepathList):
    # 遍历list 集合，根据是否有_ 来区分是否是不同的文件
    for index in range(0,len(filepathList)):
        print(filepathList[index])
        item = str(filepathList[index])
        if "_" in str(item):
            # 包含，分页数据
            studentEInfo(item,redirPath)
        else:
            # 不包含，基本数据
            studentInfo(item)

def studentEInfo(filepath,filename):
    """
        分页数据
    :param filepath: 文件路径
    :return: img
    """
    print filepath
    with open(filepath,"r") as f:
        filecontent  = f.read()
        jsondata = json.loads(filecontent)
        data = jsonpath.jsonpath(jsondata, "$.data.messageBOs[*]")
        if data != False:
            for i in range(0, len(data)):
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
                        upload_time = sj[0]
                        time_local = time.localtime(int(str(upload_time)[0:10]))
                        upload_time = time.strftime("%Y-%m-%d", time_local)
                        for photo in range(0, len(photo)):
                            photo = jsonpath.jsonpath(studentdata, "$..qiniuImgBOs[" + str(photo) + "].url")
                            imagename = str(phonelx[0]) + "-" + unicode(str(studentName[0]).encode('utf-8'),
                                                                        "utf-8") + "-" + str(uuid.uuid1()) + ".jpg"
                            download_img(str(photo[0]), filename + "\\" + imagename)

                except Exception, e:
                    print(e)
                    continue


def studentInfo(filepath):
    """
        下载基本的数据
    :param filepath: 文件的路径
    :return: img
    """
    with open(filepath, "r") as f:
        content = f.read()
        jsondata = json.loads(content)
        InfoByIdV4 = jsonpath.jsonpath(jsondata, "$..InfoByIdV4")
        topInfo_data = jsonpath.jsonpath(jsondata, "$..topInfo")
        indexInfo_data2 = jsonpath.jsonpath(jsondata, "$..indexInfo")
        albumWallList_data = jsonpath.jsonpath(jsondata, "$..albumWallList")

        # 开始解析
        # print(str(topInfo_data[0]))
        InfoByIdV4_data = json.loads(str(InfoByIdV4[0]))
        # 学校
        stu_school = str(jsonpath.jsonpath(InfoByIdV4_data, "$..schoolName")[0])
        print stu_school
        # 学院
        stu_academy = str(jsonpath.jsonpath(InfoByIdV4_data, "$..academyName")[0])
        print stu_academy
        # 专业
        stu_profession = jsonpath.jsonpath(InfoByIdV4_data, "$..profession")
        if stu_profession != False:
            print stu_profession[0]
        else:
            stu_profession = "无专业信息"
        # 入学年份
        stu_grade = str(jsonpath.jsonpath(InfoByIdV4_data, "$..grade")[0])
        stu_grade = "20"+stu_grade
        print stu_grade
        # 昵称
        stu_nickName = str(jsonpath.jsonpath(InfoByIdV4_data, "$..nickName")[0])
        print stu_nickName
        # 昵称拼音
        stu_pinyinStr = str(jsonpath.jsonpath(InfoByIdV4_data, "$..pinyinStr")[0])
        print stu_pinyinStr
        # 出生日期
        stu_bornDate = str(jsonpath.jsonpath(InfoByIdV4_data, "$..bornDate")[0])
        if stu_bornDate == "0":
            stu_bornDate = "无出生年月"
        else:
            time_local = time.localtime(int(stu_bornDate[0:9]))
            stu_bornDate = time.strftime("%Y-%m-%d", time_local)
        print stu_bornDate
        # 居住地
        stu_hometown = jsonpath.jsonpath(InfoByIdV4_data, "$..hometown")
        if stu_hometown != False:
            print(stu_hometown[0])
            stu_hometown = stu_hometown[0]
        else:
            stu_hometown = "无家乡信息"

        # 性别
        stu_gender = str(jsonpath.jsonpath(InfoByIdV4_data, "$..gender")[0])
        if stu_gender == "0":
            stu_gender = "女"
        else:
            stu_gender = "男"
        print stu_gender
        # 个性签名
        stu_signature = jsonpath.jsonpath(InfoByIdV4_data, "$..signature")
        if stu_signature != False:
            print(stu_signature[0])
            stu_signature = stu_signature[0]
        else:
            stu_signature = "无个性签名"

        # 创建目录
        dirname = "I:\\python\\xkl\\allstudent\\allinfo\\" + stu_school + "     -" + stu_grade + "      -" + stu_academy + "        -" + stu_nickName + "       -" + stu_pinyinStr + "      -" + stu_gender + "     -" \
                  + stu_bornDate + "        -" + stu_hometown + "\\"
        dirname = unicode(str(dirname).encode('utf-8'), "utf-8")
        isExists = os.path.exists(dirname)
        if not isExists:
            os.makedirs(dirname)
            print dirname + ' 创建成功'
        else:
            raise Exception('重复')


        # 头像 img
        tx_img = str(jsonpath.jsonpath(InfoByIdV4_data, "$..avatarUrl")[0])
        download_img(tx_img,dirname+stu_nickName+str(uuid.uuid1())+".jpg")
        # 以前的头像
        stu_photoBO = jsonpath.jsonpath(InfoByIdV4_data, "$..photoBO[*]")
        if stu_photoBO != False:
            for index in range(0,len(stu_photoBO)):
                photo = jsonpath.jsonpath(stu_photoBO, "$.[" + str(index) + "].photoUrl")
                print(photo[0])
                download_img(str(photo[0]), dirname+stu_nickName+str(uuid.uuid1())+".jpg")


        # 头像下面的照片
        albumWallList = json.loads(str(albumWallList_data[0]))
        img = jsonpath.jsonpath(albumWallList, "$..list[*]")
        if img != False:
            for index in range(0,len(img)):
                imgurl = jsonpath.jsonpath(img[index], "$..imgInfoBO.url")
                print(imgurl[0])
                download_img(str(imgurl[0]), dirname+stu_nickName+str(uuid.uuid1())+".jpg")

        global  redirPath
        redirPath = dirname


        # print(str(albumWallList_data[0]))

def download_img(url,imagename):
    try:
        imagename = unicode(str(imagename).encode('utf-8'), "utf-8")
        start_time = time.time()
        print(url)
        print(imagename)
        req = requests.get(url, headers=headers, timeout=10)
        spcontent = req.content
        # 下载图片
        with open(imagename, "wb") as code:
            code.write(spcontent)
        end_time = time.time() - start_time
        print("耗时：" + str(end_time))
    except Exception, e:
        print(e)



if __name__ == "__main__":
    #解析txt
    foreachFile()







