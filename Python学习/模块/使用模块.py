#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# 第2行注释表示.py文件本身使用标准UTF-8编码

' a test module '
# ' a test module ' 是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'gengzi'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("hello world")
    elif len(args) == 2:
        print("hello {}".format(args[1]))
    else:
        print("太多的参数值了")
#
# if __name__='__main__':
#     test()


# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
#
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
#
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
#
# 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。


# 定义私有的变量

def _private_1(name):
    print(name)

def printstr(name):
    _private_1(name)


printstr("你好")