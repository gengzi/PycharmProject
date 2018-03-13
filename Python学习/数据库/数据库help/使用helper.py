# -*- coding:utf-8 -*-
import MySQLdb
# 引用mysql
from MysqlHelper import *


mysql = MysqlHelper(host="123.206.30.117",user="root",passwd="111",db="1024",port=3306)

def selectVideoUrl(params):
    """
    查询指定索引的视频索引
    :param params: 参数list
    :return:
    """
    sql = "select count(vid)  from huli11 where isdowlond is null  limit %s , %s"
    return mysql.get_all(sql=sql,params=params)






if __name__ == "__main__":
    # sql = "insert into student(name,age,passwd) values(%s,%s,%s)"
    # name = raw_input("请输入您的名字：")
    # age = raw_input("请输入您的年龄:")
    # passwd = raw_input("请输入您的密码:")
    # params =[name,age,passwd]
    # print(params)
    #
    # mysqlconn = MysqlHelper(host="123.206.30.117",user="root",passwd="111",db="test",port=3306)
    # count = mysqlconn.insert(sql,params=params)
    # if count==1:
    #     print("ok")
    # else:
    #     print("error")
    params = (0,2000)
    print selectVideoUrl(params)















