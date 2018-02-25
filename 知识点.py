# -*- coding:utf-8 -*-
# Hello world - 西蒙.科泽斯 这是“向编程之神所称颂的传统咒语，愿他帮助并保佑你更好的学习这门语言”


# 面向对象编程分 类 和 对象
#
# 一个类（Class）能够创建一种新的类型（Type），其中对象（Object）就是类的实例（Instance）。


# 对象可以使用属于它的普通变量来存储数据。这种从属于对象或类的变量叫作字段（Field）。
# 对象还可以使用属于类的函数来实现某些功能，这种函数叫作类的方法（Method）。

class Person:
    def say_hi(self):
        print('Hello, how are you?')
p = Person()
p.say_hi()

#python 会自动将其解析为 Person.say_hi(self)
# 前面两行同样可以写作
# Person().say_hi()
