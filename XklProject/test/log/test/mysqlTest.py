# -*- coding:utf-8 -*-


from PycharmProject.XklProject.test.log.MysqlHelper import *
from PycharmProject.XklProject.test.log.Student import *

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 初始化mysql
mysql = MysqlHelper(host="123.206.30.117",user="root",passwd="111",db="xklinfo",port=3306)


def selectDirPathByMD(time):
    """
    返回对应日期的文件地址
    :param time: 年-月-日
    :return: 每一个文件的路径 str
    """
    sql = "select datajson from messagedata where nowtime = %s"
    param = [time]
    return mysql.get_all(sql=sql,params=param)




def insertStudentid2Studnet(student):
    """
    插入该学生的id，重复的id 会被主键拦截
    :param student: 学生信息
    :return: 是否成功
    """
    insterid_sql = "insert into student(studentId) values(%s)"
    param = [student.studentId]
    count = mysql.insert(sql=insterid_sql,params=param)
    if count >= 1:
        return "success"
    else:
        return "error"

student  = Student()
student.studentId = "1111"
print insertStudentid2Studnet(student)


# print selectDirPathByMD("2018-02-27")

