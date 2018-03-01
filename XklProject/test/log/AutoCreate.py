# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def create(param):


    print "@property"
    print "def "+param+"(self):"
    print "    return self._"+param

    print "@"+param+".setter"
    print "def "+param+"(self,value):"
    print "    self._"+param+" = value"



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




list = ["studentId","schoolName","academyName","profession","academyId","grade","nickName","pinyinStr","bornDate","hometown","gender","source"]
for item in list:
    create(item)