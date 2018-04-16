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
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from MysqlHelper import *
"""
    模拟请求一个学生的id，获取主页信息
    author：gengzi
    version：0.0.1.3
    sj：2018年2月13日13:00:54
"""
# headers
headers = {"User-Agent": 'okhttp/3.6.0'}
# 初始化mysql
mysql = MysqlHelper(host="123.206.30.117",user="root",passwd="111",db="xklinfo",port=3306)
#学生文件存在的路径
stupath = "H:\\python_workspace\\studentinfo"
#保存文件的路径
savefile="H:\\python_workspace\\xkl\\student\\"

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

def insertStudentInfo(param):
    try:
        upsql = "update student set schoolName = %s,academyName=%s,profession=%s,grade=%s," \
                "nickName=%s,pinyinStr=%s,bornDate=%s,hometown=%s,gender=%s,signature=%s where studentId=%s"
        params = param
        mysql.update(sql=upsql,params=params)
    except Exception,e:
        print(e)
        return


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


        #stu_school  学校
        #stu_grade 入学年份
        #stu_academy 学院
        #stu_profession 专业
        #stu_nickName 网名
        #stu_pinyinStr 网名拼音
        #stu_gender 性别
        #stu_bornDate 出生日期
        #stu_hometown 家乡
        #stu_signature 个性签名
        #先执行插入数据库操作
        stu_id =filepath.split("\\")[-1].split(".")[0];
        stuparam = [str(stu_school),str(stu_academy),str(stu_profession),str(stu_grade),str(stu_nickName),str(stu_pinyinStr),
                    str(stu_bornDate),str(stu_hometown),str(stu_gender),str(stu_signature),str(stu_id)]
        insertStudentInfo(stuparam)

        # 创建目录
        dirname = savefile +stu_id+";"+ stu_school + "     -" + stu_grade + "      -" + stu_academy + "        -" + stu_nickName + "       -" + stu_pinyinStr + "      -" + stu_gender + "     -" \
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


def getStudentIdByLimit():
    """
     查询数据库，分页查询student表的学生id
    :return:
    """
    sql = "SELECT studentId from student where nickName is null and studentId != '0' and infodirpath is not null LIMIT 0,100"
    idlist = mysql.get_all(sql=sql)
    return idlist





if __name__ == "__main__":
    #下载已经存在的学生信息
    #[1]分页查询数据库,每页100条
    for i in range(0,220):
        time.sleep(30)
        idlist = getStudentIdByLimit();
        #遍历这个list
        for i in range(0,len(idlist)):
            studentid =  idlist[i][0]
            #[2]根据id查询目录中对应的学生文件
            stulist = search(stupath,studentid)
             #遍历这个list
            for j in range(0,len(stulist)):
                idpath  = stulist[j]
                #[3]解析json，进行入库操作
                try:
                    studentInfo(idpath)
                    time.sleep(2)
                except Exception,e:
                    print(e)
                    continue








