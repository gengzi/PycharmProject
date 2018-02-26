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
    try:
        db = MySQLdb.connect(host="123.206.30.117",user="root",passwd="111",db="test")
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("数据库的版本%s",data)
        db.close()
    except Exception,e:
        print(e)



if __name__ == "__main__":
    connectionMysql()






