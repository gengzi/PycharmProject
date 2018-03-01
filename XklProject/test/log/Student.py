# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Student(object):
    """
      `studentId` '学生编号',
      `schoolName` '学校名称',
      `academyName` '学院',
      `profession` '专业',
      `academyId` '学历',
      `grade` '入学年份',
      `nickName` '姓名',
      `pinyinStr` '姓名拼音',
      `bornDate` '出生日期',
      `hometown` '所在地',
      `gender` 性别 数字 1男 0女 -1 不知道,
      `source` '手机类型',
    """
    # def __init__(self,studentId,schoolName,academyName,profession,academyId,grade,nickName,pinyinStr,bornDate,hometown,gender,source):
    #     self.studentId = studentId
    #     self.schoolName = schoolName
    #     self.academyName = academyName
    #     self.profession = profession
    #     self.academyId = academyId
    #     self.grade = grade
    #     self.nickName = nickName
    #     self.pinyinStr = pinyinStr
    #     self.bornDate = bornDate
    #     self.hometown = hometown
    #     self.gender = gender
    #     self.source = source


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

    @property
    def academyId(self):
        return self._academyId

    @academyId.setter
    def academyId(self, value):
        self._academyId = value

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value

    @property
    def nickName(self):
        return self._nickName

    @nickName.setter
    def nickName(self, value):
        self._nickName = value

    @property
    def pinyinStr(self):
        return self._pinyinStr

    @pinyinStr.setter
    def pinyinStr(self, value):
        self._pinyinStr = value

    @property
    def bornDate(self):
        return self._bornDate

    @bornDate.setter
    def bornDate(self, value):
        self._bornDate = value

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        self._hometown = value

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value






#测试
# stu = Student()
# stu.score = 1001
#
# print stu.score

