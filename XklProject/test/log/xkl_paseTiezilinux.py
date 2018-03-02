# -*- coding:utf-8 -*-

import json
import jsonpath
import log
import logging
from DateUtils import  *
from MysqlHelper import *
from FileUtils import *
from Student import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')


"""
    解析抓取的帖子数据
    author：gengzi
    version：0.0.1.3
    sj：2018年2月27日23:43:35
"""

logger = logging.getLogger("xkl")
# 初始化mysql
mysql = MysqlHelper(host="123.206.30.117",user="root",passwd="111",db="xklinfo",port=3306)

def parseContentByJSONPATH(content):
    """
    解析content 内容 使用jsonpath
    :param content:  json数据
    :return: Studnet
    """
    jsondata = json.loads(content)
    data = jsonpath.jsonpath(jsondata, "$.data.messageBOs[*]")
    for i in range(0, len(data)):
        try:
            studentdata = jsonpath.jsonpath(jsondata, "$.data.messageBOs[" + str(i) + "]")
            # id
            studentid = jsonpath.jsonpath(studentdata, "$..studentBO.id")

            # 对象赋值
            student = Student()
            student.studentId = studentid

            #执行sql语句
            count = insertStudentid2Studnet(student)
            if count >= 1:
                logger.info("success")
            else:
                logger.info("插入失败"+str(student))
        except Exception,e:
            logger.info(e)
            logger.info("解析出现异常")
        continue

def insertStudentid2Studnet(student):
    """
    插入该学生的id，重复的id 会被主键拦截
    :param student: 学生信息
    :return: 是否成功
    """
    insterid_sql = "insert into student(studentId) values(%s)"
    print student.studentId
    param = student.studentId
    return mysql.insert(sql=insterid_sql,params=param)

def selectDirPathByMD(time):
    """
    返回对应日期的文件地址
    :param time: 年-月-日
    :return: 每一个文件的路径 str
    """
    sql = "select datajson from messagedata where nowtime = %s"
    params = [time]
    return mysql.get_all(sql=sql,params=params)

if __name__ == "__main__":
    logger.info("<<<<<<<<<<<<<<<<<<<<<<解析帖子数据开始>>>>>>>>>>>>>>>>>>>>>>>>")

    #帖子数据中，有非常多的数据，现在只获取其中的 学生编号，存入sql 文件中， 并去除
    #[1] 读取昨天linux 的本地txt文件
    yesterday = getYesterday("%Y-%m-%d")
    # 从数据库中读取路径信息
    dirpaths = selectDirPathByMD(yesterday)
    for filepath in dirpaths:
        #读取每一个文件
        logger.info("打开文件："+filepath[0])
        try:
            with open(str(filepath[0])) as f:
                 content = f.read()
            #[2]解析内容
            parseContentByJSONPATH(content=content)

        except Exception,e:
            logger.info(e)
            logger.info("该文件"+str(filepath[0])+"不存在本地的目录：")
        # 出现异常就执行下一个
        continue

    logger.info("<<<<<<<<<<<<<<<<<<<<<<解析帖子数据结束>>>>>>>>>>>>>>>>>>>>>>>>")












