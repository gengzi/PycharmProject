# -*- coding:utf-8 -*-
from  XklProject.tools.MysqlHelper import *

if __name__ == "__main__":
    mysqlHelper = MysqlHelper(host='123.206.30.117', port=3306, passwd='111',user='root',db="test")
    sql ="select * from student"
    print mysqlHelper.get_all(sql)












