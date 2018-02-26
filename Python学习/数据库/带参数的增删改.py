# -*- coding:utf-8 -*-
import MySQLdb

def connectionMysql():
    """
    :return: 返回sql连接
    """
    db = MySQLdb.connect(host="123.206.30.117",user="root",passwd="111",db="test",port=3306,charset="utf8")

    return  db

def insert(db,name):
    """
    带参数的插入
    :param db:
    :param name:
    :return:
    """
    cursor = db.cursor()
    params = [name]
    sql = "insert into student(name) values(%s)"
    count = cursor.execute(sql,params)
    print(count)
    db.commit()
    cursor.close()
    db.close()




if __name__ == "__main__":
   db  = connectionMysql()
   cursor = db.cursor()
   name = raw_input("请输入您的名字：")
   insert(db,name)










