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
from BmobException import *



cf = ConfigParser.ConfigParser()
cf.read("./Bmob.conf")
dbname = cf.get("db", "dbaname")
applicationID = cf.get("app", "applicationID")
restapikey = cf.get("app", "restapikey")
inserturl = cf.get("insert", "inserturl")

Insertheaders = {
    "X-Bmob-Application-Id":applicationID,
    "X-Bmob-REST-API-Key":restapikey,
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
        :param tablename: 数据表名称
        :param datajson: 插入的数据，字典格式
        :param inserturl: 插入的数据的url
        :return: success 成功， error 出现错误
        """
        try:
            url = inserturl+str(tablename)
            response = requests.post(url=url,headers=Insertheaders,data=json.dumps(datajson))
            #如果返回的是 201 就是插入成功
            if response.status_code == 201:
                print response
                Location  = response.headers.get("Location")
                print(Location)
                content = response.text
                return "success"
                # 如果返回的是 404 就会有错误信息
            elif response.status_code == 404:
                errorcontent = response.text
                raise BmobException("404错误："+errorcontent)
            else:
                errorcontent = response.text
                raise BmobException("其他错误：" + errorcontent)
        except BmobException,e:
            print(e)
            return "error"




if __name__ == "__main__":
    sql = SqlHelper()
    datajosn = {"studentId":"4"}
    print sql.insert(tablename="studentfile",datajson=datajosn)

