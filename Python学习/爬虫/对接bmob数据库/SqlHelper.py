#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习

import sys
reload(sys)
sys.setdefaultencoding('utf8')  #设置系统编码格式
import ConfigParser
import requests
import jsonpath
import json



cf = ConfigParser.ConfigParser()
cf.read("./Bmob.conf")
dbname = cf.get("db", "dbaname")
applicationID = cf.get("app", "applicationID")
restapikey = cf.get("app", "restapikey")
inserturl = cf.get("insert", "inserturl")

headers = {
    "X-Bmob-Application-Id":applicationID,
    "X-Bmob-REST-API-Key":restapikey,
    "User-Agent": 'okhttp/3.6.0',
    "Content-Type":"application/json",
}

# print dbname
# print applicationID
# print restapikey


class SqlHelper():
    """
     Restful 风格的bmob 数据库操作
    """

    def __int__(self,dbname=dbname,applicationID=applicationID,restapikey=restapikey):
        # 读取配置文件
        self.dbname =dbname
        self.applicationID = applicationID
        self.restapikey = restapikey


    def getOne(self):
        pass

    def getAll(self):
        pass





    def insert(self,tablename,datajson,inserturl=inserturl):
        """
          插入数据
        :return:
        """
        try:
            url = inserturl+str(tablename)
            response = requests.post(url=url,headers=headers,data=datajson)
            if response == "201":
                Location  = response.headers.get("Location")
                print(Location)
                content = response.text
                print content
            pass
        except Exception,e:
            print(e)

