# -*- coding:utf-8 -*-
import MySQLdb

def connectionMysql():
    """
    :return: 返回sql连接
    """
    db = MySQLdb.connect(host="123.206.30.117",user="root",passwd="111",db="test",port=3306,charset="utf8")

    return  db

def insert(db):
    """
    插入一条数据
    :param cursor:
    :return:
    """
    cursor =db.cursor()
    sql  = "insert into student(name,passwd,age) values('张三','111',22)"
    count = cursor.execute(sql)
    print(count)
    db.commit()
    db.close()




def delete(db):
    cursor = db.cursor()
    sql = "delete from student where id =2"
    count = cursor.execute(sql)
    print(count)
    db.commit()
    db.close()

def update(db):
    cursor = db.cursor()
    sql = "update student set  name='李四',age =233  where id =3"
    count = cursor.execute(sql)
    print(count)
    db.commit()
    db.close()



def createTable(cursor):
    """
    创建一张表
    :param cursor:
    :return:
    """
    cursor.execute("DROP TABLE IF EXISTS student");
    sql ="""
         CREATE TABLE student (
              id int(11) NOT NULL AUTO_INCREMENT,
              name varchar(255) DEFAULT NULL,
              age int(11) DEFAULT NULL,
              passwd varchar(255) DEFAULT NULL,
              PRIMARY KEY (id)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """

    cursor.execute(sql)
    print "完成"
    cursor.close()

if __name__ == "__main__":
   db  = connectionMysql()
   cursor = db.cursor()
   # 创建数据库表
   # createTable(cursor)
   # 插入一条数据
   # insert(db)
   # 删除一条
   # delete(db)
   #更新一条
   # update(db)









