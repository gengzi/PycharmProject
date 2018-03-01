# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# class Student:
#     pass


class Student(object):

    """
      `studentId` varchar(20) NOT NULL COMMENT '学生编号',
  `schoolName` varchar(255) DEFAULT NULL COMMENT '学校名称',
  `academyName` varchar(255) DEFAULT NULL COMMENT '学院',
  `profession` varchar(255) DEFAULT NULL COMMENT '专业',
  `academyId` varchar(255) DEFAULT NULL COMMENT '学历',
  `grade` varchar(255) DEFAULT NULL COMMENT '入学年份',
  `nickName` varchar(255) DEFAULT NULL COMMENT '姓名',
  `pinyinStr` varchar(255) DEFAULT NULL COMMENT '姓名拼音',
  `bornDate` varchar(255) DEFAULT NULL COMMENT '出生日期',
  `hometown` varchar(255) DEFAULT NULL COMMENT '所在地',
  `gender` int(1) DEFAULT NULL,
  `source` varchar(255) DEFAULT NULL COMMENT '手机类型',


    """

    @property
    def studentId(self):
        return self._studentId

    @studentId.setter
    def studentId(self,value):
        self._studentId = value

    @property
    def studentId(self):
        return self._studentId

    @studentId.setter
    def studentId(self, value):
        self._studentId = value

    @property
    def schoolName(self):
        return self._schoolName

    @schoolName.setter
    def schoolName(self, value):
        self._schoolName = value

    @property
    def academyName(self):
        return self._academyName

    @academyName.setter
    def academyName(self, value):
        self._academyName = value

    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, value):
        self._profession = value



# stu = Student()
# stu.score = 1001
#
# print stu.score