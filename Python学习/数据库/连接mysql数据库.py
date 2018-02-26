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
import os
# 导入mysqldb 库
import MySQLdb



def connectionMysql():
    """
        连接mysql服务
    :return:
    """

    # 获取数据库连接
    db = MySQLdb.connect(host="123.206.30.117",user="root",passwd="111",db="test",port=3306,charset="utf8")
    # 返回游标对象
    cursor = db.cursor()
    # 执行sql语句，返回受影响的行数
    cursor.execute("SELECT VERSION()")
    # 执行查询，获取第一个行数据，返回一个元组
    data = cursor.fetchone()
    print('version :'+str(data[0]))
    # 关闭连接
    db.close()




if __name__ == "__main__":
    connectionMysql()






