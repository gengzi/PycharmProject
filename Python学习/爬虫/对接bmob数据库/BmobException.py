#!/usr/bin/env python2
# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习
import sys
reload(sys)
sys.setdefaultencoding('utf8')  #设置系统编码格式


class BmobException(Exception):
    def __init__(self, ErrorInfo):
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo





# if __name__ == '__main__':
#     try:
#         raise BmobException('客户异常')
#     except BmobException as e:
#         print(e)
