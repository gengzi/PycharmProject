# -*- coding:utf-8 -*-
import MySQLdb

def connectionMysql():
    """
    :return: 返回sql连接
    """
    db = MySQLdb.connect(host="123.206.30.117",user="root",passwd="111",db="test",port=3306,charset="utf8")

    return  db

def selectone(db):
    """
    查询一条
    :param db:
    :return:
    """

    cursor = db.cursor()
    sql = "select * from student where id =1"
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)

    db.close()
    cursor.close()

def selectmore(db):
    """
    查询多条
    :param db:
    :return:
    """
    cursor = db.cursor()
    sql = "select * from student"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

    db.close()
    cursor.close()







if __name__ == "__main__":
   db  = connectionMysql()
   cursor = db.cursor()
   selectmore(db)










