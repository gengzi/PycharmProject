# -*- coding:utf-8 -*-
from wechat_sender import Sender
import requests
import time
import json
import os
import jsonpath
import datetime
import MySQLdb
import sys
from DateUtils import *
from PycharmProject.XklProject.test.log import Student

reload(sys)
sys.setdefaultencoding('utf8')
import log
import logging
from MysqlHelper import *
"""
    author：gengzi
    version：0.0.1.3
    sj：2018年2月27日23:43:35
"""
headers = {"User-Agent": 'okhttp/3.6.0'}
posturl = "http://120.55.151.61/V2/Treehole/Message/getMessageByTopicIdV5.action"
logger = logging.getLogger("xkl")
# 初始化mysql
mysql = MysqlHelper(host="123.206.30.117",user="root",passwd="111",db="xklinfo",port=3306)

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


def login():
    """
    登陆，返回登陆成功的session
    :return:  session
    """
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
        logger.error(e)
        logger.error("登陆失败")



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
    filename =  "F:\\python\\xiakeliao\\"+studentid+".txt"
    with open(filename,"w") as f:
        f.write(json.dumps(Jsondata))
    logger.info("一般信息："+filename)
    return  filename




def insertData(dirpath,studentid):
    """
    将数据写入数据库
    :param response: 响应的json数据
    :param formatTime: 年月日时分秒
    :param topicId: 栏目的编号
    :param timestamp: 时间戳
    :param formatTimeday: 年月日
    :return: 是否成功
    """
    try:
        time = getNewFormatTime("%Y-%m-%d %H:%M:%S")
        params = [str(dirpath),str(time),str(studentid)]
        sql ="update  student set infodirpath= %s,updatetime= %s where studentId= %s"
        mysql.insert(sql=sql,params=params)
    except Exception,e:
        logger.error(e)
        logger.error("插入数据库失败"+dirpath)


def selectStuID():
    """
    分页查询所有的学生id
    :return:
    """
    sql ="SELECT  studentId  FROM student  where updatetime IS  NULL LIMIT 0,500"
    param = []
    return mysql.get_all(sql=sql,params=param)

def downloadInfoByID(studentid,session):
    """
    根据学生id下载该学生的主页数据
    :param studentid: 学生id
    :param session: 登陆的session
    :return:
    """
    dirpath = loadStrduentInfo(studentid=studentid,loginSession=session)
    #执行插入数据库的操作
    insertData(dirpath,studentid)



def selectNoDownStudentCount():
    """
    查询没有被查询的学生的个数
    :return:
    """
    sql = "SELECT  count(studentId)  FROM student  where updatetime IS  NULL "
    param = []
    return mysql.get_one(sql=sql, params=param)



if __name__ == "__main__":
    send = Sender()
    # 每24个小时调用一次

    # [1]拿到登陆成功的session
    session = login()
    logger.info("<<<<<<<<<<<<<<<<<<<<<<爬取个人数据开始>>>>>>>>>>>>>>>>>>>>>>>>")

    #[2]读取数据库，拿到studentid，爬取每一个学生的信息和贴子数据
    StudentIDlist = selectStuID()

    if len(StudentIDlist) > 0:
        for studentid in StudentIDlist:
            studentid = str(studentid[0])
            logger.info("爬取"+studentid+"这名学生的主页")
            try:
                #根据id，爬取数据
                downloadInfoByID(studentid,session)
                time.sleep(20)
            except Exception,e:
                logger.error(e)
                logger.error("访问"+studentid+"这名学生的信息出错")
                continue
    else:
        logger.info("<<<<<<<<<<<<<<<<<<<<<<学生现在已经全部查取完毕>>>>>>>>>>>>>>>>>>>>>>>>")






