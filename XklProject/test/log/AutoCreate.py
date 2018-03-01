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







list = ["studentId","schoolName","academyName","profession"]
for item in list:
    create(item)